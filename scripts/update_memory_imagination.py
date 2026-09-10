from pathlib import Path

p = Path('V3/index.html')
s = p.read_text()

s = s.replace('data-label="I &middot; yesterday"', 'data-label="I &middot; memory"', 1)
s = s.replace('<div class="eyebrow reveal">Yesterday</div>', '<div class="eyebrow reveal">Memory</div>', 1)
s = s.replace(
    '<p class="statement reveal d1">Yesterday feels like a place behind us.<br>But try <em>going back.</em></p>\n    <p class="body reveal d2">You can revisit the story, the feeling, the face. But not the event itself. What remains is a trace. A pattern carried forward. So maybe the past is not somewhere we left. Maybe it is something the present keeps rebuilding.</p>',
    '<p class="statement reveal d1">Memory feels like looking back.<br>But it only happens <em>here.</em></p>\n    <p class="body reveal d2">A face. A room. A moment you thought was gone. None of it returns exactly as it was. The mind rebuilds the past from traces, and every time it does, the memory meets the person you are now. Maybe the past is not somewhere behind us. Maybe it survives as something the present keeps making again.</p>',
    1,
)

s = s.replace('data-label="III &middot; tomorrow"', 'data-label="III &middot; imagination"', 1)
s = s.replace('<div class="eyebrow reveal">Tomorrow</div>', '<div class="eyebrow reveal">Imagination</div>', 1)
s = s.replace(
    '<p class="statement reveal d1">Tomorrow has a strong reputation<br>for a place nobody has <em>ever seen.</em></p>\n    <p class="body reveal d2">We plan for it. We fear it. We sacrifice today for it. But the future never arrives as “the future.” When it comes, it comes as this. Another now. So perhaps tomorrow is not a destination. Perhaps it is a possibility being shaped by what we do here.</p>',
    '<p class="statement reveal d1">Imagination can take you anywhere.<br>It just cannot take you <em>out of now.</em></p>\n    <p class="body reveal d2">We rehearse conversations that have not happened. We picture places we have never stood. We build whole futures from possibility. Some become real. Most do not. But every future begins the same way: as an image appearing in the present. What comes next matters. It is simply not here yet.</p>',
    1,
)

marker = '<section class="panel chapter" data-label="IV &middot; the return">'
if marker in s:
    m = s.index(marker)
    start = s.rfind('<div class="chapdiv">', 0, m)
    end = s.index('</section>', m) + len('</section>')
    s = s[:start] + s[end:]

s = s.replace('content:"open details  ↘"', 'content:"open details"')
s = s.replace('content:"close details  ↗"', 'content:"close details"')
css = '\n/* Detail tabs stay horizontal. */\n.find.open .fx .plus,.acc.open .acc-h .plus{transform:none!important}\n'
if '/* Detail tabs stay horizontal. */' not in s:
    s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s)
Path('index.html').write_text(s.replace('../media/', 'media/'))
