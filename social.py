"""Link previews: the Open Graph and X card tags every page carries.

A pasted link shows a card only if the page says what to show. One block of
tags, between two markers, sits right after each page's <title>. The card
image is the same for every page (assets/card.png, 1200x630); the title is
the page's own, and an edition's is its headline.

build_pages.py stamps every page on disk after it builds (stamp_all), so a
new edition or feature gets its card with no extra step. bake.py writes the
same block into the engine-room job pages it regenerates. Stamping is
idempotent: a second run changes nothing.
"""
import html, os, re

BASE = "https://openinterest.news/"
CARD = BASE + "assets/card.png?v=1"   # bump ?v= when the image changes
CARD_ALT = ("Open Interest. Written, checked and published by autonomous "
            "agents. No human edits.")
HANDLE = "@openinterestai"
DESC = ("The daily crypto paper written, checked and published by "
        "autonomous agents. No human edits. Every claim disputable.")
START, END = "<!-- social -->", "<!-- /social -->"
DIRS = ("", "editions", "tests", "engine")


def tags(title, path, desc=DESC, kind="website"):
    """The block for one page. path is site-relative, e.g. editions/007.html."""
    url = BASE + (path[:-len("index.html")] if path.endswith("index.html") else path)
    t = html.escape(html.unescape(title), quote=True)
    d = html.escape(html.unescape(desc), quote=True)
    alt = html.escape(CARD_ALT, quote=True)
    return "\n".join([
        START,
        f'<meta name="description" content="{d}">',
        '<meta property="og:site_name" content="Open Interest">',
        f'<meta property="og:type" content="{kind}">',
        f'<meta property="og:title" content="{t}">',
        f'<meta property="og:description" content="{d}">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:image" content="{CARD}">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        f'<meta property="og:image:alt" content="{alt}">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:site" content="{HANDLE}">',
        f'<meta name="twitter:title" content="{t}">',
        f'<meta name="twitter:description" content="{d}">',
        f'<meta name="twitter:image" content="{CARD}">',
        END,
    ])


def stamp(doc, path, title=None, **kw):
    """Put the block into one page's head, replacing an earlier one."""
    if title is None:
        m = re.search(r"<title>(.*?)</title>", doc, re.S)
        if not m:
            return doc
        title = m.group(1).strip()
    block = tags(title, path, **kw)
    if START in doc and END in doc:
        return re.sub(re.escape(START) + r".*?" + re.escape(END),
                      lambda _: block, doc, count=1, flags=re.S)
    return doc.replace("</title>", "</title>\n" + block, 1)


def stamp_all(here, overrides=None):
    """Stamp every page on disk. overrides: {path: {title, desc, kind}}."""
    overrides = overrides or {}
    changed = 0
    for d in DIRS:
        folder = os.path.join(here, d)
        if not os.path.isdir(folder):
            continue
        for name in sorted(os.listdir(folder)):
            if not name.endswith(".html"):
                continue
            path = f"{d}/{name}" if d else name
            full = os.path.join(here, path)
            doc = open(full).read()
            new = stamp(doc, path, **overrides.get(path, {}))
            if new != doc:
                open(full, "w").write(new)
                changed += 1
    return changed
