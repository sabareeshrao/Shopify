function renderNodeIcon(kind,opened){return icon(kind==='folder'?(opened?'folderOpen':'folder'):kind==='file'?'file':kind==='branch'?'branch':'building');}
function treeContent(){
 const rows=[];
 function addFolder(node,path,depth){const full=path?path+'/'+node.name:node.name,key='f:'+full,opened=expanded.has(key);const count=node.children?.length||0;
 rows.push(`<button class="tree-row folder" data-folder="${safe(key)}" style="padding-left:${8+depth*20}px" title="${safe(full)}" aria-expanded="${opened}"><span class="tree-chevron">${icon(opened?'down':'chevron')}</span>${renderNodeIcon('folder',opened)}<span class="tree-text">${safe(node.name)}</span>${depth===0?`<span class="mini-count">${Object.keys(files).length} files</span>`:''}</button>`);
 if(!opened)return;
 for(const child of node.children||[]){if(child.file)addFile(child.file,depth+1);else if(child.isResource)rows.push(`<div class="tree-row file" style="padding-left:${8+Math.min(depth+1,5)*10}px;opacity:.6"><span class="tree-chevron spacer"></span>${icon('file')}<span class="tree-text">${safe(child.name)}</span></div>`);else addFolder(child,full,depth+1);}
 }
 function addFile(fid,depth){const f=files[fid],key='file:'+fid,opened=expanded.has(key),act=selectedFile===fid;
 rows.push(`<button class="tree-row file ${act?'is-active':''}" data-file="${fid}" style="padding-left:${8+depth*20}px" title="${safe(f.path)}" aria-expanded="${opened}"><span class="tree-chevron">${icon(opened?'down':'chevron')}</span>${icon('file')}<span class="tree-text">${safe(f.name)}</span><span class="mini-count">${f.companyIds.length}</span></button>`);
 if(opened){for(const id of f.companyIds)addEntity(id,depth+1);}
 }
 function addEntity(id,depth){const c=entities[id],isSub=!!c.parent,opened=expanded.has('co:'+id),hasKids=!!c.children?.length;
 rows.push(`<button class="tree-row comp ${isSub?'sub':''} ${selected===id&&mode==='company'?'is-active':''}" data-company="${id}" style="padding-left:${8+depth*20}px" title="Company ${safe(c.no)} — ${safe(c.desc)}" ${hasKids?`aria-expanded="${opened}"`:''}><span class="tree-chevron ${hasKids?'':'spacer'}">${hasKids?icon(opened?'down':'chevron'):icon('chevron')}</span><span class="company-key">${renderNodeIcon(isSub?'branch':'company')}<span class="number">${safe(c.no)}</span></span><span class="tree-text">${safe(c.name)}</span></button>`);
 if(opened)for(const sub of c.children||[])addEntity(sub,depth+1);
 }
 addFolder(folderData,'',0);return rows.join('');
}
function renderTree(){const side=$('#tree'),before=side.scrollLeft;side.innerHTML='<div class="tree-canvas">'+treeContent()+'</div>';side.scrollLeft=before;updateTreePan();}
function updateTreePan(){
 const tree=$('#tree'),prev=$('#tree-pan-left'),next=$('#tree-pan-right'),label=$('#tree-pan-label');
 if(!tree)return;const max=Math.max(0,tree.scrollWidth-tree.clientWidth);
 if(prev)prev.disabled=tree.scrollLeft<=1;
 if(next)next.disabled=tree.scrollLeft>=max-1;
 if(label)label.textContent=max>0?'Folder tree · scroll sideways':'Folder tree · all visible';
}
function captureScroll(){
 const tree=$('#tree'),side=$('.side-body'),code=$('#current-code')||$('.file-grid .code-body');
 return {x:window.scrollX||0,y:window.scrollY||0,treeX:tree?.scrollLeft||0,sideY:side?.scrollTop||0,codeX:code?.scrollLeft||0,codeY:code?.scrollTop||0};
}
function restoreScroll(value,includeCode=false){
 if(!value)return;
 requestAnimationFrame(()=>{
   const tree=$('#tree'),side=$('.side-body'),code=$('#current-code')||$('.file-grid .code-body');
   if(tree)tree.scrollLeft=value.treeX||0;if(side)side.scrollTop=value.sideY||0;
   if(includeCode&&code){code.scrollLeft=value.codeX||0;code.scrollTop=value.codeY||0;}
   if(typeof window.scrollTo==='function')window.scrollTo({left:value.x||0,top:value.y||0,behavior:'instant'});
   updateTreePan();
 });
}
function updateBackButton(){const b=$('#history-back');if(b)b.disabled=!navStack.length;}
function saveLocation(){
 const title=$('#detail-title'),note=$('#detail-note');
 return [mode,selectedFile,selected,folderPath,captureScroll(),activeLine,activeRelationKey,title?{head:title.textContent,description:note?.textContent||''}:null];
}
function closeSidebar(){ $('#sidebar').classList.remove('open');$('#backdrop').classList.remove('open');$('#menu').setAttribute('aria-expanded','false'); }
function openParents(id){const c=entities[id],f=files[c.file];const parts=f.path.split('/');let p='shopizer';expanded.add('f:'+p);for(const part of parts.slice(0,-1)){p+='/'+part;expanded.add('f:'+p);}expanded.add('file:'+c.file);let parent=c.parent;while(parent){expanded.add('co:'+parent);parent=entities[parent].parent;}}
function syncNavigationUrl(){const target=mode==='company'&&entities[selected]?'#company-'+encodeURIComponent(entities[selected].no):(location.pathname||'')+(location.search||'');history.replaceState(null,'',target);}
function navToFile(fid,track=true){if(!files[fid])return false;if(mode==='file'&&selectedFile===fid)return true;const before=captureScroll();if(track)navStack.push(saveLocation());resetSelection();selectedFile=fid;selected=null;mode='file';expanded.add('file:'+fid);syncNavigationUrl();renderAll();closeSidebar();restoreScroll(before);return true;}
function navToCompany(id,track=true){
  const c=entities[id];if(!c)return false;
  if(mode==='company'&&selected===id){resetSelection();renderAll();return true;}
  const before=captureScroll();if(track)navStack.push(saveLocation());
  selectedFile=c.file;selected=id;mode='company';resetSelection();
  openParents(id);$('#search').value='';$('#search-results').hidden=true;
  syncNavigationUrl();
  renderAll();closeSidebar();restoreScroll(before);
  return true;
}
function navBack(){
 if(!navStack.length)return false;
 const [m,f,s,p,where,line,relation,details]=navStack.pop();
 resetSelection();mode=m;selectedFile=f;selected=s;if(p)folderPath=p;
 if(mode==='company'&&entities[selected])openParents(selected);
 syncNavigationUrl();renderAll();closeSidebar();
 if(mode==='company'&&line!==null&&Number.isFinite(line))
   requestAnimationFrame(()=>selectLine(line,false,relation,details));
 restoreScroll(where,true);updateBackButton();return true;
}
function navToFolder(path){if(!path)return false;if(mode==='folder'&&folderPath===path)return true;const before=captureScroll();navStack.push(saveLocation());resetSelection();expanded.add('f:'+path);mode='folder';selected=null;folderPath=path;syncNavigationUrl();renderAll();closeSidebar();restoreScroll(before);return true;}
let folderPath='shopizer';
function collectFolder(node,full,match){if(full===match)return node;for(const ch of node.children||[]){if(ch.file||ch.isResource)continue;const res=collectFolder(ch,full+'/'+ch.name,match);if(res)return res;}return null;}
