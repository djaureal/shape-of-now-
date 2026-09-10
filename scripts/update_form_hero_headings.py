from pathlib import Path

updates = [
    (
        Path('V3/stage/index.html'),
        '<h1 class="h1">Many people.<br>One shared <em>present.</em></h1>',
        '<h1 class="h1">Time gathers.<br><em>We arrive in the same moment.</em></h1>'
    ),
    (
        Path('V3/installation/index.html'),
        '<h1 class="h1">One work.<br>Many <em>presents.</em></h1>',
        '<h1 class="h1">Time disperses.<br><em>Each person finds their own moment.</em></h1>'
    ),
]

for path, old, new in updates:
    s = path.read_text()
    if old not in s:
        raise SystemExit(f'Expected hero heading not found in {path}')
    path.write_text(s.replace(old, new, 1))

Path('stage/index.html').write_text(Path('V3/stage/index.html').read_text().replace('../../media/', '../media/'))
Path('installation/index.html').write_text(Path('V3/installation/index.html').read_text().replace('../../media/', '../media/'))
