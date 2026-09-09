from pathlib import Path
import subprocess

ROOT=Path('.')
V3=ROOT/'V3'
(V3/'stage').mkdir(parents=True,exist_ok=True)
(V3/'installation').mkdir(parents=True,exist_ok=True)
backup='63cf874989e724deb465d549b8b33632b3601332'
original=subprocess.check_output(['git','show',f'{backup}:index.html'],text=True)

# --- root: preserve original design/content exactly, only rebase media and refine requested presentation ---
s=original.replace('"media/','"../media/').replace("'media/","'../media/")
s=s.replace('href="stage/"','href="./stage/"').replace('href="installation/"','href="./installation/"')
root_patch=r'''
/* V3 refinement — preserve original COT language */
.vbg video{opacity:.90!important;filter:grayscale(.34) contrast(1.06) brightness(.66)!important}
.find,.imat,.acc,.format-card{background:rgba(8,11,15,.56)!important}
.find:hover,.format-card:hover{background:rgba(12,16,20,.66)!important}
.find .fx .plus,.acc-h .plus{font-size:0!important;min-width:112px;text-align:right}
.find .fx .plus::before,.acc-h .plus::before{content:"open details  ↘";font-family:var(--mono);font-size:8px;letter-spacing:.16em;text-transform:uppercase;color:var(--filament);white-space:nowrap}
.find.open .fx .plus::before,.acc.open .acc-h .plus::before{content:"close details  ↗"}
.format-card p{color:var(--ink)!important}
'''
s=s.replace('</style>',root_patch+'</style>',1)
(V3/'index.html').write_text(s)

split_css=r'''
/* V3 — original Construct of Time design language */
body:after{content:"";position:fixed;inset:0;pointer-events:none;z-index:80;background:radial-gradient(125% 95% at 50% 50%,transparent 52%,rgba(0,0,0,.55) 100%);mix-blend-mode:multiply}
body:before{content:"";position:fixed;inset:-40%;z-index:79;pointer-events:none;opacity:.028;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.panel{min-height:auto!important;padding-block:clamp(82px,11vh,132px)!important;margin-block:clamp(18px,2.5vh,30px)!important;overflow:visible!important}
.hero{min-height:100svh!important;margin-top:0!important;overflow:hidden!important}
.bg video{opacity:.90!important;filter:grayscale(.34) brightness(.50) contrast(1.1)!important}
.bg:after{background:radial-gradient(100% 90% at 50% 50%,rgba(4,6,9,.48),rgba(5,7,10,.82) 75%,rgba(5,7,10,.94))!important}
.sectionbar{position:absolute!important;top:-34px!important;left:50%!important;right:auto!important;transform:translateX(-50%);width:min(560px,72vw)!important;height:auto!important;display:grid!important;grid-template-columns:1fr auto 1fr!important;gap:20px!important;border:0!important;align-items:center!important}
.sectionbar:before,.sectionbar:after{content:"";height:1px;background:linear-gradient(90deg,transparent,rgba(207,230,239,.48))}
.sectionbar:after{background:linear-gradient(90deg,rgba(207,230,239,.48),transparent)}
.sectionbar i{grid-column:2;font:italic 300 24px var(--ser)!important;color:var(--f)!important;min-width:24px!important;text-align:center}
.sectionbar span{display:none!important}
.inner{max-width:1180px}.copy{color:#aeb8be!important}
.score,.state,.research,.card{background:rgba(7,10,14,.50)!important}.trk.active{background:rgba(207,230,239,.035)!important}
.film img,.film video{background:#020304}
@media(max-width:780px){.sectionbar{width:min(420px,76vw)!important}.panel{padding-block:82px!important;margin-block:18px!important}}
'''
accordion_css=r'''
.editorial-notes{margin-top:44px;border-top:1px solid rgba(207,230,239,.12)}
.editorial-notes details{border-bottom:1px solid rgba(207,230,239,.10);padding:0}
.editorial-notes summary{list-style:none;cursor:pointer;padding:22px 4px;display:grid;grid-template-columns:34px 1fr auto;gap:14px;align-items:center}
.editorial-notes summary::-webkit-details-marker{display:none}.editorial-notes .dn{font:9px var(--mo);letter-spacing:.18em;color:var(--f)}
.editorial-notes summary b{font:400 clamp(21px,2.2vw,28px) var(--ser)}.editorial-notes .more{font:8px var(--mo);letter-spacing:.16em;text-transform:uppercase;color:var(--f);white-space:nowrap}
.editorial-notes details[open] .more{font-size:0}.editorial-notes details[open] .more:after{content:"close details ↑";font-size:8px}
.editorial-notes .dc{padding:0 4px 28px 48px;max-width:78ch}.editorial-notes .dc p{color:var(--i);font-size:14.5px;line-height:1.8;margin-top:14px}
'''

def rebase(s):
    return s.replace('../media/','../../media/')

# --- stage ---
p=Path('stage/index.html'); stage=rebase(p.read_text())
stage=stage.replace('</style>',split_css+accordion_css+r'''
.film video{width:100%;aspect-ratio:16/9;object-fit:cover;border:1px solid var(--l);display:block}
</style>''',1)
stage=stage.replace('What happens when a room gives its attention to the same <em>moment</em>?','What happens when hundreds of private timelines are pulled into the same <em>now</em>?')
stage=stage.replace('Music, moving image, performers, darkness and light unfold as one continuous composition. Each element changes the perception of the others, gathering hundreds of individual experiences into a temporary shared present.','The score, moving image, performers and architectural light operate as one system. Rhythm predicts. Repetition conditions. Darkness removes reference. The audience is not told what time feels like; its own attention becomes the material.')
stage=stage.replace('For a while, everyone is carried by the same clock.','The clock keeps running. The room begins to feel something else.')
stage=stage.replace('Seven screens create a fractured cinematic horizon around three performers. Image moves through the structure while light, haze and laser extend its geometry into the room.','Seven vertical screens form a physical cinematic architecture around three performers. Image moves across the array as material, not backdrop. Light extends the geometry beyond the screens; sub-bass gives it weight; the performers remain inside the same visual system as the audience.')
# Ensure three film fragments are playable.
if '<div class="film"><img src="../../media/video/hls/we_measure/poster.jpg">' in stage:
    old='<div class="films"><div class="film"><img src="../../media/video/hls/we_measure/poster.jpg"><h3>We Measure</h3></div><div class="film"><img src="../../media/video/hls/youre_the_wave/poster.jpg"><h3>You\'re the Wave</h3></div><div class="film"><img src="../../media/video/hls/beyond_the_end/poster.jpg"><h3>Beyond the End</h3></div></div>'
    new='<div class="films"><div class="film"><video class="film-hls" controls playsinline preload="none" poster="../../media/video/hls/we_measure/poster.jpg" data-hls="../../media/video/hls/we_measure/index.m3u8"></video><h3>We Measure</h3></div><div class="film"><video class="film-hls" controls playsinline preload="none" poster="../../media/video/hls/youre_the_wave/poster.jpg" data-hls="../../media/video/hls/youre_the_wave/index.m3u8"></video><h3>You\'re the Wave</h3></div><div class="film"><video class="film-hls" controls playsinline preload="none" poster="../../media/video/hls/beyond_the_end/poster.jpg" data-hls="../../media/video/hls/beyond_the_end/index.m3u8"></video><h3>Beyond the End</h3></div></div>'
    stage=stage.replace(old,new)
show_notes='''<div class="editorial-notes"><div class="eye" style="margin-top:42px">show format · open the production notes</div>
<details><summary><span class="dn">01</span><b>The premise: what it is</b><span class="more">open details ↓</span></summary><div class="dc"><p>Construct of Time is a cinematic audiovisual performance built from original music, moving image and live performance. Its proposition is simple: much of life is spent in memory and anticipation, while experience itself can only occur in the present.</p><p>The audience does not need a briefing in neuroscience or philosophy. The argument is carried by duration, rhythm, image, silence and scale.</p></div></details>
<details><summary><span class="dn">02</span><b>How it works</b><span class="more">open details ↓</span></summary><div class="dc"><p>The seven-screen structure turns cinema into architecture. Full-range sound gives the score physical depth; sub-bass is felt before it is analysed. Each chapter changes the conditions of attention: suspension, prediction, repetition, compression, release.</p><p>The performers are not placed in front of the visual world. They occupy it. Image, music and light are authored as one score.</p></div></details>
<details><summary><span class="dn">03</span><b>What it sets out to achieve</b><span class="more">open details ↓</span></summary><div class="dc"><p>The work does not try to prove that time is unreal. It makes the audience notice how unstable lived time already is. A minute can expand, vanish, repeat or refuse to end. The show turns that ordinary fact into a shared physical event.</p></div></details>
<details><summary><span class="dn">04</span><b>The audience experience</b><span class="more">open details ↓</span></summary><div class="dc"><p>The opening removes familiar markers: no immediate beat, no exposition, no spectacle asking to be admired. Expectation is built gradually. At the climax, sound, image and light converge into a single event, then release.</p><p>The arc moves from stillness to pressure to release without confusing intensity with meaning.</p></div></details>
<details><summary><span class="dn">05</span><b>Live performance and touring</b><span class="more">open details ↓</span></summary><div class="dc"><p>The production is designed to scale from black-box presentation to festival stage while preserving the seven-screen visual logic, full-range sound, darkness and architectural light that make the perceptual argument work.</p><p>Engineering, rigging, screen support, ballast, safety systems and venue compliance remain supplier and venue scope.</p></div></details>
<details><summary><span class="dn">06</span><b>The creative authorship</b><span class="more">open details ↓</span></summary><div class="dc"><p>Conceived, written and scored by Tony Funiciello. The project joins electronic composition, moving image, performance, spatial design and research into one authored system. Its visual language stays brutalist, cold and architectural: real materials, restrained light, no decorative futurism.</p></div></details></div>'''
stage=stage.replace('<p class="quote">Its disappearance is part of the work.</p>','<p class="quote">Its disappearance is part of the work.</p>'+show_notes)
if 'video.film-hls[data-hls]' not in stage:
    stage=stage.replace('</body>','''<script src="../../media/lib/hls.min.js"></script><script>(function(){document.querySelectorAll('video.film-hls[data-hls]').forEach(function(v){var src=v.dataset.hls;if(v.canPlayType('application/vnd.apple.mpegurl'))v.src=src;else if(window.Hls&&Hls.isSupported()){var h=new Hls({enableWorker:true});h.loadSource(src);h.attachMedia(v)}})})();</script></body>''')
(V3/'stage'/'index.html').write_text(stage)

# --- installation ---
p=Path('installation/index.html'); inst=rebase(p.read_text())
inst=inst.replace('</style>',split_css+accordion_css+'</style>',1)
inst=inst.replace('The installation is already happening when the visitor arrives and continues after they leave. There is no privileged seat, fixed sequence or single point of view.','The work has already begun before anyone enters and continues after they leave. There is no privileged seat, no master sequence and no single correct view. Arrival becomes an edit point chosen by the visitor.')
inst=inst.replace('You do not watch time unfold. You enter somewhere inside it.','You enter mid-sentence. The work never tells you where the beginning was.')
inst=inst.replace('The same work can contain completely different experiences of <em>duration</em>.','The same measured hour can contain radically different experiences of <em>duration</em>.')
inst=inst.replace('One visitor stays with an image for ten minutes. Another crosses it in thirty seconds. Someone enters while somebody else leaves.','One visitor remains with an image until it changes meaning. Another crosses the same field in seconds. Someone arrives inside an event another person has already left behind. The installation makes those differences visible without forcing them into one timeline.')
install_notes='''<div class="editorial-notes"><div class="eye">installation framework · open the spatial notes</div>
<details><summary><span class="dn">01</span><b>The premise: no fixed beginning</b><span class="more">open details ↓</span></summary><div class="dc"><p>The gallery form removes the stage clock. Visitors arrive at different moments, remain for different lengths of time and assemble their own sequence from the same audiovisual system. The work is continuous; every encounter is partial by design.</p></div></details>
<details><summary><span class="dn">02</span><b>Moving image as material</b><span class="more">open details ↓</span></summary><div class="dc"><p>Moving image is treated as surface, scale and light rather than as a film that must be watched from beginning to end. Fragments can occupy walls, floor and peripheral vision, allowing the image to behave architecturally.</p></div></details>
<details><summary><span class="dn">03</span><b>Spatial sound and anticipation</b><span class="more">open details ↓</span></summary><div class="dc"><p>Sound can announce an event before it is visible, continue after its source disappears, or make distance physically legible. Spatial sound therefore composes anticipation, memory and orientation rather than simply surrounding the visitor.</p></div></details>
<details><summary><span class="dn">04</span><b>Biological time / clock time</b><span class="more">open details ↓</span></summary><div class="dc"><p>The installation keeps measured duration constant while changing the conditions under which it is experienced. Density, repetition, darkness, novelty and waiting become variables. The experiment is not to illustrate time but to change how long the same interval feels.</p></div></details>
<details><summary><span class="dn">05</span><b>Site response</b><span class="more">open details ↓</span></summary><div class="dc"><p>The system responds to architecture rather than concealing it. Corridors produce anticipation. Distance delays arrival. Doorways divide one present from another. Existing surfaces, thresholds and circulation become part of the composition.</p></div></details>
<details><summary><span class="dn">06</span><b>Institutional presentation</b><span class="more">open details ↓</span></summary><div class="dc"><p>The installation is intended for museums, galleries and immersive spaces where darkness, spatial audio and architectural integration can be developed with the venue. Room envelope, projection or screen strategy, sound layout, capacity and circulation remain site-specific technical development.</p></div></details></div>'''
# Append notes inside science section before section VI.
marker='</div></div></section>\n<section class="panel"><div class="sectionbar"><i>VI</i>'
if marker in inst:
    inst=inst.replace(marker,install_notes+'</div></div></section>\n<section class="panel"><div class="sectionbar"><i>VI</i>',1)
(V3/'installation'/'index.html').write_text(inst)
