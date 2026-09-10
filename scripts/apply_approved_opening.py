from pathlib import Path

p = Path('V3/index.html')
s = p.read_text()

old = '''<!-- ============ PROLOGUE ============ -->
<section class="panel tall" id="prologue">
  <div class="container"><div class="col" style="max-width:760px">
    <div class="eyebrow reveal">prologue &middot; before anything else</div>
    <p class="statement reveal d1 prologue-title"><span>We spend so much of our lives</span><br><span>somewhere <em>else</em>.</span></p>
    <div class="prose reveal d2">
      <p>We remember. We imagine. We carry things that happened. We worry about things that have not happened. We plan. We regret. We hope. We wait.</p>
      <p>This is not a flaw. It is most of what a mind does. Scroll slowly, and let the sound run.</p>
    </div>
  </div></div>
</section>

<!-- ============ ARGUMENT ============ -->
<span id="arg"></span>
<section class="panel interlude">
  <div class="container"><div class="col reveal"><p class="statement tidy-two"><span class="keep-line">Between what happened and what might happen,</span><span class="keep-line">we call ourselves <em>present</em>.</span></p><div class="rule"></div></div></div>
</section>'''
if old not in s:
    raise SystemExit('Old prologue block not found')
s = s.replace(old, '<span id="arg"></span>', 1)

pairs = [
('''    <p class="statement reveal d1">You can remember yesterday.<br>You cannot <em>return</em> to it.</p>
    <p class="body reveal d2">You can describe it. You can still feel what it changed in you. But the event itself is no longer where experience is happening. What remains is <b>memory</b>: vivid, real, yours.</p>''',
'''    <p class="statement reveal d1">Yesterday feels like a place behind us.<br>But try <em>going back.</em></p>
    <p class="body reveal d2">You can revisit the story, the feeling, the face. But not the event itself. What remains is a trace. A pattern carried forward. So maybe the past is not somewhere we left. Maybe it is something the present keeps rebuilding.</p>'''),
('''    <p class="statement reveal d1">A moment does not have to remain<br>to have <em>mattered</em>.</p>
    <p class="body reveal d2">A person can leave and still change the direction of a life. An experience can end without losing its meaning. Yesterday can shape you without being somewhere you can go. <b>Letting go is not the same as losing.</b></p>''',
'''    <p class="statement reveal d1">We keep asking life<br>to <em>hold still.</em></p>
    <p class="body reveal d2">This moment. This person. This version of ourselves. But nothing really stands still. Even what looks solid is movement held together for a while. A body changes. A city changes. A memory changes every time it returns. The strange thing is not that things pass. The strange thing is how often we expect them not to.</p>'''),
('''    <p class="statement reveal d1">Tomorrow is somewhere you can<br>plan for, but never <em>visit</em>.</p>
    <p class="body reveal d2">We imagine. We plan. We hope, fear, rehearse. It is an extraordinary ability, and we need it. But notice something quiet underneath: every future you imagine is imagined <b>now</b>.</p>''',
'''    <p class="statement reveal d1">Tomorrow has a strong reputation<br>for a place nobody has <em>ever seen.</em></p>
    <p class="body reveal d2">We plan for it. We fear it. We sacrifice today for it. But the future never arrives as “the future.” When it comes, it comes as this. Another now. So perhaps tomorrow is not a destination. Perhaps it is a possibility being shaped by what we do here.</p>''')]
for a, b in pairs:
    if a not in s:
        raise SystemExit('Chapter copy target not found')
    s = s.replace(a, b, 1)

iv = '''<div class="chapdiv"><span></span><i>IV</i><span></span></div>
<section class="panel chapter" data-label="IV &middot; the return">
  <div class="vbg"><video data-vid="c2" muted loop playsinline preload="none"></video></div>
  <div class="container"><div class="col">
    <div class="eyebrow reveal">The return</div>
    <p class="statement reveal d1">Everything keeps returning<br>to the same <em>place</em>.</p>
    <p class="body reveal d2">Every memory is remembered now. Every expectation is felt now. Regret happens now. Hope happens now. Wherever the mind travels, it travels from <b>here</b>.</p>
  </div></div>
</section>

'''
if iv not in s:
    raise SystemExit('Return block not found')
s = s.replace(iv, '', 1)

oldq = '''<section class="panel tall" id="philosophy">
  <div class="container">
    <div class="sec-head reveal" style="max-width:900px">
      <div class="eyebrow">the question</div>
      <p class="statement">So what, exactly,<br>is <em>now</em>?</p>
    </div>
    <div class="prose reveal d1">
      <p>Try to hold it. Try to find its edge. By the time you say the word, the moment you meant has already changed. The present will not stand still long enough to be pointed at.</p>
      <p>And yet: the past happened. The future matters. Memory is real, as a present experience. Anticipation is real, as a present experience. Everything you have ever lived, you have lived from here. Perhaps now is not a moment at all. Perhaps it is a shape, <b>still forming</b>.</p>
    </div>
    <p class="foot reveal d2"><b>the argument</b>&nbsp;&nbsp;Presentism holds that only the now exists; eternalism, that all moments exist at once. This work lives in the tension between them. Staging a present that is the only thing real, and revealing it to be authored by a past and a future that are not.</p>
  </div>
</section>'''
newq = '''<section class="panel tall" id="philosophy">
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
if oldq not in s:
    raise SystemExit('Question block not found')
s = s.replace(oldq, newq, 1)

s = s.replace('<video data-vid="b1" muted loop playsinline preload="none"></video>', '<video src="../media/video/b1.mp4" data-vid="b1" autoplay muted loop playsinline preload="none"></video>', 1)
s = s.replace('<video data-vid="d1" muted loop playsinline preload="none"></video>', '<video src="../media/video/d1.mp4" data-vid="d1" autoplay muted loop playsinline preload="none"></video>', 1)
s = s.replace('<video data-vid="d2" muted loop playsinline preload="none"></video>', '<video src="../media/video/d2.mp4" data-vid="d2" autoplay muted loop playsinline preload="none"></video>', 1)

p.write_text(s)
Path('index.html').write_text(s.replace('../media/', 'media/'))
