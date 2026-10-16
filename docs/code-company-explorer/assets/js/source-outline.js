/* Source structure is a navigational outline, never a substitute for the original Java parser or company registry. */
function githubSourceUrl(f){
  return 'https://github.com/shopizer-ecommerce/shopizer/blob/'+PINNED_SHOPIZER_REF+'/'+f.path.split('/').map(encodeURIComponent).join('/');
}
function sourceIsText(f){
  if((f.size||0)>1600000)return false;
  return /\.(?:java|kt|groovy|scala|xml|html?|css|js|mjs|cjs|jsx|tsx|ts|json|ya?ml|properties|md|txt|sql|gradle|sh|bat|cmd|ps1|py|java|jsp|ftl|conf|ini|gitignore|editorconfig|csv|svg|dtd|xsd|graphql|adoc|rst|toml|lock|gitmodules|gitattributes)$/i.test(f.name) || /^(?:Dockerfile|Makefile|Jenkinsfile|LICENSE|NOTICE|README|pom\.xml|\.gitignore|\.editorconfig)$/i.test(f.name);
}
function importTarget(qualified){
  if(!qualified||qualified.endsWith('.*'))return null;
  const suffix='/src/main/java/'+qualified.replaceAll('.','/')+'.java';
  const hits=Object.entries(files).filter(([,f])=>f.path.endsWith(suffix));
  return hits.length===1?hits[0][0]:null;
}
function sourceBraceDelta(line){
  const noStrings=String(line).replace(/"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'/g,'""').replace(/\/\/.*$/,'');
  return (noStrings.match(/\{/g)||[]).length-(noStrings.match(/\}/g)||[]).length;
}
function buildJavaOutline(f){
  const lines=f.source||[],groups={package:[],imports:[],types:[],annotations:[],fields:[],methods:[],comments:[],initializers:[]};
  let depth=0,blockEnd=-1;
  for(let i=0;i<lines.length;i++){
    const text=String(lines[i]||''),t=text.trim(),n=i+1;
    if(blockEnd>=i){depth=Math.max(0,depth+sourceBraceDelta(text));continue;}
    if(t.startsWith('/**')||t.startsWith('/*')){
      let end=i;
      if(!t.includes('*/'))while(end+1<lines.length&&!String(lines[end]).includes('*/'))end++;
      groups.comments.push({line:n,end:end+1,label:(t.startsWith('/**')?'JavaDoc':'Block comment')+' · '+(end+1===n?'1 line':(end-i+1)+' lines'),description:'Original source documentation. Comments describe intent; they do not execute and are not numbered companies.'});
      blockEnd=end;continue;
    }
    if(t.startsWith('//')){
      groups.comments.push({line:n,label:t.slice(2).trim().slice(0,110)||'Line comment',description:'Original source comment (not executable code).'});continue;
    }
    let m=t.match(/^package\s+([\w.]+)\s*;/);
    if(m)groups.package.push({line:n,label:m[1],description:'Java namespace: identifies where this source type belongs in the project. A package is an address, not a running method.'});
    m=t.match(/^import\s+(?:static\s+)?([\w.*]+)\s*;/);
    if(m){
      const target=importTarget(m[1]);
      groups.imports.push({line:n,label:m[1],target,description:target?'Internal Shopizer source file: imported type can be opened in the project tree. The import itself does not invoke it.':'Import makes an external or unresolved Java type available; it does not execute code or imply an actual method call.'});
    }
    m=t.match(/^@([\w.]+)/);
    if(m&&(depth<=1))groups.annotations.push({line:n,label:t.slice(0,125),description:'Java annotation / metadata. Depending on the annotation, a framework may inspect it at build time or runtime; the line alone is not a method call.'});
    m=t.match(/\b(class|interface|enum|record|@interface)\s+([A-Za-z_$][\w$]*)/);
    if(m&&depth<=1){
      const parents=t.match(/\bextends\s+([\w.<>, ?]+)/),contracts=t.match(/\bimplements\s+([\w.<>, ?]+)/);
      groups.types.push({line:n,label:m[1]+' '+m[2]+(parents?' extends '+parents[1].trim():'')+(contracts?' implements '+contracts[1].trim():''),description:'Type declaration, inheritance and interface contract. Inherited behavior may come from a framework or another class and should not be presented as a direct invocation.'});
    }
    if(depth===1&&t&&!t.startsWith('@')){
      const method=t.match(/^(?:(?:public|protected|private|final|static|synchronized|abstract|native|default|strictfp)\s+)*(.+?)\s*\(/);
      if(method && !/^(?:if|while|for|switch|catch|return|throw|new)\b/.test(t) && !t.includes('= new ')){
        const name=method[1].trim().split(/\s+/).pop();
        const owner=Object.keys(entities).find(id=>entities[id].file===f.id&&entities[id].methodStart===n);
        groups.methods.push({line:n,label:name+'(…)'+(owner?' · Company '+entities[owner].no:' · not indexed'),company:owner||null,description:owner?'Verified method mapped to a numbered company.':'Method or constructor signature detected from source text; not yet assigned a company. Detection is a navigation aid, not a complete Java AST.'});
      }else if(/^(?:static\s*)\{$/.test(t)){
        groups.initializers.push({line:n,label:'Static initializer',description:'Runs during class initialization; a meaningful initializer may be reviewed as its own functional unit later.'});
      }else if(/^(?:(?:public|protected|private|static|final|transient|volatile)\s+)+/.test(t)&&t.includes(';')&&!t.startsWith('return ')){
        groups.fields.push({line:n,label:t.slice(0,145),description:'Class-level field or constant. Stores state or references a dependency; annotations such as @Inject/@Autowired may make framework wiring relevant.'});
      }
    }
    depth=Math.max(0,depth+sourceBraceDelta(text));
  }
  return groups;
}
/* Explain the selected non-company source line IN the existing code-footer, not in a second panel.
   An explanation is evidence-based: line text and known Java syntax, never a speculative company ID. */
function sourceLineFacts(f,n){
 const text=String(f.source?.[n-1]??''),line=text.trim();
 if(!line)return {kind:'Whitespace',explanation:'An empty spacer line. It separates nearby declarations or statements for readability; it does not execute code.'};
 if(!f.name.endsWith('.java')){
   if(line.startsWith('#')||line.startsWith('//'))return {kind:'Source comment',explanation:'A comment in this file. Its meaning depends on the file format and it is not executable Java.'};
   return {kind:'Original file content',explanation:'An original line from the pinned Shopizer file. This is not a numbered Java company; examine the surrounding configuration or source for its format-specific meaning.'};
 }
 if(!f.sourceFacts) {
   const groups=buildJavaOutline(f),exact=new Map();
   for(const [kind,items] of Object.entries(groups)){
     for(const item of items){
       for(let i=item.line;i<=(item.end||item.line);i++)if(!exact.has(i))exact.set(i,{kind,item});
     }
   }
   f.sourceFacts=exact;
 }
 const located=f.sourceFacts.get(n);
 const labelByKind={package:'Package declaration',imports:'Import declaration',types:'Type / inheritance',annotations:'Annotation',fields:'Class field',methods:'Java method / constructor',initializers:'Initializer block',comments:'Comment / JavaDoc'};
 if(located){
   const {kind,item}=located;
   if(kind==='package')return {kind:'Package / address',explanation:'Declares the Java package "'+item.label+'". This is the namespace/address of the class, not a method and not a call.',target:null};
   if(kind==='imports'){
     const imported=item.label,isStatic=/^import\s+static\b/.test(line);
     const origin=imported.startsWith('java.')||imported.startsWith('javax.')?'Java / Java EE API':imported.startsWith('org.springframework.')?'Spring framework':imported.startsWith('com.salesmanager.')?'Shopizer namespace':imported.startsWith('org.')||imported.startsWith('com.')?'Library or application type':'Java type or member';
     const what=isStatic?'Makes a static field or method available without repeating its class name.':'Makes this named type available by its short name elsewhere in this file.';
     return {kind:isStatic?'Static import':'Import / dependency',explanation:'Imports '+imported+' ('+origin+'). '+what+' Importing does not instantiate a class or call a method.'+(item.target?' The corresponding Shopizer source file can be opened here.':''),target:item.target||null};
   }
   if(kind==='types')return {kind:'Class / inheritance',explanation:'Declares '+item.label+'. If it extends a class, it inherits behavior; if it implements an interface, it promises a contract. This declaration is not a direct method call.'};
   if(kind==='fields'){
     const typeName=(line.match(/\b(?:private|protected|public)\s+(?:static\s+)?(?:final\s+)?([\w<>?.\[\], ]+?)\s+([A-Za-z_$][\w$]*)\s*(?:=|;)/)||[])[1];
     return {kind:'Field / dependency',explanation:'Declares class-level state: '+line+(typeName?' The declared type is '+typeName.trim()+'.':'')+' A field can store an injected service or application data; it is not a method company.'};
   }
   if(kind==='methods')return {kind:'Unnumbered Java method',explanation:'Method or constructor declaration: '+item.label+'. This is a code-section candidate not yet assigned a company ID. Full behavior must be reviewed from the complete method, not inferred from one line.'};
   if(kind==='initializers')return {kind:'Class initializer',explanation:'An initialization block. It may run when the class loads or an object is created, depending on whether it is static. Inspect its full block for effects.'};
   if(kind==='comments')return {kind:line.startsWith('/**')?'JavaDoc':line.startsWith('//')?'Comment':'Comment / JavaDoc',explanation:'Source documentation: '+(line.replace(/^\/?\*+\s*|^\/\/\s*|\*\/$/g,'').trim()||'comment delimiter or continuation')+'. It explains intent and does not execute.'};
 }
 const annotation=line.match(/^@([\w.]+)/);
 if(annotation){
   const name=annotation[1].split('.').at(-1);
   const desc={
     Autowired:'Spring injects a dependency into the annotated constructor, field or method.',
     Inject:'Standard dependency-injection annotation; a configured injector supplies the dependency.',
     Override:'Tells the compiler that the method should override a superclass method or implement an inherited interface method.',
     Bean:'Spring registers the value returned by the annotated method as an application-context bean.',
     Component:'Marks this type as a candidate for Spring component scanning.',
     Configuration:'Marks the class as a source of Spring configuration and bean definitions.',
     SpringBootApplication:'Combines core Spring Boot configuration, component scanning and auto-configuration.',
     EventListener:'Registers a method to react to a matching application event.',
     JsonIgnore:'Tells Jackson to ignore this member during JSON serialization or deserialization as applicable.',
     ServletComponentScan:'Enables discovery of supported servlet components.',
     RequestMapping:'Maps incoming HTTP requests to a controller or handler.',
     GetMapping:'Maps HTTP GET requests to this handler.',
     PostMapping:'Maps HTTP POST requests to this handler.',
     Transactional:'Configures transactional behavior when handled through Spring transaction infrastructure.',
     Value:'Injects a configured property or expression value.',
     SuppressWarnings:'Suppresses specified compiler warnings.'
   }[name]||'Java annotation metadata. The framework, compiler or reflection consumer decides its effect.';
   return {kind:'@'+name+' annotation',explanation:desc+' Original annotation: '+line};
 }
 if(/^(?:\/\*|\*|\*\/)/.test(line))return {kind:'Documentation or comment',explanation:'A JavaDoc/block-comment line or delimiter. Comments are not executed as Java statements.'};
 if(/^\/\//.test(line))return {kind:'Line comment',explanation:'A source comment describing or disabling nearby logic: '+line.slice(2).trim()+'. Java does not execute this line.'};
 if(/^(?:public|private|protected)?\s*(?:abstract\s+|final\s+)?(?:class|interface|enum|record)\s+/.test(line))return {kind:'Java type',explanation:'Declares a Java class/interface/record/enum. This defines a type; methods inside the type are separate functional units.'};
 if(/^\}\s*[;,]?$/.test(line))return {kind:'Closing brace',explanation:'Closes the surrounding method, type, conditional or initialization block. The precise owner is determined by the surrounding braces.'};
 if(/^\{\s*$/.test(line))return {kind:'Opening brace',explanation:'Opens a Java block or initialization body; the type of block is defined by the preceding declaration.'};
 if(/^(?:if|else\s+if)\s*\(/.test(line))return {kind:'Conditional',explanation:'Evaluates a condition and chooses whether to execute the following branch. Inspect the entire condition and block to understand what it checks.'};
 if(/^else\b/.test(line))return {kind:'Else branch',explanation:'Executes the alternative branch when the preceding if/else-if condition was not selected.'};
 if(/^(?:for|while|do)\b/.test(line))return {kind:'Iteration / loop',explanation:'Introduces a loop that repeats code subject to its condition. Review the loop boundaries and side effects.'};
 if(/^try\b/.test(line))return {kind:'Exception handling',explanation:'Opens a try block, where an exception may transfer control to a catch or finally block.'};
 if(/^catch\b/.test(line))return {kind:'Exception handler',explanation:'Catches a specified exception type so the application can handle that failure.'};
 if(/^finally\b/.test(line))return {kind:'Finally block',explanation:'Declares cleanup/finalization code that normally runs after the associated try/catch.'};
 if(/^return\b/.test(line))return {kind:'Return statement',explanation:'Returns control (and possibly a value or expression) to the caller. Exact expression: '+line};
 if(/^throw\b/.test(line))return {kind:'Throw exception',explanation:'Throws an exception to signal an error or interrupt normal execution: '+line};
 if(/^new\b/.test(line)||/\bnew\s+[A-Z]\w*\s*[(<]/.test(line))return {kind:'Object creation',explanation:'Creates an object or supplies a new instance as part of this statement. Inspect constructor arguments and its use: '+line};
 if(/^\b(?:private|public|protected|static|final|volatile|transient)\b/.test(line)&&/;\s*$/.test(line))return {kind:'Declaration',explanation:'Declares a member, local reference, or constant: '+line+'. Its role follows from the surrounding class or block.'};
 if(/\b(?:logger|log)\.(?:info|debug|warn|error|trace)\(/.test(line))return {kind:'Logging statement',explanation:'Writes a diagnostic log message at the specified level. It does not itself create a company: '+line};
 if(/(?<![=!<>])=(?!=)/.test(line))return {kind:'Assignment / configuration',explanation:'Assigns a value or updates configuration in this statement: '+line+'. The effect depends on the surrounding block.'};
 if(/(?:\.\w+\s*\(|^\w+\s*\()/i.test(line))return {kind:'Method call / expression',explanation:'Invokes or chains a method call as part of a larger statement: '+line+'. The destination is not assumed to be a mapped Shopizer company without verified call evidence.'};
 if(/;\s*$/.test(line))return {kind:'Java statement',explanation:'A complete Java statement: '+line+'. Understand it together with the surrounding method or declaration; it has no separate company number.'};
 return {kind:'Java source / continuation',explanation:'Part of the original Java source statement or declaration: '+line+'. It may continue from the preceding line or onto the next; inspect neighbors before assigning functionality.'};
}
function inspectUnnumberedLine(n){
 if(mode!=='file')return false;
 const f=files[selectedFile],body=$('.file-grid .code-body'),detail=$('#source-line-info');
 if(!f?.source||!body||!detail||!Number.isInteger(n)||n<1||n>f.source.length)return false;
 const line=body.querySelector('.code-row[data-line="'+n+'"]');
 if(!line||line.dataset.sourceCompany)return false;
 body.querySelectorAll('.code-row.source-inspected').forEach(e=>{e.classList.remove('source-inspected');e.setAttribute('aria-pressed','false')});
 line.classList.add('source-inspected');line.setAttribute('aria-pressed','true');
 const info=sourceLineFacts(f,n);
 detail.replaceChildren();
 const title=document.createElement('strong');title.className='source-info-title';title.textContent='Line '+n+' · '+info.kind;
 const desc=document.createElement('span');desc.className='source-info-explanation';desc.textContent=info.explanation;
 detail.append(title,desc);
 if(info.target){
   const button=document.createElement('button');button.type='button';button.dataset.gofile=info.target;
   button.className='source-info-open';button.textContent='Open imported Shopizer file ↗';detail.appendChild(button);
 }
 return true;
}

function renderPendingFileView(f){
  const url=githubSourceUrl(f),link='<a class="source-github-link" href="'+safe(url)+'" target="_blank" rel="noopener noreferrer">View pinned original on GitHub ↗</a>';
  const status=f.loadingState==='loading'?'Loading original file source…':
    f.loadingState==='unsupported'?'This file is binary or too large for a reliable text preview.':
    f.loadError?'Source preview unavailable: '+safe(f.loadError):'Preparing source preview…';
  return '<div class="hero"><div class="eyebrow">ORIGINAL REPOSITORY FILE · '+(f.name.endsWith('.java')?'JAVA':'SOURCE')+'</div><h1>'+safe(f.name)+'</h1><p class="description">'+safe(f.path)+'</p></div><section class="panel source-pending"><h2>'+status+'</h2><p>No company number has been assigned to this file. Original code is never invented.</p>'+link+'</section>';
}
