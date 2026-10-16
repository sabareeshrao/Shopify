function renderNodeIcon(kind,opened){return icon(kind==='folder'?(opened?'folderOpen':'folder'):kind==='file'?'file':kind==='branch'?'branch':'building');}
function treeContent(){
 const rows=[];
 function addFolder(node,path,depth){const full=path?path+'/'+node.name:node.name,key='f:'+full,opened=expanded.has(key);const count=node.children?.length||0;
 rows.push(`<button class="tree-row folder" data-folder="${safe(key)}" style="padding-left:${8+Math.min(depth,5)*10}px" title="${safe(full)}" aria-expanded="${opened}"><span class="tree-chevron">${icon(opened?'down':'chevron')}</span>${renderNodeIcon('folder',opened)}<span class="tree-text">${safe(node.name)}</span>${depth===0?`<span class="mini-count">${Object.keys(files).length} files</span>`:''}</button>`);
 if(!opened)return;
 for(const child of node.children||[]){if(child.file)addFile(child.file,depth+1);else if(child.isResource)rows.push(`<div class="tree-row file" style="padding-left:${8+Math.min(depth+1,5)*10}px;opacity:.6"><span class="tree-chevron spacer"></span>${icon('file')}<span class="tree-text">${safe(child.name)}</span></div>`);else addFolder(child,full,depth+1);}
 }
 function addFile(fid,depth){const f=files[fid],key='file:'+fid,opened=expanded.has(key),act=selectedFile===fid;
 rows.push(`<button class="tree-row file ${act?'is-active':''}" data-file="${fid}" style="padding-left:${8+Math.min(depth,5)*10}px" title="${safe(f.path)}" aria-expanded="${opened}"><span class="tree-chevron">${icon(opened?'down':'chevron')}</span>${icon('file')}<span class="tree-text">${safe(f.name)}</span><span class="mini-count">${f.companyIds.length}</span></button>`);
 if(opened){for(const id of f.companyIds)addEntity(id,depth+1);}
 }
 function addEntity(id,depth){const c=entities[id],isSub=!!c.parent,opened=expanded.has('co:'+id),hasKids=!!c.children?.length;
 rows.push(`<button class="tree-row comp ${isSub?'sub':''} ${selected===id&&mode==='company'?'is-active':''}" data-company="${id}" style="padding-left:${8+Math.min(depth,5)*10}px" title="Company ${safe(c.no)} — ${safe(c.desc)}" ${hasKids?`aria-expanded="${opened}"`:''}><span class="tree-chevron ${hasKids?'':'spacer'}">${hasKids?icon(opened?'down':'chevron'):icon('chevron')}</span><span class="company-key">${renderNodeIcon(isSub?'branch':'company')}<span class="number">${safe(c.no)}</span></span><span class="tree-text">${safe(c.name)}</span></button>`);
 if(opened)for(const sub of c.children||[])addEntity(sub,depth+1);
 }
 addFolder(folderData,'',0);return rows.join('');
}
function renderTree(){const side=$('#tree');side.innerHTML=treeContent();}
function closeSidebar(){ $('#sidebar').classList.remove('open');$('#backdrop').classList.remove('open');$('#menu').setAttribute('aria-expanded','false'); }
function openParents(id){const c=entities[id],f=files[c.file];const parts=f.path.split('/');let p='shopizer';expanded.add('f:'+p);for(const part of parts.slice(0,-1)){p+='/'+part;expanded.add('f:'+p);}expanded.add('file:'+c.file);let parent=c.parent;while(parent){expanded.add('co:'+parent);parent=entities[parent].parent;}}
function syncNavigationUrl(){const target=mode==='company'&&entities[selected]?'#company-'+encodeURIComponent(entities[selected].no):(location.pathname||'')+(location.search||'');history.replaceState(null,'',target);}
function navToFile(fid,track=true){if(!files[fid])return;resetSelection();if(track)navStack.push([mode,selectedFile,selected,folderPath]);selectedFile=fid;selected=null;mode='file';expanded.add('file:'+fid);syncNavigationUrl();renderAll();closeSidebar();window.scrollTo({top:0,behavior:'auto'});}
function navToCompany(id,track=true){
  const c=entities[id];if(!c)return false;
  if(track&&(mode!=='company'||selected!==id))navStack.push([mode,selectedFile,selected,folderPath]);
  selectedFile=c.file;selected=id;mode='company';resetSelection();
  openParents(id);$('#search').value='';$('#search-results').hidden=true;
  syncNavigationUrl();
  renderAll();closeSidebar();window.scrollTo({top:0,behavior:'auto'});
  return true;
}
function navBack(){if(!navStack.length)return;resetSelection();const [m,f,s,p]=navStack.pop();mode=m;selectedFile=f;selected=s;if(p)folderPath=p;syncNavigationUrl();renderAll();closeSidebar();window.scrollTo({top:0,behavior:'auto'});}
function navToFolder(path){if(!path)return;resetSelection();if(mode!=='folder'||folderPath!==path)navStack.push([mode,selectedFile,selected,folderPath]);const key='f:'+path;expanded.add(key);mode='folder';selected=null;folderPath=path;syncNavigationUrl();renderAll();closeSidebar();window.scrollTo({top:0,behavior:'auto'});}
let folderPath='shopizer';
function collectFolder(node,full,match){if(full===match)return node;for(const ch of node.children||[]){if(ch.file||ch.isResource)continue;const res=collectFolder(ch,full+'/'+ch.name,match);if(res)return res;}return null;}
