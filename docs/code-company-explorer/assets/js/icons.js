
'use strict';
const ICONS={
 git:'<path d="M3 3v12a6 6 0 0 0 6 6h12"/><path d="M7 7h10v10H7z"/><circle cx="7" cy="7" r="1"/><circle cx="17" cy="17" r="1"/>',
 folder:'<path d="M3 19V6a2 2 0 0 1 2-2h5l2 3h7a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z"/>',
 folderOpen:'<path d="M3 7V6a2 2 0 0 1 2-2h5l2 3h7a2 2 0 0 1 2 2v2"/><path d="M3 20l3-9h15l-3 9z"/>',
 file:'<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M9 13l-2 2 2 2m6-4 2 2-2 2"/>',
 code:'<path d="m8 8-4 4 4 4m8-8 4 4-4 4m-3-13-2 18"/>',
 building:'<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M8 7h2m4 0h2M8 11h2m4 0h2M8 15h2m4 0h2M10 22v-4h4v4"/>',
 branch:'<path d="M6 3v12a4 4 0 0 0 4 4h8"/><circle cx="6" cy="3" r="2"/><circle cx="18" cy="19" r="2"/><circle cx="6" cy="11" r="2"/>',
 chevron:'<path d="m9 18 6-6-6-6"/>',
 down:'<path d="m6 9 6 6 6-6"/>',
 search:'<circle cx="10" cy="10" r="7"/><path d="m15.5 15.5 6 6"/>',
 copy:'<rect x="8" y="8" width="13" height="13" rx="2"/><path d="M16 8V5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h3"/>',
 menu:'<path d="M4 6h16M4 12h16M4 18h16"/>',
 close:'<path d="m5 5 14 14M19 5 5 19"/>',
 arrow:'<path d="M4 12h16m-6-6 6 6-6 6"/>',
 layers:'<path d="m12 2 9 5-9 5-9-5 9-5Zm-9 10 9 5 9-5M3 17l9 5 9-5"/>',
 back:'<path d="m14 18-6-6 6-6"/>',
 mark:'<path d="M4 12l5 5L20 6"/>'};
function icon(id){return `<span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true">${ICONS[id]||ICONS.code}</svg></span>`;}
function safe(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}

