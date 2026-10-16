function drawWires(){if(mode!=='company')return;const net=$('#network'),svg=$('#wires'),center=$('#focus-card');if(!net||!svg||!center)return;const B=net.getBoundingClientRect(),C=center.getBoundingClientRect();if(window.matchMedia('(max-width:1100px)').matches){svg.innerHTML='';return;}svg.setAttribute('viewBox',`0 0 ${B.width} ${B.height}`);let paths='';for(const side of ['usedby','uses']){const cards=$$('.graph-col.'+side+' .relation-card');const total=cards.length;cards.forEach((el,i)=>{const A=el.getBoundingClientRect(),left=side==='usedby',dir=left?1:-1;const x1=(left?A.right:A.left)-B.left,y1=A.top+A.height/2-B.top,x2=(left?C.left:C.right)-B.left,y2=C.top+Math.max(38,Math.min(C.height-30,100+(i-(total-1)/2)*25))-B.top;const stroke=left?'#53aaff':'#ffa445';paths+=`<path class="wire-path${el.dataset.relationKey===activeRelationKey?' is-selected':''}" data-relation-key="${safe(el.dataset.relationKey||'')}" d="M${x1},${y1} C${x1+dir*32},${y1} ${x2-dir*28},${y2} ${x2},${y2}" stroke="${stroke}" stroke-width="2" fill="none" opacity=".84"/><circle cx="${x2}" cy="${y2}" r="3.6" fill="${stroke}"/><circle cx="${x1}" cy="${y1}" r="2.5" fill="${stroke}"/>`;});}svg.innerHTML=paths;}

function getRelations(id){
  const c=entities[id];
  const needs=(c.needs||[]).filter(x=>entities[x.to]),usedBy=clientsOf(id).filter(x=>entities[x.id]);
  (c.externalClients||[]).forEach((x,i)=>usedBy.push({id:'outside-in-'+i,line:x.code_line??c.start}));
  (c.externalSuppliers||[]).forEach((x,i)=>needs.push({to:'outside-out-'+i,line:x.code_line??c.start}));
  return {needs,usedBy};
}
function edgeCard(id,line,side,index){
  if(String(id).startsWith('outside-')){
    // Relation cards may interleave internal companies and external APIs. The
    // array position is not the external source index (e.g. Company 6 has two internal calls).
    const sourceIndex=Number(String(id).split('-').at(-1));
    const data=(side==='usedby'?entities[selected].externalClients:entities[selected].externalSuppliers)[sourceIndex];
    if(!data)return '';
    const relationKey=side+':'+id;
    return `<button type="button" class="relation-card${activeRelationKey===relationKey?' is-selected':''}" data-relation-key="${safe(relationKey)}" aria-pressed="${activeRelationKey===relationKey}" data-external="${side}" data-external-index="${sourceIndex}" data-line="${data.code_line??entities[selected].start}">
    <span class="rel-num">${side==='usedby'?'WHO STARTS IT':'OUTSIDE SERVICE'} <span class="rel-arrow">↗</span></span>
    <span class="rel-name">${safe(data.name)}</span>
    <span class="rel-file">${safe(data.description||'Outside this Java file')}</span>
    <span class="rel-line">Code line ${data.code_line??entities[selected].start}</span></button>`;
  }
  const c=entities[id];
  const relationKey=side+':'+id;
  return `<a class="relation-card${activeRelationKey===relationKey?' is-selected':''}" href="${safe(location.pathname+location.search+'#company-'+encodeURIComponent(c.no))}" target="_blank" rel="noopener noreferrer" aria-label="Open Company ${safe(c.no)} in another tab" data-relation-key="${safe(relationKey)}" data-company="${id}" data-highlight="${line??''}" data-side="${side}" data-index="${index}">
  <span class="rel-num">COMPANY ${safe(c.no)} <span class="rel-arrow">↗</span></span>
  <span class="rel-name">${safe(c.name)}</span><span class="rel-file">${safe(files[c.file].name)}</span>
  ${line!=null?`<span class="rel-line">Connected at line ${line}</span>`:''}</a>`;
}
