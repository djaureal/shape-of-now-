from pathlib import Path

for path, src in [
    (Path('V3/installation/index.html'), '../../media/room-audio.js'),
    (Path('installation/index.html'), '../media/room-audio.js'),
]:
    s=path.read_text()
    tag=f'<script src="{src}"></script>'
    if tag in s:
        continue
    if '</body>' not in s:
        raise SystemExit(f'</body> not found in {path}')
    s=s.replace('</body>', tag+'\n</body>', 1)
    path.write_text(s)
