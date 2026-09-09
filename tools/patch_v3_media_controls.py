from pathlib import Path

p = Path('V3/stage/index.html')
s = p.read_text()

old_css = ".dock{position:fixed;bottom:0;left:0;right:0;z-index:45;min-height:76px;background:rgba(4,6,10,.96);border-top:1px solid var(--l);display:grid;grid-template-columns:auto auto auto minmax(120px,220px) minmax(120px,1fr) auto minmax(72px,110px);align-items:center;gap:10px;padding:10px var(--g)}"
new_css = ".dock{position:fixed;bottom:0;left:0;right:0;z-index:120;min-height:82px;background:rgba(4,6,10,.93);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-top:1px solid rgba(207,230,239,.28);display:grid;grid-template-columns:auto auto auto minmax(140px,220px) auto minmax(160px,1fr) auto minmax(92px,130px);align-items:center;gap:12px;padding:11px var(--g);box-shadow:0 -16px 40px rgba(0,0,0,.34)}"
if old_css not in s:
    raise SystemExit('dock css anchor not found')
s = s.replace(old_css, new_css, 1)

s = s.replace(".seek{width:100%;accent-color:var(--f)}", ".seek{width:100%;accent-color:var(--f);min-width:160px}.time{display:flex;gap:5px;align-items:center;font:9px var(--mo);letter-spacing:.08em;color:var(--d);white-space:nowrap}.time .elapsed{color:var(--s)}", 1)
s = s.replace(".vol{width:100%;accent-color:var(--f)}", ".vol{width:100%;accent-color:var(--f)}.volwrap{display:grid;grid-template-columns:auto 1fr;align-items:center;gap:7px;min-width:92px}.volwrap span{font:8px var(--mo);letter-spacing:.14em;color:var(--d)}", 1)
s = s.replace(".dock input[type=range]{height:2px;cursor:pointer}", ".dock input[type=range]{height:4px;cursor:pointer}.dock input[type=range]::-webkit-slider-thumb{cursor:grab}.dock input[type=range]:active::-webkit-slider-thumb{cursor:grabbing}", 1)

old_mobile = "@media(max-width:780px){body{padding-bottom:126px}.switch{top:70px;left:var(--g);right:auto}.panel{padding-left:24px;padding-right:24px}.sectionbar{left:24px;right:24px}.films{grid-template-columns:1fr}.dock{grid-template-columns:auto auto auto 1fr;grid-template-areas:\"prev play next title\" \"seek seek mute vol\";padding:10px 18px;gap:9px}.dock .prev{grid-area:prev}.dock .play{grid-area:play}.dock .next{grid-area:next}.trackname{grid-area:title}.seek{grid-area:seek}.mute{grid-area:mute}.vol{grid-area:vol}}"
new_mobile = "@media(max-width:780px){body{padding-bottom:148px}.switch{top:70px;left:var(--g);right:auto}.panel{padding-left:24px;padding-right:24px}.sectionbar{left:24px;right:24px}.films{grid-template-columns:1fr}.dock{grid-template-columns:auto auto auto 1fr auto;grid-template-areas:\"prev play next title time\" \"seek seek seek seek seek\" \"mute vol vol vol vol\";padding:10px 18px;gap:9px}.dock .prev{grid-area:prev}.dock .play{grid-area:play}.dock .next{grid-area:next}.trackname{grid-area:title}.time{grid-area:time;justify-self:end}.seek{grid-area:seek}.mute{grid-area:mute}.volwrap{grid-area:vol}.vol{width:100%}}"
if old_mobile not in s:
    raise SystemExit('mobile dock css anchor not found')
s = s.replace(old_mobile, new_mobile, 1)

old_html = '<div class="dock" aria-label="Audio player"><button class="prev" id="prev" aria-label="Previous track">‹</button><button class="play" id="pp" aria-label="Play or pause">▶</button><button class="next" id="next" aria-label="Next track">›</button><div class="trackname" id="now">We Measure</div><input class="seek" id="seek" type="range" min="0" max="100" step="0.1" value="0" aria-label="Track position"><button class="mute" id="mute" aria-label="Audio on or off">AUDIO ON</button><input class="vol" id="vol" type="range" min="0" max="1" step="0.01" value="0.8" aria-label="Volume"></div>'
new_html = '<div class="dock" aria-label="Audio player"><button class="prev" id="prev" aria-label="Previous track" title="Previous track">‹</button><button class="play" id="pp" aria-label="Play or pause" title="Play / pause">▶</button><button class="next" id="next" aria-label="Next track" title="Next track">›</button><div class="trackname" id="now">We Measure</div><div class="time" aria-label="Track time"><span class="elapsed" id="elapsed">0:00</span><span>/</span><span id="duration">0:00</span></div><input class="seek" id="seek" type="range" min="0" max="100" step="0.1" value="0" aria-label="Track position" title="Drag to move through the track"><button class="mute" id="mute" aria-label="Audio on or off" title="Audio on / off">AUDIO ON</button><label class="volwrap"><span>VOL</span><input class="vol" id="vol" type="range" min="0" max="1" step="0.01" value="0.8" aria-label="Volume" title="Volume"></label></div>'
if old_html not in s:
    raise SystemExit('dock html anchor not found')
s = s.replace(old_html, new_html, 1)

old_refs = "seek=document.getElementById('seek'),vol=document.getElementById('vol'),mute=document.getElementById('mute'),prev=document.getElementById('prev'),next=document.getElementById('next');"
new_refs = "seek=document.getElementById('seek'),vol=document.getElementById('vol'),mute=document.getElementById('mute'),prev=document.getElementById('prev'),next=document.getElementById('next'),elapsed=document.getElementById('elapsed'),duration=document.getElementById('duration');"
if old_refs not in s:
    raise SystemExit('player refs anchor not found')
s = s.replace(old_refs, new_refs, 1)

old_state = "let cur=0,rows=[];const playable=()=>"
new_state = "let cur=0,rows=[];const fmt=t=>{if(!isFinite(t)||t<0)return'0:00';const m=Math.floor(t/60),sec=Math.floor(t%60);return m+':'+String(sec).padStart(2,'0')};const playable=()=>"
s = s.replace(old_state, new_state, 1)

s = s.replace("n.textContent=T[i][0];seek.value=0;setActive();", "n.textContent=T[i][0];seek.value=0;elapsed.textContent='0:00';duration.textContent='0:00';setActive();", 1)

old_time = "a.ontimeupdate=()=>{if(a.duration&&!seek.matches(':active'))seek.value=a.currentTime/a.duration*100};seek.oninput=()=>{if(a.duration)a.currentTime=(parseFloat(seek.value)/100)*a.duration};"
new_time = "a.onloadedmetadata=()=>{duration.textContent=fmt(a.duration)};a.ondurationchange=()=>{duration.textContent=fmt(a.duration)};a.ontimeupdate=()=>{elapsed.textContent=fmt(a.currentTime);duration.textContent=fmt(a.duration);if(a.duration&&!seek.matches(':active'))seek.value=a.currentTime/a.duration*100};seek.oninput=()=>{if(a.duration){a.currentTime=(parseFloat(seek.value)/100)*a.duration;elapsed.textContent=fmt(a.currentTime)}};"
if old_time not in s:
    raise SystemExit('timeupdate anchor not found')
s = s.replace(old_time, new_time, 1)

p.write_text(s)
