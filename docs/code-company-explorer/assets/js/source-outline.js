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


/* YouTube-mentor source explanations: grounded in real symbols, usage and neighbors. */
const MENTOR_SYMBOL_PURPOSE={
 ArrayList:'the growable Java list used for collecting items',Collection:'the generic group-of-values interface',List:'the ordered Java collection interface',Arrays:'helpers for working with Java arrays',Locale:'language and regional settings',CollectionUtils:'Apache Commons collection helpers',
 Logger:'the interface used for diagnostic logs',LoggerFactory:'the factory that supplies class loggers',Log:'the Apache Commons logging interface',LogFactory:'the Apache Commons logger factory',
 DataAccessException:'the Spring data-access failure abstraction',GrantedAuthority:'a Spring Security permission or role contract',SimpleGrantedAuthority:'a concrete authority containing a permission or role name',
 UserDetails:'the Spring Security representation of account details',UserDetailsService:'the contract for loading a user by username',UsernameNotFoundException:'the exception signalling an absent username',
 BadCredentialsException:'an authentication error for rejected credentials',Authentication:'a Spring Security authentication result or request object',AuthenticationException:'the base kind of authentication error',
 UsernamePasswordAuthenticationToken:'the username/password authentication token type',DaoAuthenticationProvider:'a Spring Security username/password authentication provider',PasswordEncoder:'the password hashing and verification contract',
 Inject:'a standard dependency-injection annotation',Autowired:'Spring dependency wiring metadata',Bean:'the Spring bean registration annotation',
 ApplicationReadyEvent:'the Spring Boot application-ready event',FilterRegistrationBean:'a servlet filter registration with chosen URL patterns',XssFilter:'Shopizer’s custom XSS-related filter (whose implementation needs separate review)',
 CorsFilter:'a Shopizer CORS-related component (inspect its actual interface before judging it)',MappingJackson2HttpMessageConverter:'Spring MVC’s JSON converter backed by Jackson',
 ByteArrayHttpMessageConverter:'Spring’s HTTP byte-array converter',HttpMessageConverter:'the Spring MVC HTTP-body conversion contract',ViewControllerRegistry:'the registry binding URLs to simple views',InterceptorRegistry:'the MVC interceptor registration point',
 LocaleChangeInterceptor:'the interceptor that reacts to locale-change parameters',SessionLocaleResolver:'a session-backed resolver for the visitor’s language',
 CustomerService:'a service for customer records',GroupService:'a service for user groups',PermissionService:'a service for permissions',Customer:'a shop customer domain entity',Group:'a model representing a group',Permission:'a model representing permission',
 IOException:'an input/output failure',ServiceException:'a service-layer error whose specific meaning needs its declaration',Constants:'common constants shared inside Shopizer'
};
const MENTOR_ANNOTATION_PURPOSE={
 Autowired:'asks Spring to supply the dependency attached to the following declaration',Inject:'requests injection of the neighboring collaborator',
 Override:'asks the Java compiler to verify an inherited method contract',Bean:'registers the following factory method’s result in Spring',
 Configuration:'marks a configuration class',ComponentScan:'chooses packages for scanning Spring components',
 EventListener:'connects a method to a Spring application event',JsonIgnore:'tells Jackson to ignore the annotated property where applicable',
 EnableWebSecurity:'enables Spring Security’s web configuration',Transactional:'configures transaction handling in a framework-managed call',
 GetMapping:'maps an HTTP GET handler',PostMapping:'maps an HTTP POST handler',RequestMapping:'configures an HTTP route',
 Import:'includes another configuration class',Value:'injects a configured value',SuppressWarnings:'suppresses selected compiler warnings'
};
function mentorContextFor(f,n){
 if(!f._mentorContext){
  let scope=f.name.replace(/\.java$/,''),method='',arr=[];
  for(let i=0;i<f.source.length;i++){
   const line=String(f.source[i]).trim();
   const cls=line.match(/\b(?:class|interface|enum|record)\s+([A-Za-z_$][\w$]*)/);
   if(cls)scope=cls[1];
   const signature=line.match(/^(?:(?:public|private|protected|static|final|abstract|synchronized)\s+)+[\w<>, ?\[\].]*\s([A-Za-z_$][\w$]*)\s*\(/);
   if(signature)method=signature[1]+'()';
   arr.push({scope,method});
  }
  for(let i=0;i<arr.length;i++){
   for(let j=i-1;j>=0;j--){const x=String(f.source[j]).trim();if(x&&!/^(?:\*|\/\*|\*\/)$/.test(x)){arr[i].before=x;break}}
   for(let j=i+1;j<f.source.length;j++){const x=String(f.source[j]).trim();if(x&&!/^(?:\*|\/\*|\*\/)$/.test(x)){arr[i].after=x;break}}
  }
  f._mentorContext=arr;
 }
 return f._mentorContext[n-1]||{};
}
function mentorShort(x){const s=String(x||'').trim().replace(/\s+/g,' ');return s.length>115?s.slice(0,112)+'…':s||'(no nearby statement)'}
function mentorUsage(f,name,exclude){
 if(!/^[A-Za-z_$][\w$]*$/.test(name))return null;
 const re=new RegExp('\\b'+name+'\\b');
 for(let k=0;k<f.source.length;k++){
  const s=String(f.source[k]);if(k!==exclude-1&&!/^\s*import\b/.test(s)&&!s.trim().startsWith('//')&&re.test(s))return mentorShort(s);
 }
 return null;
}
const oldLineFacts=sourceLineFacts;
sourceLineFacts=function(f,n){
 const old=oldLineFacts(f,n),line=String(f.source?.[n-1]||'').trim();
 if(!line)return old;
 const cx=mentorContextFor(f,n),after=mentorShort(cx.after),before=mentorShort(cx.before),scope=cx.scope||f.name;
 const output=explanation=>({...old,explanation});
 const quoted=x=>'“'+mentorShort(x)+'”';
 const pack=line.match(/^package\s+([\w.]+)\s*;/);
 if(pack)return output('Before any Shopizer method runs, Java needs the class address. '+quoted(pack[1])+' puts this source under the '+pack[1].split('.').at(-1)+' package. Think of a labeled aisle in the project: this line organizes code; it does not perform a request.');
 const importMatch=line.match(/^import\s+(static\s+)?([\w.*]+)\s*;/);
 if(importMatch){
  const name=importMatch[2].split('.').at(-1),meaning=MENTOR_SYMBOL_PURPOSE[name],use=mentorUsage(f,name,n);
  return output('Look at '+name+' here. '+(meaning?'It means '+meaning+'.':'It names a '+(importMatch[1]?'static member':'type')+' from '+importMatch[2]+'.')+
   (importMatch[1]?' This static import lets the code mention it without its parent class.':' Importing makes its short name available in this file.')+
   (use?' Now find its actual use: '+quoted(use)+'.':' The name is not visibly used outside the import in this source snapshot.')+
   ' Merely importing '+name+' does not mean any request has invoked its behavior.');
 }
 const annotation=line.match(/^@([\w.]+)/);
 if(annotation){
  const name=annotation[1].split('.').at(-1),meaning=MENTOR_ANNOTATION_PURPOSE[name]||'adds metadata for the compiler or an associated framework';
  return output('Notice @'+name+' sitting just above '+quoted(after)+'. It '+meaning+'. This is our clue about how '+scope+' is configured; the annotation is metadata, not a direct call to the code beneath it.');
 }
 const type=line.match(/\b(class|interface|record|enum)\s+([A-Za-z_$][\w$]*)/);
 if(type){
  const parent=line.match(/\bextends\s+([\w.$]+)/),contracts=line.match(/\bimplements\s+([\w.,\s]+)/);
  return output('Meet '+type[2]+', the '+type[1]+' declared in this file. '+(parent?'It inherits from '+parent[1]+', which is why the parent contract matters.':contracts?'It promises the '+contracts[1].trim()+' interface contract.':'Its members will define what this type can do.')+' We are reading its blueprint, not invoking a method.');
 }
 const doc=/^(?:\/\*|\/\/|\*|\*\/)/.test(line);
 if(doc){
  const words=line.replace(/^\/\*+|^\/\/|^\*+|\*\/$/g,'').trim();
  if(words)return output('The developer wrote '+quoted(words)+' near '+scope+'. What does it suggest about the next source, '+quoted(after)+'? Treat this as a helpful author note, but always check the executable Java before trusting it.');
  return output('This documentation marker sits between '+quoted(before)+' and '+quoted(after)+'. It separates or closes source commentary; Java never executes the marker itself. Read the neighboring words to identify what is being documented.');
 }
 const field=line.match(/^(?:public|protected|private)\s+(?:(?:static|final|volatile|transient)\s+)*([\w<>?,.\[\]]+)\s+([A-Za-z_$][\w$]*)\s*(?:[=;])/);
 if(field)return output('Here '+scope+' declares '+field[2]+', a field of type '+field[1]+'. '+(MENTOR_SYMBOL_PURPOSE[field[1]]?'That type is '+MENTOR_SYMBOL_PURPOSE[field[1]]+'. ':'')+'Think of fields as the data or collaborators a class keeps around. The declaration itself is not a separate company.');
 if(old.kind==='Unnumbered Java method')return output('Here’s the doorway to a method or constructor: '+quoted(line)+'. It sits in '+scope+'. Before assigning this code a company number, we would read its complete body, beginning near '+quoted(after)+', and verify real callers.');
 if(/^\}\s*[,;]?$/.test(line))return output('That closing brace ends the block after '+quoted(before)+'. The following source is '+quoted(after)+'. We are closing a Java scope, not launching a new operation. Check the enclosing method to know what finished.');
 if(line==='{')return output('The opening brace starts a block just after '+quoted(before)+'. Its first nearby statement is '+quoted(after)+'. Think of braces as the fence around the work; the statements inside decide the behavior.');
 if(/^return\b/.test(line))return output('The method now hands '+quoted(line.replace(/^return\s*/,'').replace(/;$/,''))+' back to its caller. Notice that this follows '+quoted(before)+'. A return value becomes useful only when we see what the caller does with it.');
 if(/^(?:if|else\s+if)\s*\(/.test(line))return output('Stop at this decision: '+quoted(line)+'. If its condition passes, the following branch near '+quoted(after)+' is reachable. Trace both sides before concluding which customers or requests are affected.');
 if(/^else\b/.test(line))return output('This is the alternate branch after '+quoted(before)+'. It leads toward '+quoted(after)+'. It can run only when the earlier condition selects that path; the keyword alone does not tell us which case reaches it.');
 if(/^(?:for|while|do)\b/.test(line))return output('A loop begins with '+quoted(line)+'. What changes every pass, and what stops it? Watch the next statement '+quoted(after)+' to see the repeated work; loops can hide expensive shop operations.');
 if(/^try\b/.test(line))return output('The developer is about to attempt work that could fail. The first nearby statement is '+quoted(after)+'. A try block is not an error itself; search for its matching catch or finally to see how failure is handled.');
 if(/^catch\b/.test(line))return output('This branch catches '+quoted(line)+'. The response starts near '+quoted(after)+'. That might report, recover, or rethrow an error—we have to read the actual body rather than guessing.');
 if(/^finally\b/.test(line))return output('This finally block is where cleanup can happen after the try/catch flow. Its first source statement is '+quoted(after)+'. The block body tells us which resource or state is actually cleaned up.');
 if(/^throw\b/.test(line))return output('This line raises an exception: '+quoted(line)+'. It follows '+quoted(before)+'. Java transfers control to a matching handler or framework error path instead of returning normally.');
 if(/\b(?:LOGGER|logger|log)\.(?:info|debug|warn|error|trace)\s*\(/.test(line))return output('This records a diagnostic message: '+quoted(line)+'. It helps explain what happened inside '+scope+', but writing a log is not the business action itself. Check whether sensitive values might be exposed.');
 const assign=line.match(/^(?:this\.)?([A-Za-z_$][\w$]*(?:\.[\w$]+)*)\s*=(?!=)\s*(.+)$/);
 if(assign)return output('Notice '+assign[1]+'. Here the code stores the result of '+quoted(assign[2].replace(/;$/,''))+'. The next statement is '+quoted(after)+', which may consume that stored value. Think about the actual data flow, not just the equals sign.');
 const call=line.match(/([A-Za-z_$][\w$]*(?:\.[\w$]+)*)\s*\(/);
 if(call)return output('This expression mentions a call to '+call[1]+'(): '+quoted(line)+'. Inside '+scope+' it is part of a larger action. We should follow the real callee before claiming it belongs to any numbered Shopizer company.');
 return output('Let’s read this exact piece of '+scope+': '+quoted(line)+'. It comes after '+quoted(before)+' and before '+quoted(after)+'. Look at the surrounding block to decide whether it is a declaration, expression or continuation; one isolated line cannot tell the whole story.');
};


/* Teach repeated syntax by its ACTUAL use: owner method, next declaration,
   neighboring operation, and where an identical source statement also occurs. */
function mentorFollowingMember(f,n){
 for(let i=n;i<Math.min(f.source.length,n+10);i++){
  const t=String(f.source[i]).trim();
  if(!t||t.startsWith('@')||t.startsWith('*')||t.startsWith('//'))continue;
  const m=t.match(/\b([A-Za-z_$][\w$]*)\s*\(/);
  if(m)return m[1]+'()';
  const field=t.match(/\b([A-Za-z_$][\w$]*)\s*(?:[;=])/);
  if(field)return field[1]+' field';
  return mentorShort(t);
 }
 return 'the following declaration';
}
const groundedMentorFacts=sourceLineFacts;
sourceLineFacts=function(f,n){
 const r=groundedMentorFacts(f,n),line=String(f.source?.[n-1]||'').trim();
 if(!line)return r;
 const ctx=mentorContextFor(f,n);
 let explanation=r.explanation;
 if(/^@/.test(line)){
  const member=mentorFollowingMember(f,n);
  explanation+=' For this particular occurrence, the nearby target is '+member+'.';
 }
 if(/^\}\s*[,;]?$/.test(line))
  explanation+=' You are still tracing '+(ctx.method||ctx.scope)+' in '+f.name+'.';
 if(/^return\b/.test(line))explanation+=' This return belongs near '+(ctx.method||ctx.scope)+' of '+f.name+'.';
 if(/(?:\.\w+\s*\(|^\w+\s*\()/.test(line)&&!/^@/.test(line))
  explanation+=' To follow this call in context, compare the next source statement '+JSON.stringify(mentorShort(ctx.after))+'.';
 if(/^package\b/.test(line))explanation+=' The specific file at this address is '+f.name+'.';
 if(/^import\b/.test(line))explanation+=' We are using this import specifically inside '+f.name+'; compare its references with those of other Java classes.';
 if(/^(?:if|else|try|catch|finally)\b/.test(line))
  explanation+=' This control-flow boundary belongs to '+(ctx.method||ctx.scope)+' in '+f.name+'; its exact branch is specific to that file.';
 if(/^(?:this\.)?[A-Za-z_$][\w$]*(?:\.[\w$]+)*\s*=(?!=)/.test(line))
  explanation+=' In '+f.name+' this assignment supports '+(ctx.method||ctx.scope)+', so check which identity or customer object owns the value.';
 // A source file can literally repeat the same Java statement in several branches.
 // Explain where the repetitions occur instead of pretending one generic note
 // describes different occurrences.
 if(!f._mentorRepeated){
  const byCode=new Map();
  for(let i=0;i<f.source.length;i++){
   const code=String(f.source[i]).trim();
   if(!code)continue;
   const list=byCode.get(code)||[];list.push(i+1);byCode.set(code,list);
  }
  f._mentorRepeated=byCode;
 }
 const occurrences=f._mentorRepeated.get(line)||[];
 if(occurrences.length>1){
  const ordinal=occurrences.indexOf(n)+1,other=occurrences.find(x=>x!==n),before=mentorShort(ctx.before),after=mentorShort(ctx.after);
  explanation+=' You will encounter the same written source statement '+occurrences.length+' times in '+f.name+'. This is occurrence '+ordinal+
   ': it follows '+JSON.stringify(before)+' and leads to '+JSON.stringify(after)+'. Compare it with the matching occurrence at line '+other+' to see why repeated code may serve different branches or steps.';
 }
 return {...r,explanation};
};


/* Strict per-file uniqueness guard. Only used if distinct source positions
   unexpectedly produce the same explanatory prose. The added text compares
   the actual nearby statements and other occurrence, not a fake company ID. */
const mentorFactBeforeDedup=sourceLineFacts;
sourceLineFacts=function(f,n){
 if(!f._mentorDistinctFacts){
  const facts=new Map(),groups=new Map();
  for(let i=1;i<=f.source.length;i++){
   if(!String(f.source[i-1]).trim())continue;
   const result=mentorFactBeforeDedup(f,i);facts.set(i,result);
   const key=result.explanation,list=groups.get(key)||[];list.push(i);groups.set(key,list);
  }
  for(const positions of groups.values()){
   if(positions.length<2)continue;
   positions.forEach((line,i)=>{
    const fact=facts.get(line),cx=mentorContextFor(f,line),other=positions.find(k=>k!==line);
    const comparison=' In this file, the same explanation would otherwise apply to '+positions.length+' positions. This occurrence is beside '+mentorShort(cx.before)+' and '+mentorShort(cx.after)+'. Compare the corresponding code near line '+other+': the source repeats a pattern, but its placement can matter. This is the '+(i+1)+' of those occurrences.';
    facts.set(line,{...fact,explanation:fact.explanation+comparison});
   });
  }
  f._mentorDistinctFacts=facts;
 }
 return f._mentorDistinctFacts.get(n)||mentorFactBeforeDedup(f,n);
};
