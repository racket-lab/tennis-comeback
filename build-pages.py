"""Erzeugt docs/index.html (für GitHub Pages) aus index.html.

index.html ist ohne <html>/<head>-Gerüst geschrieben, damit es auch als
claude.ai-Artifact funktioniert. GitHub Pages braucht ein vollständiges
HTML-Dokument, deshalb wird hier das Gerüst ergänzt.

Aufruf:  python build-pages.py
"""
from pathlib import Path

root = Path(__file__).parent
src = (root / "index.html").read_text(encoding="utf-8")
src = src.replace('<meta charset="utf-8">\n', "", 1)

page = (
    "<!doctype html>\n"
    '<html lang="de">\n<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '<meta name="theme-color" content="#F1F4F2">\n'
    "<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}"
    "body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n"
    "</head>\n<body>\n" + src + "\n</body>\n</html>\n"
)

out = root / "docs" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(page, encoding="utf-8", newline="\n")
print("geschrieben:", out)
