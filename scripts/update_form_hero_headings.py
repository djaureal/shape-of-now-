from pathlib import Path
import re

updates = [
    (Path('V3/stage/index.html'), '<h1 class="h1">Time gathers.<br>We arrive in the same <em>moment.</em></h1>'),
    (Path('V3/installation/index.html'), '<h1 class="h1">Time disperses.<br>The present becomes <em>personal.</em></h1>'),
]

for path, new_heading in updates:
    s = path.read_text()
    s2, count = re.subn(r'<h1 class="h1">.*?</h1>', new_heading, s, count=1, flags=re.S)
    if count != 1:
        raise SystemExit(f'Hero heading not found in {path}')
    path.write_text(s2)

Path('stage/index.html').write_text(Path('V3/stage/index.html').read_text().replace('../../media/', '../media/'))
Path('installation/index.html').write_text(Path('V3/installation/index.html').read_text().replace('../../media/', '../media/'))
