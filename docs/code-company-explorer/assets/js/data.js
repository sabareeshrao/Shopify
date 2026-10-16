const files={},entities={},folderData={name:'shopizer',children:[]};
const filePathIndex=new Map();
let PINNED_SHOPIZER_REF='';
const loadingFiles=new Map();
function sourceFileId(path){return filePathIndex.get(path)||null;}
async function ensureSourceLoaded(fid){
  const f=files[fid];
  if(!f||f.source)return;
  if(loadingFiles.has(fid))return loadingFiles.get(fid);
  if(!sourceIsText(f)){f.loadingState='unsupported';return;}
  f.loadingState='loading';
  const sourceUrl='https://raw.githubusercontent.com/shopizer-ecommerce/shopizer/'+PINNED_SHOPIZER_REF+'/'+f.path.split('/').map(encodeURIComponent).join('/');
  const pending=(async()=>{
    try{
      const response=await fetch(sourceUrl,{mode:'cors',cache:'force-cache'});
      if(!response.ok)throw Error('HTTP '+response.status+' from pinned Shopizer source');
      const raw=(await response.text()).replace(/\r\n?/g,'\n');
      if(raw.includes('\u0000'))throw Error('This file cannot be displayed as text');
      const lines=raw.split('\n');
      if(lines.at(-1)==='')lines.pop();
      f.source=lines;f.loadingState='ready';f.loadError=null;
    }catch(error){f.loadError=String(error.message||error);f.loadingState='error';}
    finally{loadingFiles.delete(fid);}
  })();
  loadingFiles.set(fid,pending);
  return pending;
}
async function loadRealCode(){
  const [manifest,tree,mentors]=await Promise.all([
    fetch('./companies.json',{cache:'no-store'}).then(r=>{if(!r.ok)throw Error('Cannot load companies.json');return r.json()}),
    fetch('./repository-tree.json',{cache:'no-store'}).then(r=>{if(!r.ok)throw Error('Cannot load complete repository tree');return r.json()}),
    fetch('./mentor-lessons.json',{cache:'no-store'}).then(r=>{if(!r.ok)throw Error('Cannot load mentor company lessons');return r.json()})
  ]);
  if(mentors.reference_commit!==manifest.reference.ref)throw Error('Mentor explanations do not match the pinned source');
  const missingLessons=manifest.companies.filter(c=>!mentors.lessons?.[c.id]);
  if(missingLessons.length)throw Error('Missing company mentor lessons: '+missingLessons.map(c=>c.id).join(', '));
  if(!tree.complete_tree||tree.reference_commit!==manifest.reference.ref)throw Error('Repository tree does not match the pinned source commit');
  if(tree.file_count!==tree.files.length)throw Error('Repository tree count mismatch');
  PINNED_SHOPIZER_REF=manifest.reference.ref;
  const sourcePaths=[...new Set(manifest.companies.map(c=>c.source_data_file))];
  const sources=Object.fromEntries(await Promise.all(sourcePaths.map(async p=>[p,await fetch('./'+p,{cache:'no-store'}).then(r=>{if(!r.ok)throw Error('Cannot load '+p);return r.json()})])));
  folderData.children=[];
  for(const entry of tree.files){
    const path=entry.path;
    if(typeof path!=='string'||path.includes('..'))throw Error('Invalid repository path');
    if(filePathIndex.has(path))throw Error('Duplicate repository file path: '+path);
    const fid='file-'+(filePathIndex.size+1),name=path.split('/').at(-1);
    files[fid]={id:fid,name,path,about:'Original Shopizer file · not yet mapped as a company',companyIds:[],source:null,
      size:entry.size,blobSha:entry.sha,loadingState:null,loadError:null};
    filePathIndex.set(path,fid);
    let parent=folderData;
    for(const part of path.split('/').slice(0,-1)){
      let next=parent.children.find(x=>x.name===part&&!x.file);
      if(!next){next={name:part,children:[]};parent.children.push(next);}
      parent=next;
    }
    parent.children.push({name,file:fid});
  }
  for(const c of manifest.companies){
    const fid=filePathIndex.get(c.source_path);
    if(!fid)throw Error('Mapped company is absent from pinned repository: '+c.id);
    const source=sources[c.source_data_file];
    if(!source||source.source_path!==c.source_path||source.source_blob_sha!==c.source_blob_sha)throw Error('Pinned company source is inconsistent: '+c.id);
    const f=files[fid];
    if(f.source&&f.source!==source.lines&&f.source.length!==source.lines.length)throw Error('Multiple source snapshots for file '+c.source_path);
    f.source=source.lines;f.loadingState='ready';f.about='Verified Shopizer Java source · '+source.lines.length+' lines';
    if(!f.source||f.source.length<c.end_line)throw Error('Incorrect source line range for company '+c.id);
    const eid='company-'+c.id;
    entities[eid]={no:c.id,file:fid,name:c.name,method:c.method,desc:c.plain_english,start:c.start_line,end:c.end_line,
      code:f.source.slice(c.start_line-1,c.end_line),parent:c.parent_id?'company-'+c.parent_id:null,children:[],
      needs:(c.outbound||[]).filter(dep=>dep.company_id).map(dep=>({to:'company-'+dep.company_id,line:dep.code_line,kind:dep.kind})),
      sequenceReason:c.sequence_reason||'',mentorWhy:mentors.lessons[c.id],interview:c.interview||null,methodStart:c.method_start_line||c.start_line,
      externalClients:(c.inbound||[]).filter(dep=>!dep.company_id),externalSuppliers:(c.outbound||[]).filter(dep=>!dep.company_id)};
    if(!c.parent_id)f.companyIds.push(eid);
  }
  for(const [id,c] of Object.entries(entities))if(c.parent&&entities[c.parent])entities[c.parent].children.push(id);
  for(const [id,c] of Object.entries(entities))for(const dep of c.needs)
    if(!entities[dep.to])throw Error('Missing linked company from '+c.no+' to '+dep.to);
  for(const f of Object.values(files))f.companyIds.sort((x,y)=>entities[x].start-entities[y].start);
  const link=decodeURIComponent(location.hash.replace(/^#/,'')).match(/^company-(\d+(?:\.\d+)*)$/);
  const requested=link&&manifest.companies.find(c=>c.id===link[1]);
  selected='company-'+(requested?.id||manifest.companies.at(-1).id);
  selectedFile=entities[selected].file;mode='company';activeLine=null;folderPath='shopizer';
  expanded.clear();
  openParents(selected);
  document.querySelector('.repo-title span:nth-child(2)').textContent='shopizer-ecommerce / shopizer';
  document.querySelector('.repo-meta').innerHTML='<span class="demo-dot"></span> '+tree.file_count+' original files · '+manifest.count+' companies mapped';
  document.querySelector('.side-bottom').innerHTML='<span>JAVA · SPRING BOOT</span><b>PINNED SHOPIZER</b>';
  document.title='Code Company | Shopizer · '+manifest.count+' Companies · '+tree.file_count+' Files';
  renderAll();
  queueRevealCurrentTreeRow();
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
