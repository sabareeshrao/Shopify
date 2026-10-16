function orderedCompanies(){
  const compare=(a,b)=>{
    const aa=entities[a].no.split('.').map(Number), bb=entities[b].no.split('.').map(Number);
    for(let i=0;i<Math.max(aa.length,bb.length);i++){
      if(i===aa.length)return -1;
      if(i===bb.length)return 1;
      if(aa[i]!==bb[i])return aa[i]-bb[i];
    }
    return 0;
  };
  return Object.keys(entities).sort(compare);
}
function companyNumberQuery(q){
  const match=String(q).trim().match(/^(?:company\s*#?\s*)?(\d+(?:\.\d+)*)$/i);
  return match ? match[1].split('.').map(Number).join('.') : null;
}
function companyByNumber(q){
  const num=companyNumberQuery(q);
  return num===null?null:orderedCompanies().find(id=>entities[id].no.split('.').map(Number).join('.')===num)||null;
}
function companySequence(){
  const selectedNo=mode==='company'&&entities[selected]?entities[selected].no:null;
  // Top-level companies navigate 1 → 2 → 3; subsidiaries navigate siblings, e.g. 2.1 → 2.2.
  if(!selectedNo||!selectedNo.includes('.'))return orderedCompanies().filter(id=>!entities[id].no.includes('.'));
  const bits=selectedNo.split('.'),parent=bits.slice(0,-1).join('.')+'.';
  return orderedCompanies().filter(id=>{
    const n=entities[id].no;return n.startsWith(parent)&&n.split('.').length===bits.length;
  });
}
function updateCompanySequence(){
  const items=companySequence(),index=mode==='company'?items.indexOf(selected):-1;
  const prev=$('#prev-company'),next=$('#next-company'),position=$('#sequence-position');
  prev.disabled=index<=0&&index!==-1 || !items.length;
  next.disabled=index>=items.length-1&&index!==-1 || !items.length;
  if(index===-1){prev.disabled=next.disabled=!items.length;position.textContent=items.length+' companies mapped';return;}
  prev.disabled=index===0;
  next.disabled=index===items.length-1;
  position.textContent='Company '+entities[selected].no+' · '+(index+1)+' / '+items.length;
  prev.setAttribute('aria-label',index>0?'Previous: Company '+entities[items[index-1]].no:'First company');
  next.setAttribute('aria-label',index<items.length-1?'Next: Company '+entities[items[index+1]].no:'Last mapped company');
}
function moveCompany(direction){
  const items=companySequence();
  if(!items.length)return;
  const index=mode==='company'?items.indexOf(selected):-1;
  const nextIndex=index<0?(direction>0?0:items.length-1):index+direction;
  if(nextIndex<0||nextIndex>=items.length)return;
  navToCompany(items[nextIndex]);
}

function searchResults(q){
  const r=$('#search-results'),value=String(q).trim();
  if(!value){r.hidden=true;r.innerHTML='';return;}
  const numeric=companyNumberQuery(value);
  if(numeric!==null){
    const id=companyByNumber(value);
    r.innerHTML=id
      ?`<button type="button" data-company="${id}" aria-label="Open Company ${safe(entities[id].no)}">${icon('building')}<span><b>Company ${safe(entities[id].no)} · ${safe(entities[id].name)}</b><small>${safe(files[entities[id].file].name)} · tap to open</small></span></button>`
      :`<div class="search-unmapped">Company ${safe(numeric)} has not been created yet. Only verified companies are available.</div>`;
    r.hidden=false;return;
  }
  const needle=value.toLowerCase(),hits=[];
  for(const id of orderedCompanies()){
    const c=entities[id],file=files[c.file];
    if((c.no+' '+c.name+' '+c.method+' '+c.desc+' '+file.name+' '+file.path).toLowerCase().includes(needle)){
      hits.push({type:'company',id,label:'Company '+c.no+' · '+c.name,sub:c.method+' · '+file.name});
    }
  }
  for(const [id,f] of Object.entries(files)){
    if((f.name+' '+f.path+' '+f.about).toLowerCase().includes(needle))hits.push({type:'file',id,label:f.name,sub:f.path});
  }
  r.innerHTML=hits.slice(0,18).map(it=>`<button data-${it.type==='file'?'gofile':'company'}="${it.id}">${icon(it.type==='file'?'file':'building')}<span><b>${safe(it.label)}</b><small>${safe(it.sub)}</small></span></button>`).join('')||'<div class="search-unmapped">No matching company or file yet.</div>';
  r.hidden=false;
}
function getLocation(){if(mode==='company'){const c=entities[selected];return `${files[c.file].path}:${c.start}-${c.end||c.start+(c.code?.length||1)-1} (Company ${c.no})`;}return mode==='file'?files[selectedFile].path:folderPath;}
async function copyText(text,button){try{await navigator.clipboard.writeText(text);flash(button,'Copied');}catch(e){const box=document.createElement('textarea');box.value=text;box.style.position='fixed';box.style.opacity='0';document.body.appendChild(box);box.select();try{document.execCommand('copy');flash(button,'Copied');}catch(err){flash(button,'Copy unavailable');}box.remove();}}
function flash(el,txt){const previous=el.dataset.original||el.innerHTML;if(!el.dataset.original)el.dataset.original=previous;el.textContent=txt;setTimeout(()=>{if(el.isConnected)el.innerHTML=previous;},1200);}
