from pathlib import Path
import re

SECTION = '''

<!-- ============ ABOUT THE ARTIST ============ -->
<section class="panel tall" id="artist">
  <div class="container">
    <div class="sec-head reveal" style="margin-left:auto;margin-right:auto;text-align:center;max-width:920px">
      <div class="eyebrow" style="justify-content:center">about the artist</div>
      <p class="statement">The work comes from a long conversation between<br><em>philosophy, science, music and technology.</em></p>
    </div>
    <div class="prose reveal d1" style="margin-left:auto;margin-right:auto;max-width:72ch">
      <p><b>Tony Funiciello</b> is an audiovisual artist, producer, DJ and creative technologist whose work sits between philosophy, science, music and moving image.</p>
      <details class="artist-more">
        <summary><span class="artist-open">open details</span><span class="artist-close">close details</span></summary>
        <div class="artist-more-body">
          <p>His curiosity began long before <em>The Shape of Now</em>. From an early interest in electronics, rhythm and visual culture, through experimental music, punk, industrial sound and electronic production, his practice developed around a simple instinct: use technology not as decoration, but as a way to ask better questions about perception, consciousness and the way we experience reality.</p>
          <p>Born in Caracas and shaped by a life across different cultures, Tony’s trajectory has moved through music, visual art, multimedia, live performance and immersive environments. As DJ Aureal, he has spent decades exploring electronic music as a physical and psychological space — from underground dance music and experimental electronics to cinematic sound and audiovisual performance.</p>
          <p>Alongside his artistic practice, he has continually worked with emerging technologies: digital image-making, interactive systems, immersive media, generative tools, spatial sound and real-time visual environments. Technology becomes part of the thinking itself — a practical way to translate abstract ideas into something an audience can actually see, hear and feel.</p>
          <p><em>The Shape of Now</em> grows directly from that trajectory. It brings together a long-standing fascination with time, memory, anticipation, consciousness and perception, filtered through scientific research and philosophical inquiry, then rebuilt as an audiovisual experience.</p>
          <p>Tony is not interested in illustrating theory. He is interested in turning difficult ideas into experiences the body can understand.</p>
        </div>
      </details>
    </div>
    <p class="foot reveal d2" style="margin-left:auto;margin-right:auto;max-width:72ch"><b>The questions often begin in philosophy and science.</b><br>The work begins when those questions can be felt.</p>
  </div>
</section>
'''

CSS = '''
/* About the Artist — progressive disclosure */
#artist .artist-more{margin-top:24px;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:0}
#artist .artist-more summary{list-style:none;cursor:pointer;padding:16px 0;font-family:var(--mono);font-size:9.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--filament);text-align:center}
#artist .artist-more summary::-webkit-details-marker{display:none}
#artist .artist-close{display:none}
#artist .artist-more[open] .artist-open{display:none}
#artist .artist-more[open] .artist-close{display:inline}
#artist .artist-more-body{padding:0 0 22px}
#artist .artist-more-body p:first-child{margin-top:4px}
'''

MARKER = '<!-- ============ INSTALLATION x NEURO ============ -->'
pattern = re.compile(r'<!-- ============ ABOUT THE ARTIST ============ -->.*?(?=' + re.escape(MARKER) + r')', re.S)

for path in [Path('V3/index.html'), Path('index.html')]:
    s = path.read_text()
    if pattern.search(s):
        s = pattern.sub(SECTION + '\n', s, count=1)
    else:
        if MARKER not in s:
            raise SystemExit(f'Marker not found in {path}')
        s = s.replace(MARKER, SECTION + '\n' + MARKER, 1)
    if '#artist .artist-more{' not in s:
        if '</style>' not in s:
            raise SystemExit(f'</style> not found in {path}')
        s = s.replace('</style>', CSS + '\n</style>', 1)
    path.write_text(s)
