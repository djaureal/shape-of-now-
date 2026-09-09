from pathlib import Path

files=[Path('V3/index.html'),Path('V3/stage/index.html'),Path('V3/installation/index.html')]

# Shared rule: display headings should not accidentally become 3 lines on desktop.
css='''\n/* V3 typography discipline — intentional one/two-line display headings */\n@media(min-width:821px){\n  .tidy-two{max-width:none!important;width:100%!important}\n  .tidy-two .keep-line{display:block;white-space:nowrap}\n  .formats-intro .statement{max-width:1100px}\n}\n@media(max-width:820px){.tidy-two .keep-line{white-space:normal}}\n'''

for p in files:
    if not p.exists():
        continue
    s=p.read_text()
    if 'V3 typography discipline' not in s:
        s=s.replace('</style>',css+'\n</style>',1)
    p.write_text(s)

# Fix the specific shared interlude so its two intended phrases remain two lines on desktop.
p=Path('V3/index.html')
s=p.read_text()
old='<p class="statement">Between what happened and what might happen,<br>we call ourselves <em>present</em>.</p>'
new='<p class="statement tidy-two"><span class="keep-line">Between what happened and what might happen,</span><span class="keep-line">we call ourselves <em>present</em>.</span></p>'
if old in s:
    s=s.replace(old,new,1)
p.write_text(s)
