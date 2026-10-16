/* Compact IDE toolwindow. Actions never alter company or code data. */
(function(){
 'use strict';
 const tree=document.getElementById('tree'),side=document.querySelector('.side-body');
 const locate=document.getElementById('project-locate'),collapse=document.getElementById('project-collapse'),expand=document.getElementById('project-expand'),reset=document.getElementById('project-reset-width');
 if(!tree||!locate||!collapse||!expand||!reset)return;
 locate.addEventListener('click',()=>{
   if(!entities[selected])return;
   openParents(selected);renderTree();
   const row=[...tree.querySelectorAll('[data-company]')].find(x=>x.dataset.company===selected);
   if(!row)return;
   const bounds=side.getBoundingClientRect(),item=row.getBoundingClientRect();
   if(item.top<bounds.top+8)side.scrollTop+=item.top-bounds.top-8;
   else if(item.bottom>bounds.bottom-8)side.scrollTop+=item.bottom-bounds.bottom+8;
   row.focus({preventScroll:true});
 });
 collapse.addEventListener('click',()=>{expanded.clear();expanded.add('f:shopizer');renderTree()});
 expand.addEventListener('click',()=>{
   expanded.add('f:shopizer');
   for(const [id,f] of Object.entries(files)){
     let path='shopizer';
     for(const part of f.path.split('/').slice(0,-1)){path+='/'+part;expanded.add('f:'+path)}
     expanded.add('file:'+id);
   }
   for(const id of Object.keys(entities))expanded.add('co:'+id);
   renderTree();
 });
 reset.addEventListener('click',()=>document.getElementById('sidebar-resizer')?.dispatchEvent(new MouseEvent('dblclick',{bubbles:true})));
 tree.addEventListener('keydown',e=>{
   if(e.ctrlKey||e.altKey||e.metaKey)return;
   const row=e.target.closest('button.tree-row');
   if(!row||!['ArrowUp','ArrowDown','ArrowLeft','ArrowRight','Home','End'].includes(e.key))return;
   e.preventDefault();e.stopPropagation();
   const items=[...tree.querySelectorAll('button.tree-row')],i=items.indexOf(row);
   if(e.key==='ArrowUp'||e.key==='ArrowDown'||e.key==='Home'||e.key==='End'){
     const j=e.key==='Home'?0:e.key==='End'?items.length-1:Math.min(items.length-1,Math.max(0,i+(e.key==='ArrowDown'?1:-1)));
     items[j]?.focus();return;
   }
   const toggle=row.querySelector('.tree-chevron'),open=row.getAttribute('aria-expanded')==='true',can=row.hasAttribute('aria-expanded');
   if(e.key==='ArrowRight'){
     if(can&&!open)toggle?.click();
     else if(can&&open)items[i+1]?.focus();
   }else{
     if(can&&open)toggle?.click();
     else{
       const depth=Number(row.dataset.depth||0);
       for(let k=i-1;k>=0;k--)if(Number(items[k].dataset.depth)<depth){items[k].focus();break}
     }
   }
 });
})();