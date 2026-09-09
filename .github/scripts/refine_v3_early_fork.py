from pathlib import Path
import re

root = Path('V3/index.html')
s = root.read_text()

css = r'''
/* V3.2 — early cinematic fork */
.chapter,.act{margin-block:clamp(8px,1.2vh,16px)!important}
#installation,#stage-design,#room,#story,#films,#score,#close,section.act{display:none!important}
.dock{display:none!important}body{padding-bottom:0!important}
.nav a[data-s="installation"],.nav a[data-s="stage-design"],.nav a[data-s="room"],.nav a[data-s="story"],.nav a[data-s="films"],.nav a[data-s="acts"],.nav a[data-s="score"]{display:none!important}

#formats{display:block!important;padding:clamp(84px,11vh,126px) 0 0!important;background:var(--void)!important;overflow:hidden!important}
#formats .formats-intro{width:100%;max-width:var(--maxw);padding-inline:var(--gutter);margin:0 auto clamp(52px,7vh,84px)}
#formats .formats-intro .body{max-width:62ch}
.threshold-door{position:relative;min-height:clamp(430px,54svh,680px);display:flex;align-items:flex-end;text-decoration:none;color:inherit;overflow:hidden;border-top:1px solid var(--line-soft)}
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

#research{margin-top:clamp(18px,2vh,28px)!important}
#enquiries{display:flex!important;margin-top:clamp(8px,1.2vh,16px)!important;min-height:78svh!important}
.enquiry-box h2 em{color:var(--filament);font-style:italic}
.enquiry-meta{font-family:var(--mono);font-size:9px;line-height:1.8;letter-spacing:.18em;text-transform:uppercase;color:var(--dim);margin:20px auto 34px;max-width:75ch}

@media(max-width:820px){.door-grid{grid-template-columns:1fr;gap:24px}.threshold-door{min-height:580px}.threshold-door:after,.threshold-door.installation:after{background:linear-gradient(180deg,rgba(4,6,9,.42),rgba(4,6,9,.94) 72%)}}
'''
if '/* V3.2 — early cinematic fork */' not in s:
    s = s.replace('</style>', css + '\n</style>', 1)

formats = '''<section class="panel tall" id="formats">
  <div class="formats-intro reveal">
    <div class="eyebrow">one work · two forms</div>
    <p class="statement">The same investigation.<br>Two ways to <em>enter it.</em></p>
    <p class="body">Construct of Time begins with one question: if memory and anticipation are both experienced now, what exactly is the present we are living inside? From here the work divides by situation, not by idea. One form concentrates attention into a shared event. The other lets duration disperse through a room.</p>
  </div>
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
</section>'''

pattern = re.compile(r'<section\s+class="panel tall"\s+id="formats">.*?</section>', re.S)
if not pattern.search(s):
    raise SystemExit('formats section not found')
s = pattern.sub(formats, s, count=1)

# Replace the shared ending with a concise, specific programming invitation.
enquiries = '''<section class="panel tall" id="enquiries">
  <div class="container enquiry-box">
    <div class="eyebrow reveal">programming · curatorial enquiries</div>
    <h2 class="reveal d1">One work.<br>Two conditions of <em>attention.</em></h2>
    <p class="reveal d2">The live form scales through stage architecture, screen configuration and sound. The installation responds to room, circulation and dwell time. In both cases the technical conversation begins with the space, because the space changes how time is experienced.</p>
    <div class="enquiry-meta reveal d2">live performance · immersive installation · festivals · museums · galleries · cultural institutions</div>
    <div class="enquiry-actions reveal d3">
      <a href="mailto:tony@shufflem.com.au?subject=Construct%20of%20Time%20Programming%20Enquiry">programming enquiry</a>
      <a href="mailto:tony@shufflem.com.au?subject=Construct%20of%20Time%20Presentation%20Deck">request presentation deck</a>
      <a href="mailto:tony@shufflem.com.au?subject=Construct%20of%20Time%20Technical%20Specifications">technical specifications</a>
    </div>
  </div>
</section>'''
q = re.compile(r'<section\s+class="panel tall"\s+id="enquiries">.*?</section>', re.S)
if q.search(s):
    s = q.sub(enquiries, s, count=1)

root.write_text(s)

# Tighten Stage and Installation while retaining the original visual language already applied to V3.
for fn in ['V3/stage/index.html','V3/installation/index.html']:
    p=Path(fn); x=p.read_text()
    add='''\n/* V3.2 shared rhythm */\n.panel{margin-block:clamp(8px,1.2vh,16px)!important}\n.hero{margin-top:0!important}\n.bg video{opacity:.88!important}\n'''
    if '/* V3.2 shared rhythm */' not in x:
        x=x.replace('</style>',add+'\n</style>',1)
    p.write_text(x)
