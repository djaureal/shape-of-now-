from pathlib import Path

p = Path('V3/index.html')
s = p.read_text()

old_css = '''.threshold-door{position:relative;min-height:clamp(430px,54svh,680px);display:flex;align-items:flex-end;text-decoration:none;color:inherit;overflow:hidden;border-top:1px solid var(--line-soft)}
.threshold-door:last-of-type{border-bottom:1px solid var(--line-soft)}
.threshold-door video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.68;filter:grayscale(.42) contrast(1.08) brightness(.48);transform:scale(1.015);transition:transform 1.6s cubic-bezier(.2,.7,.2,1),opacity 1s ease}
.threshold-door:hover video{transform:scale(1.045);opacity:.78}
.threshold-door:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(4,6,9,.96) 0%,rgba(4,6,9,.82) 38%,rgba(4,6,9,.42) 72%,rgba(4,6,9,.62) 100%)}
.threshold-door.installation:after{background:linear-gradient(90deg,rgba(4,6,9,.92) 0%,rgba(4,6,9,.68) 42%,rgba(4,6,9,.42) 70%,rgba(4,6,9,.78) 100%)}
.door-content{position:relative;z-index:2;width:100%;max-width:var(--maxw);margin:0 auto;padding:clamp(62px,9vh,104px) var(--gutter)}
.door-index{font-family:var(--mono);font-size:9px;letter-spacing:.3em;text-transform:uppercase;color:var(--filament);margin-bottom:22px}
.door-grid{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(300px,.7fr);gap:clamp(34px,8vw,120px);align-items:end}
.door-grid h3{font-family:var(--serif);font-weight:300;font-size:clamp(54px,8vw,118px);line-height:.82;letter-spacing:-.015em}
.door-grid h3 em{font-style:italic;color:var(--filament)}
.door-copy{max-width:49ch;font-size:clamp(14px,1.25vw,16px);line-height:1.78;color:var(--ink)}
.door-copy b{color:var(--signal);font-weight:400}
.door-meta{font-family:var(--mono);font-size:8.5px;letter-spacing:.19em;text-transform:uppercase;color:var(--dim);margin-bottom:16px}
.door-enter{display:inline-block;margin-top:28px;font-family:var(--mono);font-size:9px;letter-spacing:.22em;text-transform:uppercase;color:var(--signal);border-bottom:1px solid var(--line);padding-bottom:8px;transition:border-color .3s,letter-spacing .3s}
.threshold-door:hover .door-enter{border-color:var(--filament);letter-spacing:.26em}
.fork-divider{width:min(560px,72vw);display:grid;grid-template-columns:1fr auto 1fr;gap:20px;align-items:center;margin:clamp(20px,3vh,34px) auto}
.fork-divider span{height:1px}.fork-divider span:first-child{background:linear-gradient(90deg,transparent,var(--glow))}.fork-divider span:last-child{background:linear-gradient(90deg,var(--glow),transparent)}
.fork-divider i{font-family:var(--serif);font-size:23px;font-style:italic;color:var(--filament);opacity:.8}
'''

new_css = '''.fork-pair{display:grid;grid-template-columns:minmax(0,1fr) 76px minmax(0,1fr);align-items:stretch;border-top:1px solid var(--line-soft);border-bottom:1px solid var(--line-soft)}
.threshold-door{position:relative;min-height:clamp(540px,66svh,760px);display:flex;align-items:flex-end;text-decoration:none;color:inherit;overflow:hidden}
.threshold-door.live{border-right:1px solid rgba(207,230,239,.08)}
.threshold-door.installation{border-left:1px solid rgba(207,230,239,.08)}
.threshold-door video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.68;filter:grayscale(.42) contrast(1.08) brightness(.48);transform:scale(1.015);transition:transform 1.6s cubic-bezier(.2,.7,.2,1),opacity 1s ease}
.threshold-door:hover video{transform:scale(1.045);opacity:.79}
.threshold-door:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(4,6,9,.30) 0%,rgba(4,6,9,.56) 42%,rgba(4,6,9,.94) 100%)}
.threshold-door.installation:after{background:linear-gradient(180deg,rgba(4,6,9,.24) 0%,rgba(4,6,9,.52) 44%,rgba(4,6,9,.94) 100%)}
.door-content{position:relative;z-index:2;width:100%;padding:clamp(46px,7vh,74px) clamp(28px,4.3vw,70px)}
.door-index{font-family:var(--mono);font-size:8.5px;letter-spacing:.28em;text-transform:uppercase;color:var(--filament);margin-bottom:20px}
.door-grid{display:block}
.door-grid h3{font-family:var(--serif);font-weight:300;font-size:clamp(48px,5.7vw,86px);line-height:.84;letter-spacing:-.015em;margin-bottom:32px}
.door-grid h3 em{font-style:italic;color:var(--filament)}
.door-copy{max-width:43ch;font-size:clamp(13.5px,1.05vw,15.5px);line-height:1.76;color:var(--ink)}
.door-copy b{color:var(--signal);font-weight:400}
.door-meta{font-family:var(--mono);font-size:8px;letter-spacing:.17em;text-transform:uppercase;color:var(--dim);margin-bottom:14px}
.door-enter{display:inline-block;margin-top:25px;font-family:var(--mono);font-size:8.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--signal);border-bottom:1px solid var(--line);padding-bottom:8px;transition:border-color .3s,letter-spacing .3s}
.threshold-door:hover .door-enter{border-color:var(--filament);letter-spacing:.24em}
.fork-divider{width:auto;margin:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;background:var(--void)}
.fork-divider span{width:1px;min-height:86px;flex:1;background:linear-gradient(180deg,transparent,var(--glow))}
.fork-divider span:last-child{background:linear-gradient(180deg,var(--glow),transparent)}
.fork-divider i{font-family:var(--serif);font-size:23px;font-style:italic;color:var(--filament);opacity:.82;line-height:1}
'''

if old_css not in s:
    raise SystemExit('expected fork CSS block not found')
s = s.replace(old_css, new_css, 1)

old_html = '''  <a class="threshold-door live" href="./stage/" aria-label="Enter Construct of Time Live Performance">
    <video src="../media/video/c1.mp4" muted autoplay loop playsinline preload="metadata"></video>
    <div class="door-content"><div class="door-index">01 · live performance</div><div class="door-grid">
      <h3>Live<br><em>Performance</em></h3>
      <div class="door-copy"><div class="door-meta">festivals · theatres · audiovisual programs</div><p>Three performers, seven screens, original electronic music and architectural light operate as one score. The audience is not asked to observe an idea about time. Its own attention becomes the material.</p><span class="door-enter">enter the live performance →</span></div>
    </div></div>
  </a>
  <div class="fork-divider" aria-hidden="true"><span></span><i>or</i><span></span></div>
  <a class="threshold-door installation" href="./installation/" aria-label="Enter Construct of Time Immersive Installation">
    <video src="../media/installation/field.mp4" muted autoplay loop playsinline preload="metadata"></video>
    <div class="door-content"><div class="door-index">02 · immersive installation</div><div class="door-grid">
      <h3>Immersive<br><em>Installation</em></h3>
      <div class="door-copy"><div class="door-meta">museums · galleries · site-responsive spaces</div><p>No fixed beginning. No privileged viewpoint. Moving image, spatial sound, darkness and architecture create a field in which different visitors can inhabit different durations at the same time.</p><span class="door-enter">enter the installation →</span></div>
    </div></div>
  </a>'''

new_html = '''  <div class="fork-pair">
    <a class="threshold-door live" href="./stage/" aria-label="Enter Construct of Time Live Performance">
      <video src="../media/video/c1.mp4" muted autoplay loop playsinline preload="metadata"></video>
      <div class="door-content"><div class="door-index">01 · live performance</div><div class="door-grid">
        <h3>Live<br><em>Performance</em></h3>
        <div class="door-copy"><div class="door-meta">festivals · theatres · audiovisual programs</div><p>Three performers, seven screens, original electronic music and architectural light operate as one score. The audience is not asked to observe an idea about time. Its own attention becomes the material.</p><span class="door-enter">enter the live performance →</span></div>
      </div></div>
    </a>
    <div class="fork-divider" aria-hidden="true"><span></span><i>or</i><span></span></div>
    <a class="threshold-door installation" href="./installation/" aria-label="Enter Construct of Time Immersive Installation">
      <video src="../media/installation/field.mp4" muted autoplay loop playsinline preload="metadata"></video>
      <div class="door-content"><div class="door-index">02 · immersive installation</div><div class="door-grid">
        <h3>Immersive<br><em>Installation</em></h3>
        <div class="door-copy"><div class="door-meta">museums · galleries · site-responsive spaces</div><p>No fixed beginning. No privileged viewpoint. Moving image, spatial sound, darkness and architecture create a field in which different visitors can inhabit different durations at the same time.</p><span class="door-enter">enter the installation →</span></div>
      </div></div>
    </a>
  </div>'''

if old_html not in s:
    raise SystemExit('expected fork HTML not found')
s = s.replace(old_html, new_html, 1)

old_media = '''@media(max-width:820px){.door-grid{grid-template-columns:1fr;gap:24px}.threshold-door{min-height:580px}.threshold-door:after,.threshold-door.installation:after{background:linear-gradient(180deg,rgba(4,6,9,.42),rgba(4,6,9,.94) 72%)}}'''
new_media = '''@media(max-width:820px){.fork-pair{grid-template-columns:1fr;border-top:1px solid var(--line-soft);border-bottom:1px solid var(--line-soft)}.threshold-door{min-height:580px}.threshold-door.live,.threshold-door.installation{border-left:0;border-right:0}.fork-divider{width:min(560px,72vw);height:86px;margin:0 auto;display:grid;grid-template-columns:1fr auto 1fr;gap:20px;align-items:center;background:var(--void)}.fork-divider span{width:auto;height:1px;min-height:0;background:linear-gradient(90deg,transparent,var(--glow))}.fork-divider span:last-child{background:linear-gradient(90deg,var(--glow),transparent)}.door-content{padding:54px 24px}.door-grid h3{font-size:clamp(50px,14vw,78px)}.threshold-door:after,.threshold-door.installation:after{background:linear-gradient(180deg,rgba(4,6,9,.34),rgba(4,6,9,.94) 72%)}}'''
if old_media not in s:
    raise SystemExit('expected fork mobile CSS not found')
s = s.replace(old_media, new_media, 1)

p.write_text(s)
