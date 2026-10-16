function renderNodeIcon(kind){
 if(kind==='folder'||kind==='package')return '<span class="ide-node-icon"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M2 5.5c0-.8.6-1.5 1.5-1.5H8l1.7 2h6.8c.9 0 1.5.7 1.5 1.5v8c0 .9-.6 1.5-1.5 1.5h-13c-.9 0-1.5-.6-1.5-1.5z" fill="#9aa3b0" opacity=".85"/><path d="M3 7.5H17" stroke="#dae0e7" stroke-width=".8"/></svg></span>';
 if(kind==='file')return '<span class="ide-node-icon"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M5 2.5h7.5l3.2 3.3v11.4H5z" stroke="#abb2c0" stroke-width="1.2" fill="#292e35"/><path d="M12.4 2.9v3h3" stroke="#abb2c0" fill="none"/><text x="7.1" y="14" font-size="8.5" font-weight="700" fill="#ed9c74">J</text></svg></span>';
 return '<span class="ide-method-symbol '+(kind==='branch'?'ide-subsidiary-symbol':'')+'" aria-hidden="true">m</span>';
}
function ideFolder(node,path){
 let current=node,label=node.name,full=path?path+'/'+node.name:node.name;
 const isPackage=full.includes('/src/main/java/');
 while(isPackage&&current.children?.length===1){
   const c=current.children[0];
   if(c.file||c.isResource||!Array.isArray(c.children))break;
   full+='/'+c.name;label+='.'+c.name;current=c;
 }
 return {current,label,full,isPackage};
}
function treeContent(){
 const rows=[],pad=d=>4+d*14;
 function addFolder(node,path,depth){
   const f=ideFolder(node,path),key='f:'+f.full,open=expanded.has(key);
   rows.push(`<button type="button" class="tree-row folder${f.isPackage?' ide-package':''}" data-folder="${safe(key)}" data-depth="${depth}" style="padding-left:${pad(depth)}px" aria-label="${safe(f.full)}" aria-level="${depth+1}" aria-expanded="${open}"><span class="tree-chevron">${icon(open?'down':'chevron')}</span>${renderNodeIcon(f.isPackage?'package':'folder')}<span class="tree-text">${safe(f.label)}</span>${depth===0?`<span class="mini-count">${Object.keys(files).length} files</span>`:''}</button>`);
   if(!open)return;
   for(const ch of f.current.children||[]){
     if(ch.file)addFile(ch.file,depth+1);
     else if(ch.isResource)rows.push(`<div class="tree-row file" style="padding-left:${pad(depth+1)}px"><span class="tree-chevron spacer"></span>${renderNodeIcon('file')}<span class="tree-text">${safe(ch.name)}</span></div>`);
     else addFolder(ch,f.full,depth+1);
   }
 }
 function addFile(fid,depth){
   const f=files[fid],key='file:'+fid,open=expanded.has(key),active=mode==='file'&&selectedFile===fid;
   rows.push(`<button type="button" class="tree-row file ${active?'is-active':''}" data-file="${fid}" data-depth="${depth}" aria-level="${depth+1}" style="padding-left:${pad(depth)}px" aria-label="${safe(f.path)}" aria-expanded="${open}"><span class="tree-chevron">${icon(open?'down':'chevron')}</span>${renderNodeIcon('file')}<span class="tree-text">${safe(f.name)}</span><span class="mini-count">${f.companyIds.length}</span></button>`);
   if(open)for(const id of f.companyIds)addEntity(id,depth+1);
 }
 function addEntity(id,depth){
   const c=entities[id],sub=!!c.parent,open=expanded.has('co:'+id),children=!!c.children?.length;
   rows.push(`<button type="button" class="tree-row comp ${sub?'sub':''} ${selected===id&&mode==='company'?'is-active':''}" data-company="${id}" ${selected===id&&mode==='company'?'aria-current="location"':''} data-depth="${depth}" aria-level="${depth+1}" style="padding-left:${pad(depth)}px" aria-label="Company ${safe(c.no)} — ${safe(c.name)}" ${children?`aria-expanded="${open}"`:''}><span class="tree-chevron ${children?'':'spacer'}">${children?icon(open?'down':'chevron'):''}</span><span class="company-key">${renderNodeIcon(sub?'branch':'company')}<span class="number">${safe(c.no)}</span></span><span class="tree-text">${safe(c.name)}</span></button>`);
   if(open)for(const child of c.children||[])addEntity(child,depth+1);
 }
 addFolder(folderData,'',0);return rows.join('');
}
function renderTree(){const side=$('#tree');side.innerHTML='<div class="tree-canvas">'+treeContent()+'</div>';}
/* The visible Project selection follows the company shown in the right pane.
   Scroll ONLY the sidebar's .side-body; never scroll the document or the source pane.
   Called after route/render/scroll restoration, not on ordinary user scrolling. */
function revealCurrentTreeRow(){
 if(mode!=='company'&&mode!=='file')return false;
 const sidebar=$('.side-body'),tree=$('#tree');
 if(!sidebar||!tree)return false;
 const selector=mode==='company'?'[data-company]':'[data-file]';
 const value=mode==='company'?selected:selectedFile;
 let row=[...tree.querySelectorAll('button.tree-row'+selector)].find(el=>
   (mode==='company'?el.dataset.company:el.dataset.file)===value);
 if(!row && mode==='company' && entities[selected]){
   openParents(selected);renderTree();
   row=[...tree.querySelectorAll('button.tree-row[data-company]')].find(el=>el.dataset.company===selected);
 }
 if(!row && mode==='file' && files[selectedFile]){
   openFileParents(selectedFile);renderTree();
   row=[...tree.querySelectorAll('button.tree-row[data-file]')].find(el=>el.dataset.file===selectedFile);
 }
 if(!row)return false;
 const viewport=sidebar.getBoundingClientRect(),item=row.getBoundingClientRect();
 const margin=Math.min(24,Math.max(4,viewport.height/8));
 if(item.top<viewport.top+margin||item.bottom>viewport.bottom-margin){
   // Center the selected row, accounting for existing Project header/caption.
   sidebar.scrollTop+=item.top-viewport.top-(viewport.height-item.height)/2;
 }
 return true;
}
function queueRevealCurrentTreeRow(){
 // Restore-scroll runs in a requestAnimationFrame; queue after it so it
 // cannot move the selected company back outside the sidebar viewport.
 requestAnimationFrame(revealCurrentTreeRow);
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
 });
}
function updateBackButton(){const b=$('#history-back');if(b)b.disabled=!navStack.length;}
function saveLocation(){
 const title=$('#detail-title'),note=$('#detail-note');
 return [mode,selectedFile,selected,folderPath,captureScroll(),activeLine,activeRelationKey,title?{head:title.textContent,description:note?.textContent||''}:null];
}
function closeSidebar(){ $('#sidebar').classList.remove('open');$('#backdrop').classList.remove('open');$('#menu').setAttribute('aria-expanded','false'); }
function openFileParents(fid){
 const f=files[fid];if(!f)return;
 let path='shopizer';expanded.add('f:'+path);
 for(const part of f.path.split('/').slice(0,-1)){path+='/'+part;expanded.add('f:'+path);}
 expanded.add('file:'+fid);
}
function openParents(id){
 const c=entities[id];if(!c)return;
 openFileParents(c.file);
 let parent=c.parent;while(parent){expanded.add('co:'+parent);parent=entities[parent].parent;}
}
function syncNavigationUrl(){const target=mode==='company'&&entities[selected]?'#company-'+encodeURIComponent(entities[selected].no):(location.pathname||'')+(location.search||'');history.replaceState(null,'',target);}
function navToFile(fid,track=true){if(!files[fid])return false;if(mode==='file'&&selectedFile===fid)return true;const before=captureScroll();if(track)navStack.push(saveLocation());resetSelection();selectedFile=fid;selected=null;mode='file';openFileParents(fid);syncNavigationUrl();renderAll();closeSidebar();restoreScroll({...before,x:0,y:0},false);queueRevealCurrentTreeRow();return true;}
function navToCompany(id,track=true){
  const c=entities[id];if(!c)return false;
  if(mode==='company'&&selected===id){resetSelection();openParents(id);renderAll();window.scrollTo({left:0,top:0,behavior:'instant'});queueRevealCurrentTreeRow();return true;}
  const before=captureScroll();if(track)navStack.push(saveLocation());
  selectedFile=c.file;selected=id;mode='company';resetSelection();
  openParents(id);$('#search').value='';$('#search-results').hidden=true;
  syncNavigationUrl();
  renderAll();closeSidebar();restoreScroll({...before,x:0,y:0},false);queueRevealCurrentTreeRow();
  return true;
}
function navBack(){
 if(!navStack.length)return false;
 const [m,f,s,p,where,line,relation,details]=navStack.pop();
 resetSelection();mode=m;selectedFile=f;selected=s;if(p)folderPath=p;
 if(mode==='company'&&entities[selected])openParents(selected);
 if(mode==='file'&&files[selectedFile])openFileParents(selectedFile);
 syncNavigationUrl();renderAll();closeSidebar();
 if(mode==='company'&&line!==null&&Number.isFinite(line))
   requestAnimationFrame(()=>selectLine(line,false,relation,details));
 restoreScroll(where,true);queueRevealCurrentTreeRow();updateBackButton();return true;
}
function navToFolder(path){if(!path)return false;if(mode==='folder'&&folderPath===path)return true;const before=captureScroll();navStack.push(saveLocation());resetSelection();expanded.add('f:'+path);mode='folder';selected=null;folderPath=path;syncNavigationUrl();renderAll();closeSidebar();restoreScroll({...before,x:0,y:0},false);return true;}
let folderPath='shopizer';
function collectFolder(node,full,match){if(full===match)return node;for(const ch of node.children||[]){if(ch.file||ch.isResource)continue;const res=collectFolder(ch,full+'/'+ch.name,match);if(res)return res;}return null;}
