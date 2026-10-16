// Add static SVG icons in the initial HTML shell.
$$('[data-icon]').forEach(el=>el.innerHTML=icon(el.dataset.icon));
$('#maincontent').innerHTML='<div class="panel" style="padding:24px;color:var(--dim)">Loading real Shopizer code…</div>';
loadRealCode().catch(error=>{console.error(error);$('#maincontent').innerHTML='<div class="panel" style="padding:24px;color:var(--orange)">Could not load source: '+safe(error.message)+'</div>';});
