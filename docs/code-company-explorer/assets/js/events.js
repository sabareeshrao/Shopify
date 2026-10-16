document.addEventListener('click',e=>{
 const external=e.target.closest('.relation-card[data-external]');
 if(external){selectExternalCard(external);return;}
 const folder=e.target.closest('[data-folder]');if(folder){const key=folder.dataset.folder;if(expanded.has(key))expanded.delete(key);else expanded.add(key);renderTree();return;}const file=e.target.closest('[data-file]');if(file){const id=file.dataset.file,key='file:'+id;if(e.target.closest('.tree-chevron')){if(expanded.has(key))expanded.delete(key);else expanded.add(key);renderTree();}else{expanded.add(key);navToFile(id);}return;}const comp=e.target.closest('[data-company]');if(comp){const id=comp.dataset.company;if(comp.classList.contains('tree-row')&&e.target.closest('.tree-chevron')&&entities[id]?.children?.length){const key='co:'+id;if(expanded.has(key))expanded.delete(key);else expanded.add(key);renderTree();return;}const wantLine=comp.dataset.highlight;if(!entities[id])return;navToCompany(id);if(wantLine){
 const c=entities[id],l=Number(wantLine);
 if(Number.isFinite(l)){
   if(l>=c.start&&l<=c.end)selectLine(l);
   else selectLine(c.methodStart||c.start,false,null,{
     head:'Linked source call · line '+l,
     description:'The related callsite is outside this method. You are viewing '+c.name+' in '+files[c.file].name+'.'
   });
 }
 }$('#search-results').hidden=true;return;}const go=e.target.closest('[data-gofile]');if(go){navToFile(go.dataset.gofile);return;}const fo=e.target.closest('[data-openfolder]');if(fo){navToFolder(fo.dataset.openfolder);return;}const line=e.target.closest('#maincontent .code-row[data-line]');if(line){selectLine(Number(line.dataset.line),true,null);return;}if(!e.target.closest('.searchwrap'))$('#search-results').hidden=true;});
$('#search-results').addEventListener('click',e=>{
  const button=e.target.closest('button[data-company],button[data-gofile]');
  if(!button)return;
  e.preventDefault();e.stopPropagation();
  if(button.dataset.company)navToCompany(button.dataset.company);
  else if(button.dataset.gofile)navToFile(button.dataset.gofile);
});
$('#search').addEventListener('input',e=>searchResults(e.target.value));
$('#search').addEventListener('keydown',e=>{
  if(e.key==='Enter'){
    e.preventDefault();
    const typed=e.currentTarget.value;
    const exact=companyByNumber(typed);
    if(exact){navToCompany(exact);e.currentTarget.blur();}
    else if(companyNumberQuery(typed)!==null){searchResults(typed);}
    else {const first=$('#search-results button');if(first){first.click();e.currentTarget.blur();}}
  }else if(e.key==='Escape'){$('#search-results').hidden=true;}
});
$('#prev-company').addEventListener('click',()=>moveCompany(-1));
$('#next-company').addEventListener('click',()=>moveCompany(1));
$('#copy').addEventListener('click',e=>copyText(getLocation(),e.currentTarget));
$('#maincontent').addEventListener('click',e=>{const btn=e.target.closest('#copy-method');if(btn){const c=getCode(selected);copyText(c.lines.join('\n'),btn);}const interview=e.target.closest('#copy-interview');if(interview&&entities[selected]?.interview){const c=entities[selected];copyText(c.interview.id+' — '+c.interview.question,interview);}});
$('#side-close').addEventListener('click',closeSidebar);
$('#menu').addEventListener('click',()=>{const open=!$('#sidebar').classList.contains('open');$('#sidebar').classList.toggle('open',open);$('#backdrop').classList.toggle('open',open);$('#menu').setAttribute('aria-expanded',String(open));});$('#backdrop').addEventListener('click',closeSidebar);
document.addEventListener('keydown',e=>{
  if(e.key==='Escape'){if($('#sidebar').classList.contains('open'))closeSidebar();else if(document.activeElement?.tagName!=='INPUT')navBack();return;}
  if(e.key!=='ArrowLeft'&&e.key!=='ArrowRight')return;
  if(e.altKey||e.ctrlKey||e.metaKey||e.shiftKey)return;
  if(e.target?.closest?.('input,textarea,select,[contenteditable="true"]'))return;
  e.preventDefault();
  moveCompany(e.key==='ArrowRight'?1:-1);
});
window.addEventListener('hashchange',()=>{
  const match=decodeURIComponent(location.hash.slice(1)).match(/^company-(\d+(?:\.\d+)*)$/);
  if(!match)return;
  const id=companyByNumber(match[1]);
  if(id&&id!==selected)navToCompany(id,false);
});
window.addEventListener('resize',()=>requestAnimationFrame(drawWires));window.addEventListener('load',drawWires);

