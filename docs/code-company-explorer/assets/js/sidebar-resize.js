/* Resizable IDE-like Project panel. The main content remains fully visible and company IDs are untouched. */
(function(){
 'use strict';
 const handle=document.getElementById('sidebar-resizer');
 const sidebar=document.getElementById('sidebar');
 if(!handle||!sidebar)return;
 const STORE_KEY='code-company-explorer.sidebar-width.v1';
 const DEFAULT=318,MIN=260;
 const mobile=window.matchMedia('(max-width:1100px)');
 let current=DEFAULT,pointer=null,frame=null;
 const maxWidth=()=>Math.max(MIN,Math.min(900,window.innerWidth-410));
 const clamp=v=>Math.min(maxWidth(),Math.max(MIN,Math.round(v)));
 const persist=()=>{try{window.localStorage.setItem(STORE_KEY,String(current))}catch(ignore){}};
 const wireUpdate=()=>{
   if(frame!==null)return;
   frame=requestAnimationFrame(()=>{frame=null;if(typeof drawWires==='function')drawWires()});
 };
 function setWidth(value,save=false){
   current=clamp(value);
   document.documentElement.style.setProperty('--sidebar-width',current+'px');
   handle.setAttribute('aria-valuenow',String(current));
   handle.setAttribute('aria-valuemax',String(maxWidth()));
   if(save)persist();
   wireUpdate();
 }
 try{
   const stored=Number(window.localStorage.getItem(STORE_KEY));
   if(Number.isFinite(stored)&&stored>=MIN)setWidth(stored);
   else setWidth(DEFAULT);
 }catch(ignore){setWidth(DEFAULT);}
 function endDrag(e){
   if(pointer===null||e&&e.pointerId!==pointer)return;
   pointer=null;document.body.classList.remove('sidebar-resizing');
   persist();wireUpdate();
 }
 handle.addEventListener('pointerdown',e=>{
   if(mobile.matches||e.button!==0)return;
   pointer=e.pointerId;
   document.body.classList.add('sidebar-resizing');
   handle.setPointerCapture(e.pointerId);
   e.preventDefault();
 });
 handle.addEventListener('pointermove',e=>{
   if(pointer===null||e.pointerId!==pointer||mobile.matches)return;
   setWidth(e.clientX);e.preventDefault();
 });
 handle.addEventListener('pointerup',endDrag);
 handle.addEventListener('pointercancel',endDrag);
 handle.addEventListener('lostpointercapture',()=>{if(pointer!==null)endDrag()});
 handle.addEventListener('dblclick',()=>{if(!mobile.matches)setWidth(DEFAULT,true)});
 handle.addEventListener('keydown',e=>{
   if(mobile.matches)return;
   let target=null;
   const step=e.shiftKey?40:16;
   if(e.key==='ArrowRight')target=current+step;
   if(e.key==='ArrowLeft')target=current-step;
   if(e.key==='Home')target=MIN;
   if(e.key==='End')target=maxWidth();
   if(target===null)return;
   e.preventDefault();e.stopPropagation();setWidth(target,true);
 });
 window.addEventListener('resize',()=>{setWidth(current);wireUpdate()});
})();
