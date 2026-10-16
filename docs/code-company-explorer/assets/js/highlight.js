function $$(selector){return Array.from(document.querySelectorAll(selector));}

/* One source of truth for selected card, code line and explanation. */
function findLineInfo(id,line){
 const c=entities[id],root=topEntity(id);
 for(const ent of Object.values(entities)){
   if(ent.parent&&topEntity(Object.keys(entities).find(k=>entities[k]===ent))===root&&line>=ent.start&&line<=ent.end)
     return {head:'Company '+ent.no+' · '+ent.name,description:ent.desc};
 }
 const linked=(root.needs||[]).find(dep=>dep.line===line&&entities[dep.to]);
 if(linked)return {head:'Uses Company '+entities[linked.to].no+' · '+entities[linked.to].name,description:entities[linked.to].desc};
 const external=(root.externalSuppliers||[]).find(dep=>dep.code_line===line);
 if(external)return {head:external.name,description:external.description||root.desc};
 const incoming=(root.externalClients||[]).find(dep=>dep.code_line===line);
 if(incoming)return {head:incoming.name,description:incoming.description||root.desc};
 return {head:files[c.file].name+' · line '+line,description:c.desc};
}
function resetSelection(){
 activeLine=null;
 activeRelationKey=null;
}
function selectLine(line,scroll=true,relationKey=null,details=null){
 if(mode!=='company'||!entities[selected])return;
 const company=entities[selected],first=company.start,last=company.end||company.start+(company.code||[]).length-1;
 const n=Number(line);
 if(!Number.isFinite(n))return;
 activeLine=n>=first&&n<=last?n:null;
 activeRelationKey=relationKey;
 $$('.relation-card').forEach(el=>{
   const on=!!relationKey&&el.dataset.relationKey===relationKey;
   el.classList.toggle('is-selected',on);
   el.setAttribute('aria-pressed',String(on));
 });
 $$('#wires .wire-path').forEach(el=>{el.classList.toggle('is-selected',!!relationKey&&el.dataset.relationKey===relationKey);el.classList.toggle('is-muted',!!relationKey&&el.dataset.relationKey!==relationKey);});
 $$('#current-code .code-row').forEach(el=>{
   const row=Number(el.dataset.line);
   el.classList.toggle('highlight',(activeLine!==null&&row===activeLine)||
     (!!company.parent&&row>=company.start&&row<=company.end));
 });
 const info=details||findLineInfo(selected,n);
 const title=$('#detail-title'),note=$('#detail-note'),label=$('#detail-line');
 if(title)title.textContent=info.head;
 if(note)note.textContent=info.description;
 if(label)label.textContent='Line '+n+(activeLine===null?' · related file':'');
 if(scroll&&activeLine!==null){
   const pane=$('#current-code'),row=pane?.querySelector('.code-row[data-line="'+activeLine+'"]');
   if(pane&&row){
     const region=pane.getBoundingClientRect(),position=row.getBoundingClientRect();
     if(position.top<region.top+8)pane.scrollTop+=position.top-region.top-8;
     else if(position.bottom>region.bottom-8)pane.scrollTop+=position.bottom-region.bottom+8;
   }
 }
}
function selectExternalCard(button){
 if(mode!=='company'||!button)return;
 const side=button.dataset.external;
 const index=Number(button.dataset.externalIndex);
 if((side!=='uses'&&side!=='usedby')||!Number.isInteger(index)||index<0)return;
 const company=entities[selected];
 const data=(side==='uses'?company.externalSuppliers:company.externalClients)[index];
 if(!data)return;
 const relationKey=side+':outside-'+(side==='uses'?'out-':'in-')+index;
 selectLine(data.code_line??company.start,true,relationKey,{
   head:data.name,description:data.description||company.desc
 });
}
