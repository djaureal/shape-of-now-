from pathlib import Path

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
      <p>His curiosity began long before <em>The Shape of Now</em>. From an early interest in electronics, rhythm and visual culture, through experimental music, punk, industrial sound and electronic production, his practice developed around a simple instinct: use technology not as decoration, but as a way to ask better questions about perception, consciousness and the way we experience reality.</p>
      <p>Born in Caracas and shaped by a life across different cultures, Tony’s trajectory has moved through music, visual art, multimedia, live performance and immersive environments. As DJ Aureal, he has spent decades exploring electronic music as a physical and psychological space — from underground dance music and experimental electronics to cinematic sound and audiovisual performance.</p>
      <p>Alongside his artistic practice, he has continually worked with emerging technologies: digital image-making, interactive systems, immersive media, generative tools, spatial sound and real-time visual environments. Technology becomes part of the thinking itself — a practical way to translate abstract ideas into something an audience can actually see, hear and feel.</p>
      <p><em>The Shape of Now</em> grows directly from that trajectory. It brings together a long-standing fascination with time, memory, anticipation, consciousness and perception, filtered through scientific research and philosophical inquiry, then rebuilt as an audiovisual experience.</p>
      <p>Tony is not interested in illustrating theory. He is interested in turning difficult ideas into experiences the body can understand.</p>
    </div>
    <p class="foot reveal d2" style="margin-left:auto;margin-right:auto;max-width:72ch"><b>The questions often begin in philosophy and science.</b><br>The work begins when those questions can be felt.</p>
  </div>
</section>
'''

MARKER = '<!-- ============ INSTALLATION x NEURO ============ -->'

for path in [Path('V3/index.html'), Path('index.html')]:
    s = path.read_text()
    if 'id="artist"' in s:
        continue
    if MARKER not in s:
        raise SystemExit(f'Marker not found in {path}')
    s = s.replace(MARKER, SECTION + '\n' + MARKER, 1)
    path.write_text(s)
