from pathlib import Path
import re

for path, src in [
    (Path('V3/installation/index.html'), '../../media/room-audio.js'),
    (Path('installation/index.html'), '../media/room-audio.js'),
]:
    s=path.read_text()
    tag=f'<script src="{src}"></script>'
    if tag not in s:
        if '</body>' not in s:
            raise SystemExit(f'</body> not found in {path}')
        s=s.replace('</body>', tag+'\n</body>', 1)

    # Keep the visual Hz phases on screen long enough to match the audio.
    # 24s total cycle preserves the existing theta/alpha/beta/gamma proportions.
    s=s.replace('const ts=R.loopT/1000, lt=(ts%15)/15;', 'const ts=R.loopT/1000, lt=(ts%24)/24;')

    # SHOW and BONES are legacy room controls with no useful effect in the current build.
    # Hide them without removing their DOM nodes so the existing room script remains untouched.
    hide_css='\n/* Current 3D room controls — hide inactive legacy buttons. */\n#btnShow,#btnBones{display:none!important}\n'
    if '#btnShow,#btnBones{display:none!important}' not in s:
        s=s.replace('</style>', hide_css+'\n</style>', 1)

    # Remove the redundant Duration / Calm-Open / Compression-Pulse section.
    s, removed = re.subn(
        r'\n*<section class="panel"><div class="sectionbar"><i>IV</i><span></span></div><div class="bg"><video src="[^\"]*/duration\.mp4".*?</section>\n*',
        '\n',
        s,
        count=1,
        flags=re.S,
    )

    # Renumber the remaining top-level Installation sections after removal.
    s=s.replace('<div class="sectionbar"><i>V</i><span></span></div>', '<div class="sectionbar"><i>IV</i><span></span></div>', 1)
    s=s.replace('<div class="sectionbar"><i>VI</i><span></span></div>', '<div class="sectionbar"><i>V</i><span></span></div>', 1)
    s=s.replace('<div class="sectionbar"><i>VII</i><span></span></div>', '<div class="sectionbar"><i>VI</i><span></span></div>', 1)

    path.write_text(s)
