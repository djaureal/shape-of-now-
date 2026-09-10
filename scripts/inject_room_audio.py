from pathlib import Path

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
    path.write_text(s)
