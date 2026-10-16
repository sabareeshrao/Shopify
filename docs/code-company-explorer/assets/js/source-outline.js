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
function sourceOutlinePanel(f){
  if(!f.name.endsWith('.java'))return '<div class="source-outline-note">Complete text is shown with its original line numbers. This file is not a Java class, so no Java structure is inferred.</div>';
  const groups=buildJavaOutline(f),labels=[['package','Package / address'],['imports','Imports / dependencies'],['types','Types / inheritance'],['annotations','Annotations / framework metadata'],['fields','Fields / injected dependencies'],['methods','Methods / constructors'],['initializers','Initializer blocks'],['comments','JavaDoc / comments']];
  const counts=labels.map(pair=>'<span class="source-count">'+safe(pair[1])+': <b>'+groups[pair[0]].length+'</b></span>').join('');
  let out='<div class="source-counts">'+counts+'</div><p class="source-outline-note">Every original line stays visible in the source pane. These entries explain structure; only verified functional units receive company numbers. Source outline uses lightweight syntax detection, not a full Java compiler parser.</p>';
  for(const [id,label] of labels){
    const entries=groups[id];
    const list=entries.length?entries.map(item=>{
      const action=item.target?'<button type="button" class="source-open-file" data-gofile="'+safe(item.target)+'" aria-label="Open imported Shopizer file">Open source ↗</button>':'';
      const mapped=item.company?'<span class="source-mapped">Mapped company</span>':'';
      return '<div class="source-outline-entry"><button type="button" class="source-line-link" data-outline-line="'+item.line+'" data-outline-desc="'+safe(item.description)+'"><span class="source-line-number">L'+item.line+'</span><span class="source-label">'+safe(item.label)+'</span></button>'+mapped+action+'</div>';
    }).join(''):'<div class="source-none">No entries found in this category.</div>';
    out+='<details class="source-outline-group"'+(['package','types','methods','fields'].includes(id)?' open':'')+'><summary>'+safe(label)+' <span>'+entries.length+'</span></summary><div class="source-outline-items">'+list+'</div></details>';
  }
  out+='<div id="source-detail" class="source-detail" role="status">Select a structure entry to locate its exact original source line.</div>';
  return out;
}
function showSourceLine(button){
  if(mode!=='file'||!files[selectedFile]?.source)return;
  const n=Number(button.dataset.outlineLine),container=$('.file-grid .code-body');
  if(!container||!Number.isInteger(n))return;
  container.querySelectorAll('.code-row.outline-active').forEach(el=>el.classList.remove('outline-active'));
  const target=container.querySelector('.code-row[data-line="'+n+'"]');
  if(!target)return;
  target.classList.add('outline-active');
  const note=$('#source-detail');
  if(note)note.textContent='Line '+n+' — '+(button.dataset.outlineDesc||'Original source code');
  const outer=container.getBoundingClientRect(),inner=target.getBoundingClientRect();
  if(inner.top<outer.top+8)container.scrollTop+=inner.top-outer.top-8;
  if(inner.bottom>outer.bottom-8)container.scrollTop+=inner.bottom-outer.bottom+8;
}
function renderPendingFileView(f){
  const url=githubSourceUrl(f),link='<a class="source-github-link" href="'+safe(url)+'" target="_blank" rel="noopener noreferrer">View pinned original on GitHub ↗</a>';
  const status=f.loadingState==='loading'?'Loading original file source…':
    f.loadingState==='unsupported'?'This file is binary or too large for a reliable text preview.':
    f.loadError?'Source preview unavailable: '+safe(f.loadError):'Preparing source preview…';
  return '<div class="hero"><div class="eyebrow">ORIGINAL REPOSITORY FILE · '+(f.name.endsWith('.java')?'JAVA':'SOURCE')+'</div><h1>'+safe(f.name)+'</h1><p class="description">'+safe(f.path)+'</p></div><section class="panel source-pending"><h2>'+status+'</h2><p>No company number has been assigned to this file. Original code is never invented.</p>'+link+'</section>';
}
