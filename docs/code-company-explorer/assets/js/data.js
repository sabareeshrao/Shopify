const files={},entities={},folderData={name:'shopizer',children:[]};
async function loadRealCode(){
  const manifest=await fetch('./companies.json',{cache:'no-store'}).then(r=>{if(!r.ok)throw Error('Cannot load companies.json');return r.json()});
  const sourcePaths=[...new Set(manifest.companies.map(c=>c.source_data_file))];
  const sources=Object.fromEntries(await Promise.all(sourcePaths.map(async p=>[p,await fetch('./'+p,{cache:'no-store'}).then(r=>{if(!r.ok)throw Error('Cannot load '+p);return r.json()})])));
  folderData.children=['sm-core-model','sm-core-modules','sm-core','sm-shop-model','sm-shop'].map(name=>({name,children:[]}));
  const seen=new Map();
  for(const c of manifest.companies){
    const p=c.source_path;
    if(!seen.has(p)){
      const source=sources[c.source_data_file];
      if(!source||source.source_path!==p)throw Error('Wrong file: '+p);
      const id='file-'+(seen.size+1),name=p.split('/').at(-1);
      files[id]={name,path:p,about:'Shopizer Java source · '+source.lines.length+' lines',companyIds:[],source:source.lines};
      seen.set(p,id);
      let parent=folderData;
      for(const part of p.split('/').slice(0,-1)){let next=parent.children.find(x=>x.name===part&&!x.file);if(!next){next={name:part,children:[]};parent.children.push(next)}parent=next}
      parent.children.push({name,file:id});
    }
    const fid=seen.get(p),eid='company-'+c.id;
    if(!files[fid].source||files[fid].source.length<c.end_line)throw Error('Wrong source line range: '+c.id);
    entities[eid]={no:c.id,file:fid,name:c.name,method:c.method,desc:c.plain_english,start:c.start_line,end:c.end_line,
      code:files[fid].source.slice(c.start_line-1,c.end_line),parent:c.parent_id?'company-'+c.parent_id:null,children:[],
      needs:(c.outbound||[]).filter(dep=>dep.company_id).map(dep=>({to:'company-'+dep.company_id,line:dep.code_line,kind:dep.kind})),
      sequenceReason:c.sequence_reason||'',interview:c.interview||null,methodStart:c.method_start_line||c.start_line,
      externalClients:(c.inbound||[]).filter(dep=>!dep.company_id),externalSuppliers:(c.outbound||[]).filter(dep=>!dep.company_id)};
    if(!c.parent_id)files[fid].companyIds.push(eid);
  }
  for(const [id,c] of Object.entries(entities))if(c.parent&&entities[c.parent])entities[c.parent].children.push(id);
  for(const [id,c] of Object.entries(entities)){
    for(const dep of c.needs)if(!entities[dep.to])throw Error('Missing linked company from '+c.no+' to '+dep.to);
  }
  for(const f of Object.values(files))f.companyIds.sort((x,y)=>entities[x].start-entities[y].start);
  const link=decodeURIComponent(location.hash.replace(/^#/,'')).match(/^company-(\d+(?:\.\d+)*)$/);
  const requested=link&&manifest.companies.find(c=>c.id===link[1]);
  selected='company-'+(requested?.id||manifest.companies.at(-1).id);
  selectedFile=entities[selected].file;mode='company';activeLine=null;folderPath='shopizer';
  expanded.clear();expanded.add('f:shopizer');
  for(const file of Object.values(files)){let part='shopizer';for(const folder of file.path.split('/').slice(0,-1)){part+='/'+folder;expanded.add('f:'+part)}expanded.add('file:'+selectedFile)}
  document.querySelector('.repo-title span:nth-child(2)').textContent='shopizer-ecommerce / shopizer';
  document.querySelector('.repo-meta').innerHTML='<span class="demo-dot"></span> Real source · '+manifest.count+' verified companies';
  document.querySelector('.side-bottom').innerHTML='<span>JAVA · SPRING BOOT</span><b>REAL SOURCE</b>';
  renderAll();
}
// Initial tree state: the real GitHub directory hierarchy stays intact.
const expanded=new Set();
let selectedFile='',selected='',mode='company',activeLine=null,activeRelationKey=null,navStack=[];
const $=s=>document.querySelector(s);
function entityLineCount(c){return c.end?c.end-c.start+1:c.code?.length||0;}
function topEntity(id){let c=entities[id];while(c?.parent)c=entities[c.parent];return c;}
function getCode(id){const c=entities[id];if(!c.parent)return {lines:c.code||[],start:c.start,highlight:[]};const root=topEntity(id);return {lines:root.code||[],start:root.start,highlight:Array.from({length:c.end-c.start+1},(_,i)=>c.start+i)};}
function getNeeds(id){return entities[id].needs||[];}
function clientsOf(id){const seen=new Set(),out=[];if(entities[id].parent){out.push({id:entities[id].parent,line:entities[id].start});seen.add(entities[id].parent);}for(const [from,entity] of Object.entries(entities)){for(const dep of entity.needs||[]){if(dep.to!==id)continue;const key=from;if(!seen.has(key)){seen.add(key);out.push({id:from,line:dep.line});}}}return out;}
