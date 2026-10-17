document.addEventListener('click',e=>{
 const external=e.target.closest('.relation-card[data-external]');
 if(external){selectExternalCard(external);return;}
 const folder=e.target.closest('[data-folder]');if(folder){const key=folder.dataset.folder;if(expanded.has(key))expanded.delete(key);else expanded.add(key);renderTree();return;}const file=e.target.closest('[data-file]');if(file){const id=file.dataset.file,key='file:'+id;if(e.target.closest('.tree-chevron')){if(expanded.has(key))expanded.delete(key);else expanded.add(key);renderTree();}else{expanded.add(key);navToFile(id);}return;}const comp=e.target.closest('[data-company]');if(comp){const id=comp.dataset.company;if(comp.classList.contains('tree-row')&&e.target.closest('.tree-chevron')&&entities[id]?.children?.length){const key='co:'+id;if(expanded.has(key))expanded.delete(key);else expanded.add(key);renderTree();return;}if(!entities[id])return;
if(comp.classList.contains('relation-card')&&comp.tagName==='A')return;
if(comp.classList.contains('subs-card')){
 const url=new URL(location.href);url.hash='company-'+encodeURIComponent(entities[id].no);
 window.open(url.href,'_blank','noopener,noreferrer');
 try{window.focus();}catch(ignore){}
 return;
}
const wantLine=comp.dataset.highlight;
const from=selected&&entities[selected]?entities[selected]:null,fromFile=from?files[from.file]:null,side=comp.dataset.side;
navToCompany(id);
if(wantLine&&from){
 const target=entities[id],call=Number(wantLine),declaration=target.methodStart||target.start;
 if(Number.isInteger(call)&&side==='usedby'&&call>=target.start&&call<=target.end){
   selectLine(call,false,null,{head:'Verified caller · source line '+call,description:'Company '+target.no+' calls Company '+from.no+' at '+files[target.file].name+':'+call+'. This green highlight is the actual callsite.'});
 }else if(Number.isInteger(call)){
   selectLine(declaration,false,null,{head:'Company '+target.no+' · method declaration',description:'Opened from Company '+from.no+' ('+fromFile.name+', line '+call+'). The callsite is in that previous company; highlighted line '+declaration+' is the destination method declaration.'});
 }
}
$('#search-results').hidden=true;return;}const go=e.target.closest('[data-gofile]');if(go){navToFile(go.dataset.gofile);return;}const fo=e.target.closest('[data-openfolder]');if(fo){navToFolder(fo.dataset.openfolder);return;}const line=e.target.closest('#maincontent .code-row[data-line]');
if(line){const n=Number(line.dataset.line);if(mode==='file'){const id=line.dataset.sourceCompany;if(id&&entities[id]){navToCompany(id);selectLine(n,false,null,{head:'Original Java source · line '+n,description:'Opened Company '+entities[id].no+' from '+files[entities[id].file].name+', source line '+n+'.'});}else{inspectUnnumberedLine(n);}}else selectLine(n,true,null);return;}if(!e.target.closest('.searchwrap'))$('#search-results').hidden=true;});
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
$('#maincontent').addEventListener('click',e=>{const back=e.target.closest('#back-company');if(back){navBack();return;}const btn=e.target.closest('#copy-method');if(btn){const c=getCode(selected);copyText(c.lines.join('\n'),btn);}const interview=e.target.closest('#copy-interview');if(interview&&entities[selected]?.interview){const c=entities[selected];copyText(c.interview.id+' — '+c.interview.question,interview);}});
$('#history-back').addEventListener('click',navBack);
$('#side-close').addEventListener('click',closeSidebar);
$('#menu').addEventListener('click',()=>{const open=!$('#sidebar').classList.contains('open');$('#sidebar').classList.toggle('open',open);$('#backdrop').classList.toggle('open',open);$('#menu').setAttribute('aria-expanded',String(open));if(open)queueRevealCurrentTreeRow();});$('#backdrop').addEventListener('click',closeSidebar);
document.addEventListener('keydown',e=>{
  if((e.key==='Enter'||e.key===' ')&&e.target?.closest?.('#maincontent .code-row[data-source-company],#maincontent .code-row[data-source-context]')){e.preventDefault();e.target.closest('.code-row').click();return;}
  if(e.key==='Escape'){if($('#sidebar').classList.contains('open'))closeSidebar();else if(document.activeElement?.tagName!=='INPUT')navBack();return;}
  if(e.key!=='ArrowLeft'&&e.key!=='ArrowRight')return;
  if(e.altKey||e.ctrlKey||e.metaKey||e.shiftKey)return;
  if(e.target?.closest?.('input,textarea,select,[contenteditable="true"],[role="separator"]'))return;
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

