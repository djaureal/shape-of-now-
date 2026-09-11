from pathlib import Path

FILES = [
    Path('V3/stage/index.html'),
    Path('V3/installation/index.html'),
    Path('stage/index.html'),
    Path('installation/index.html'),
]

CSS = r'''

/* Shared programming footer — Live + Installation */
.form-footer{
  position:relative;
  z-index:4;
  padding:clamp(54px,7vh,82px) var(--g,clamp(22px,6vw,104px)) clamp(64px,8vh,96px);
  border-top:1px solid rgba(207,230,239,.10);
  text-align:center;
  background:linear-gradient(180deg,rgba(5,7,10,.12),rgba(5,7,10,.72));
}
.form-footer-meta{
  max-width:760px;
  margin:0 auto 30px;
  font:8.5px/2 var(--mo,"IBM Plex Mono",monospace);
  letter-spacing:.30em;
  text-transform:uppercase;
  color:var(--d,#7b858b);
}
.form-footer-actions{
  display:flex;
  justify-content:center;
  flex-wrap:wrap;
  gap:11px;
}
.form-footer-actions a{
  min-width:154px;
  padding:14px 18px;
  border:1px solid rgba(207,230,239,.22);
  color:var(--i,#b8c2c8);
  text-decoration:none;
  font:8px var(--mo,"IBM Plex Mono",monospace);
  letter-spacing:.20em;
  text-transform:uppercase;
  transition:border-color .3s,color .3s,background .3s;
}
.form-footer-actions a:hover{
  color:var(--s,#eef4f7);
  border-color:rgba(207,230,239,.48);
  background:rgba(207,230,239,.035);
}
@media(max-width:700px){
  .form-footer{padding-left:22px;padding-right:22px}
  .form-footer-meta{font-size:7.5px;letter-spacing:.22em}
  .form-footer-actions{flex-direction:column;align-items:stretch;max-width:360px;margin:auto}
  .form-footer-actions a{width:100%}
}
'''

FOOTER = r'''
<footer class="form-footer" aria-label="Programming and presentation enquiries">
  <div class="form-footer-meta">live performance · immersive installation · festivals · museums · galleries · cultural institutions</div>
  <div class="form-footer-actions">
    <a href="mailto:tony@shufflem.com.au?subject=The%20Shape%20of%20Now%20Programming%20Enquiry">programming enquiry</a>
    <a href="mailto:tony@shufflem.com.au?subject=The%20Shape%20of%20Now%20Presentation%20Deck">request presentation deck</a>
    <a href="mailto:tony@shufflem.com.au?subject=The%20Shape%20of%20Now%20Technical%20Specifications">technical specifications</a>
  </div>
</footer>
'''

for path in FILES:
    s = path.read_text()
    if '.form-footer{' not in s:
        if '</style>' not in s:
            raise SystemExit(f'</style> not found in {path}')
        s = s.replace('</style>', CSS + '\n</style>', 1)
    if 'aria-label="Programming and presentation enquiries"' not in s:
        marker = '<div class="dock"'
        if marker in s:
            s = s.replace(marker, FOOTER + '\n' + marker, 1)
        elif '</body>' in s:
            s = s.replace('</body>', FOOTER + '\n</body>', 1)
        else:
            raise SystemExit(f'footer insertion point not found in {path}')
    path.write_text(s)
