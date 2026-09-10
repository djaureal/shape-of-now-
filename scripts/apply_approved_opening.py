from pathlib import Path
import re

p = Path('V3/index.html')
s = p.read_text()

# Remove the long prologue and the interlude immediately before Yesterday.
s, n = re.subn(r'<!-- ============ PROLOGUE ============ -->.*?<span id="arg"></span>\s*<section class="panel interlude">.*?</section>', '<span id="arg"></span>', s, count=1, flags=re.S)
if n != 1:
    raise SystemExit('Opening prologue/interlude block not found')

sections = {
'I &middot; yesterday': '''<section class="panel chapter" data-label="I &middot; yesterday">
  <div class="vbg"><video src="../media/video/b1.mp4" data-vid="b1" autoplay muted loop playsinline preload="none"></video></div>
  <div class="container"><div class="col">
    <div class="eyebrow reveal">Yesterday</div>
    <p class="statement reveal d1">Yesterday feels like a place behind us.<br>But try <em>going back.</em></p>
    <p class="body reveal d2">You can revisit the story, the feeling, the face. But not the event itself. What remains is a trace. A pattern carried forward. So maybe the past is not somewhere we left. Maybe it is something the present keeps rebuilding.</p>
  </div></div>
</section>''',
'II &middot; impermanence': '''<section class="panel chapter" data-label="II &middot; impermanence">
  <div class="vbg"><video src="../media/video/d1.mp4" data-vid="d1" autoplay muted loop playsinline preload="none"></video></div>
  <div class="container"><div class="col">
    <div class="eyebrow reveal">Impermanence</div>
    <p class="statement reveal d1">We keep asking life<br>to <em>hold still.</em></p>
    <p class="body reveal d2">This moment. This person. This version of ourselves. But nothing really stands still. Even what looks solid is movement held together for a while. A body changes. A city changes. A memory changes every time it returns. The strange thing is not that things pass. The strange thing is how often we expect them not to.</p>
  </div></div>
</section>''',
'III &middot; tomorrow': '''<section class="panel chapter" data-label="III &middot; tomorrow">
  <div class="vbg"><video src="../media/video/d2.mp4" data-vid="d2" autoplay muted loop playsinline preload="none"></video></div>
  <div class="container"><div class="col">
    <div class="eyebrow reveal">Tomorrow</div>
    <p class="statement reveal d1">Tomorrow has a strong reputation<br>for a place nobody has <em>ever seen.</em></p>
    <p class="body reveal d2">We plan for it. We fear it. We sacrifice today for it. But the future never arrives as “the future.” When it comes, it comes as this. Another now. So perhaps tomorrow is not a destination. Perhaps it is a possibility being shaped by what we do here.</p>
  </div></div>
</section>'''
}
for label, replacement in sections.items():
    pattern = rf'<section class="panel chapter" data-label="{re.escape(label)}">.*?</section>'
    s, n = re.subn(pattern, replacement, s, count=1, flags=re.S)
    if n != 1:
        raise SystemExit(f'Section not found: {label}')

# Remove chapter IV / The Return and its divider.
s, n = re.subn(r'<div class="chapdiv"><span></span><i>IV</i><span></span></div>\s*<section class="panel chapter" data-label="IV &middot; the return">.*?</section>\s*', '', s, count=1, flags=re.S)
if n != 1:
    raise SystemExit('Return section not found')

question = '''<section class="panel tall" id="philosophy">
  <div class="container">
    <div class="sec-head reveal" style="max-width:900px">
      <div class="eyebrow">the question</div>
      <p class="statement">And now we get to<br>the difficult part.</p>
    </div>
    <div class="prose reveal d1">
      <p>Where exactly is now? Not the word. Not the clock. The actual thing.</p>
      <p>There is no single universal beat that the whole cosmos agrees to follow. Speed changes time. Gravity changes time. Even the order of events can depend on where you stand.</p>
      <p>And at the smallest scales, reality is less like a collection of fixed objects and more like a field of possibilities becoming definite through interaction.</p>
      <p>Meanwhile, your own mind is doing something similar. It takes fragments, fills gaps, predicts what comes next, and gives you a world that feels continuous.</p>
      <p>So perhaps “now” is not a tiny slice between past and future. Perhaps it is the meeting place — where memory, possibility, perception, and change all become one experience.</p>
      <p>Not still. Not fixed. Just taking form.</p>
    </div>
    <p class="foot reveal d2"><b>The Shape of Now</b></p>
  </div>
</section>'''
s, n = re.subn(r'<section class="panel tall" id="philosophy">.*?</section>', question, s, count=1, flags=re.S)
if n != 1:
    raise SystemExit('Question section not found')

p.write_text(s)
Path('index.html').write_text(s.replace('../media/', 'media/'))
