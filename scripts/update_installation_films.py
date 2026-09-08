from pathlib import Path

p = Path('installation/index.html')
s = p.read_text()
old = '''<div class="films"><div class="film"><img src="../media/video/hls/we_measure/poster.jpg"><h3>We Measure</h3></div><div class="film"><img src="../media/video/hls/youre_the_wave/poster.jpg"><h3>You're the Wave</h3></div><div class="film"><img src="../media/video/hls/beyond_the_end/poster.jpg"><h3>Beyond the End</h3></div></div>'''
new = '''<div class="films film-player-grid">
<div class="film film-player-card"><div class="film-media"><video class="film-hls" data-hls="../media/video/hls/we_measure/index.m3u8" poster="../media/video/hls/we_measure/poster.jpg" playsinline preload="metadata" controls></video></div><div class="film-foot"><h3>We Measure</h3><button type="button" class="film-fullscreen">full screen</button></div></div>
<div class="film film-player-card"><div class="film-media"><video class="film-hls" data-hls="../media/video/hls/youre_the_wave/index.m3u8" poster="../media/video/hls/youre_the_wave/poster.jpg" playsinline preload="metadata" controls></video></div><div class="film-foot"><h3>You're the Wave</h3><button type="button" class="film-fullscreen">full screen</button></div></div>
<div class="film film-player-card"><div class="film-media"><video class="film-hls" data-hls="../media/video/hls/beyond_the_end/index.m3u8" poster="../media/video/hls/beyond_the_end/poster.jpg" playsinline preload="metadata" controls></video></div><div class="film-foot"><h3>Beyond the End</h3><button type="button" class="film-fullscreen">full screen</button></div></div>
</div>'''
if old not in s:
    raise SystemExit('film block not found')
s = s.replace(old, new, 1)
css = '''\n/* playable moving-image films */\n.film-player-card{min-width:0}.film-media{position:relative;background:#000;border:1px solid var(--l);overflow:hidden}.film-media video{display:block;width:100%;aspect-ratio:16/9;object-fit:cover;background:#000}.film-foot{display:flex;align-items:center;justify-content:space-between;gap:14px;margin-top:10px}.film-foot h3{margin:0}.film-fullscreen{font:8.5px var(--mo);letter-spacing:.16em;text-transform:uppercase;color:var(--f);background:rgba(5,7,10,.72);border:1px solid var(--l);padding:9px 11px;cursor:pointer;white-space:nowrap}.film-fullscreen:hover{border-color:var(--f);color:var(--s)}\n'''
s = s.replace('</style>', css + '\n</style>', 1)
js = '''\n<script src="../media/lib/hls.min.js"></script>\n<script id="installationFilmPlayback">\n(function(){\nvar videos=[].slice.call(document.querySelectorAll('.film-hls[data-hls]'));\nvideos.forEach(function(video){\nvar src=video.dataset.hls;\nif(video.canPlayType('application/vnd.apple.mpegurl')){video.src=src;}\nelse if(window.Hls&&Hls.isSupported()){var hls=new Hls({enableWorker:true,lowLatencyMode:false});hls.loadSource(src);hls.attachMedia(video);video._cotHls=hls;}\nvideo.addEventListener('play',function(){videos.forEach(function(other){if(other!==video&&!other.paused)other.pause();});});\n});\ndocument.querySelectorAll('.film-fullscreen').forEach(function(btn){btn.addEventListener('click',function(){var video=btn.closest('.film-player-card').querySelector('video');if(video.requestFullscreen){video.requestFullscreen();}else if(video.webkitRequestFullscreen){video.webkitRequestFullscreen();}else if(video.webkitEnterFullscreen){video.webkitEnterFullscreen();}});});\n})();\n</script>\n'''
s = s.replace('</body>', js + '\n</body>', 1)
p.write_text(s)
