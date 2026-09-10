from pathlib import Path
import re

CSS = r'''
/* Hero hierarchy — exactly two lines: primary larger, secondary quieter. */
.hero .h1.hero-two-line{
  max-width:none!important;
  width:100%!important;
  line-height:1!important;
}
.hero .hero-primary,
.hero .hero-secondary{
  display:block;
  white-space:nowrap;
}
.hero .hero-primary{
  font-size:clamp(54px,8vw,110px);
  line-height:.88;
  font-style:normal;
  color:var(--s);
}
.hero .hero-secondary{
  margin-top:clamp(12px,1.6vh,20px);
  font-size:clamp(28px,4.5vw,58px);
  line-height:1.02;
  font-style:italic;
  color:var(--f);
}
@media(max-width:780px){
  .hero .hero-primary{font-size:clamp(44px,12vw,68px)}
  .hero .hero-secondary{font-size:clamp(22px,6.2vw,34px);margin-top:12px}
}
'''

updates = [
    (
        Path('V3/stage/index.html'),
        '<h1 class="h1 hero-two-line"><span class="hero-primary">Time gathers.</span><span class="hero-secondary">We arrive in the same moment.</span></h1>'
    ),
    (
        Path('V3/installation/index.html'),
        '<h1 class="h1 hero-two-line"><span class="hero-primary">Time disperses.</span><span class="hero-secondary">The present becomes personal.</span></h1>'
    ),
]

for path, new_heading in updates:
    s = path.read_text()
    s, count = re.subn(r'<h1 class="h1(?: hero-two-line)?">.*?</h1>', new_heading, s, count=1, flags=re.S)
    if count != 1:
        raise SystemExit(f'Hero heading not found in {path}')
    if '/* Hero hierarchy — exactly two lines:' not in s:
        s = s.replace('</style>', CSS + '\n</style>', 1)
    path.write_text(s)

Path('stage/index.html').write_text(Path('V3/stage/index.html').read_text().replace('../../media/', '../media/'))
Path('installation/index.html').write_text(Path('V3/installation/index.html').read_text().replace('../../media/', '../media/'))
