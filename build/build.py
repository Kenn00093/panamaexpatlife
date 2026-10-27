"""Builds PanamaExpatLife.com into ../site as plain static HTML.

No JavaScript is used anywhere: every word is in the HTML that crawlers and AI
answer engines download. Run:  python3 build/build.py
"""

import html
import json
import shutil
from pathlib import Path

from config import (KIT_FORM_ID, LANG, LAST_CHECKED, LAST_CHECKED_HUMAN, NAV,
                    PANAMA_PROPERTIES_URL, SITE_NAME, SITE_TAGLINE, SITE_URL)
from content import CHECKLIST, PAGES

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site"
STATIC = ROOT / "build" / "static"

PAGE_BY_SLUG = {p["slug"]: p for p in PAGES}

import hashlib
CSS_VERSION = hashlib.md5((STATIC / "style.css").read_bytes()).hexdigest()[:8]


def text(s):
    """Plain text (entities decoded, tags stripped) for JSON-LD and llms.txt."""
    import re
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def ld(obj):
    return ('<script type="application/ld+json">'
            + json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
            + "</script>")


ORG = {
    "@type": "Organization",
    "@id": SITE_URL + "/#organization",
    "name": SITE_NAME,
    "url": SITE_URL + "/",
    "logo": SITE_URL + "/logo.png",
    "description": SITE_TAGLINE,
    "areaServed": {"@type": "Country", "name": "Panama"},
}
WEBSITE = {
    "@type": "WebSite",
    "@id": SITE_URL + "/#website",
    "name": SITE_NAME,
    "url": SITE_URL + "/",
    "inLanguage": LANG,
    "publisher": {"@id": SITE_URL + "/#organization"},
}


def nav_html(current):
    items = []
    for slug, label in NAV:
        cur = ' aria-current="page"' if slug == current else ""
        items.append(f'<li><a href="/{slug}/"{cur}>{label}</a></li>')
    return "\n        ".join(items)


def layout(*, path, title, description, body, current="", schema=None, og_type="website",
           noindex=False):
    url = SITE_URL + path
    robots = '<meta name="robots" content="noindex">' if noindex else \
        '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">'
    schema_html = ld({"@context": "https://schema.org", "@graph": [ORG, WEBSITE] + (schema or [])})
    return f"""<!doctype html>
<html lang="{LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
{robots}
<link rel="canonical" href="{url}">
<link rel="alternate" type="text/plain" title="LLM summary" href="/llms.txt">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="en_CA">
<meta property="og:image" content="{SITE_URL}/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#f5efe3">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://images.unsplash.com">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,650&family=Source+Sans+3:wght@400;600;700&display=swap">
<link rel="stylesheet" href="/style.css?v={CSS_VERSION}">
{schema_html}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="/" aria-label="{SITE_NAME} home">
      <svg class="brand-mark" viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="13" r="7" fill="var(--sun)"/><path d="M2 22c4-3 8-3 12 0s8 3 12 0 4-2 4-2v8H2z" fill="var(--sea)"/></svg>
      <span>Panama <em>Expat</em> Life</span>
    </a>
    <nav aria-label="Main">
      <ul class="nav">
        {nav_html(current)}
      </ul>
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <p class="footer-brand">Panama Expat Life</p>
      <p>{SITE_TAGLINE}. Written by a team that lives and works across Panama.</p>
      <p><a class="btn btn-small" href="/free-checklist/">Get the free move checklist</a></p>
    </div>
    <div>
      <p class="footer-head">Guides</p>
      <ul class="footer-links">
        {"".join(f'<li><a href="/{s}/">{l}</a></li>' for s, l in NAV)}
      </ul>
    </div>
    <div>
      <p class="footer-head">About</p>
      <ul class="footer-links">
        <li><a href="/about/">About us</a></li>
        <li><a href="/about/#disclosure">Disclosure</a></li>
        <li><a href="/about/#standards">Editorial standards</a></li>
        <li><a href="/privacy/">Privacy</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap disclosure">
    <p>Panama Expat Life is run by a team affiliated with <a href="{PANAMA_PROPERTIES_URL}" rel="noopener">Panama Properties</a>, a licensed Panamanian real estate brokerage. Some links on this site are referral partnerships. Everything here is general information, not legal, tax, immigration or medical advice.</p>
    <p>&copy; 2026 Panama Expat Life</p>
  </div>
</footer>
</body>
</html>
"""


def breadcrumb(items):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE_URL + p}
            for i, (n, p) in enumerate(items)
        ],
    }


def faq_schema(faq, path):
    return {
        "@type": "FAQPage",
        "@id": SITE_URL + path + "#faq",
        "mainEntity": [
            {"@type": "Question", "name": text(q),
             "acceptedAnswer": {"@type": "Answer", "text": text(a)}}
            for q, a in faq
        ],
    }


def section_page(p):
    path = f"/{p['slug']}/"
    toc = [(h, t) for h, t in __import__("re").findall(r'<h2 id="([^"]+)">(.*?)</h2>', p["body"])]
    toc_html = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)
    faq_html = "".join(
        f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q, a in p["faq"])
    related = "".join(
        f'<li><a class="card-link" href="/{s}/"><span class="card-kicker">{PAGE_BY_SLUG[s]["kicker"]}</span>'
        f'<span class="card-title">{PAGE_BY_SLUG[s]["h1"]}</span></a></li>'
        for s in p["related"])
    body = f"""
<article class="article">
  <div class="wrap article-head">
    <nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li aria-current="page">{p['kicker']}</li></ol></nav>
    <p class="kicker">{p['kicker']}</p>
    <h1>{p['h1']}</h1>
    <p class="lead">{p['lead']}</p>
    <p class="meta">By the Panama Expat Life team &middot; Last checked <time datetime="{LAST_CHECKED}">{LAST_CHECKED_HUMAN}</time></p>
  </div>
  <div class="wrap article-grid">
    <aside class="toc" aria-label="On this page">
      <p class="toc-head">On this page</p>
      <ol>{toc_html}<li><a href="#faq">Common questions</a></li></ol>
    </aside>
    <div class="prose">
      {p['body']}
      <section id="faq" class="faq" aria-labelledby="faq-title">
        <h2 id="faq-title">Common questions</h2>
        {faq_html}
      </section>
    </div>
  </div>
  <section class="wrap related" aria-labelledby="related-title">
    <h2 id="related-title">Keep reading</h2>
    <ul class="cards cards-3">{related}</ul>
  </section>
  {cta_band()}
</article>
"""
    schema = [
        {
            "@type": "Article",
            "@id": SITE_URL + path + "#article",
            "headline": text(p["h1"]),
            "description": text(p["description"]),
            "inLanguage": LANG,
            "dateModified": LAST_CHECKED,
            "datePublished": LAST_CHECKED,
            "mainEntityOfPage": SITE_URL + path,
            "author": {"@id": SITE_URL + "/#organization"},
            "publisher": {"@id": SITE_URL + "/#organization"},
            "about": {"@type": "Country", "name": "Panama"},
        },
        breadcrumb([("Home", "/"), (p["kicker"], path)]),
        faq_schema(p["faq"], path),
    ]
    return layout(path=path, title=p["title"], description=p["description"], body=body,
                  current=p["slug"], schema=schema, og_type="article")


def cta_band():
    return """
  <section class="cta-band" aria-labelledby="cta-title">
    <div class="wrap cta-inner">
      <div>
        <h2 id="cta-title">Planning a move? Start with the checklist.</h2>
        <p>A free, month-by-month timeline from twelve months out to your first week in Panama.</p>
      </div>
      <a class="btn" href="/free-checklist/">Get the free checklist</a>
    </div>
  </section>"""


def home_page():
    cards = "".join(
        f'<li><a class="card-link" href="/{p["slug"]}/"><span class="card-kicker">{p["kicker"]}</span>'
        f'<span class="card-title">{p["h1"]}</span><span class="card-text">{p["description"]}</span></a></li>'
        for p in PAGES)
    def photo(pid, alt, label, credit, credit_url, first=False):
        base = f"https://images.unsplash.com/{pid}?fm=jpg&q=70&fit=crop&crop=entropy&auto=format"
        srcset = ", ".join(f"{base}&w={w}&h={round(w*0.62)} {w}w" for w in (640, 960, 1280))
        prio = 'loading="eager" fetchpriority="high"' if first else 'loading="eager"'
        return (f'<figure class="hero-photo"><img src="{base}&w=960&h=595" srcset="{srcset}" '
                f'sizes="(max-width: 700px) 100vw, 50vw" width="960" height="595" alt="{alt}" {prio} decoding="async">'
                f'<figcaption><span class="photo-label">{label}</span>'
                f'<span class="photo-credit">Photo: <a href="{credit_url}" rel="noopener">{credit}</a> on Unsplash</span></figcaption></figure>')

    photos = (
        photo("photo-1587759301533-ae42d7065a80",
              "The Panama City skyline at golden hour, framed by a palm tree",
              "Panama City", "Fabrice Parchet", "https://unsplash.com/photos/KWEllBjrSVM", first=True)
        + photo("photo-1517154868524-c6b5fbd62a1c",
                "A wooden canoe on turquoise water off a palm-lined beach in the San Blas Islands, Panama",
                "San Blas Islands", "Angel Silva", "https://unsplash.com/photos/V-uYocR8k8k"))

    body = f"""
<section class="hero-photos" aria-label="Panama City and a Panama beach">
  {photos}
</section>
<section class="hero">
  <div class="wrap hero-inner">
    <div class="hero-copy">
      <p class="kicker">The practical guide to Panama</p>
      <h1>Moving to Panama, explained by people who live here</h1>
      <p class="lead">Residency, cost of living, healthcare, banking, pets and where to live, in plain English. Honest about the good and the hard parts, and checked against current rules.</p>
      <p class="hero-actions"><a class="btn" href="/start-here/">Start here</a> <a class="btn btn-ghost" href="/free-checklist/">Free move checklist</a></p>
    </div>
  </div>
</section>

<section class="wrap answer" aria-labelledby="quick-title">
  <h2 id="quick-title">Moving to Panama in one paragraph</h2>
  <p>Panama uses the US dollar, has one of the region's more accessible retiree visas (the Pensionado, for a lifetime pension of about US$1,000 a month), and offers a choice of climates within a few hours' drive: hot cities and beaches, and cool mountain towns like Boquete. Most successful movers visit first, choose a region, pick a residency route with their own lawyer, arrange health insurance and banking early, and rent for six to twelve months before buying.</p>
</section>

<section class="wrap guides" aria-labelledby="guides-title">
  <h2 id="guides-title">The guides</h2>
  <ul class="cards">{cards}</ul>
</section>

<section class="wrap regions-teaser" aria-labelledby="regions-title">
  <div class="split">
    <div>
      <h2 id="regions-title">Every expat region, not just the famous ones</h2>
      <p>From Panama City and Coronado to Boquete, Volc&aacute;n, Pedas&iacute;, Las Tablas, Santa Catalina and Bocas del Toro, we cover where expats actually live, with the trade-offs nobody puts in the brochure.</p>
      <p><a href="/where-to-live/">Compare the nine regions &rarr;</a></p>
    </div>
    <ul class="pill-list" aria-label="Regions covered">
      <li>Panama City</li><li>Pacific beaches</li><li>El Valle</li><li>Chiriqu&iacute; highlands</li><li>Chiriqu&iacute; coast</li><li>Azuero Peninsula</li><li>Veraguas coast</li><li>Caribbean</li><li>Islands</li>
    </ul>
  </div>
</section>
{cta_band()}
"""
    schema = [{"@type": "WebPage", "@id": SITE_URL + "/#webpage", "url": SITE_URL + "/",
               "name": SITE_NAME, "isPartOf": {"@id": SITE_URL + "/#website"},
               "about": {"@type": "Country", "name": "Panama"}, "dateModified": LAST_CHECKED}]
    return layout(path="/", title="Panama Expat Life: Practical Guide to Moving to and Living in Panama",
                  description="Practical, local guidance for moving to and living in Panama: residency visas, cost of living, healthcare, banking, pets and the best places to live.",
                  body=body, schema=schema)


def checklist_page():
    groups = "".join(
        f'<section class="check-group" aria-labelledby="cl-{i}"><h2 id="cl-{i}">{when}</h2><ul class="checks">'
        + "".join(f"<li>{item}</li>" for item in items) + "</ul></section>"
        for i, (when, items) in enumerate(CHECKLIST))
    if KIT_FORM_ID:
        form = f"""
      <form class="signup" action="https://app.kit.com/forms/{KIT_FORM_ID}/subscriptions" method="post">
        <label for="email">Email address</label>
        <div class="signup-row">
          <input id="email" name="email_address" type="email" autocomplete="email" required placeholder="you@example.com">
          <button class="btn" type="submit">Send me the checklist</button>
        </div>
        <p class="small">We'll email you the printable checklist and our new guides. Unsubscribe any time. See our <a href="/privacy/">privacy policy</a>.</p>
      </form>"""
    else:
        form = """
      <div class="signup signup-soon">
        <p><strong>Email sign-up opens soon.</strong> The full checklist is below, free to read and print now.</p>
      </div>"""
    body = f"""
<article class="article">
  <div class="wrap article-head">
    <nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li aria-current="page">Free checklist</li></ol></nav>
    <p class="kicker">Free checklist</p>
    <h1>The Panama move checklist</h1>
    <p class="lead">A month-by-month timeline for moving to Panama, from your scouting trip twelve months out to your first week in the country. Get the printable version and new guides by email, or read the whole checklist right here.</p>
    {form}
  </div>
  <div class="wrap checklist">
    {groups}
    <p class="small">General information only. Your lawyer's document list for your residency route takes priority over this checklist.</p>
  </div>
</article>
"""
    schema = [{
        "@type": "HowTo",
        "name": "How to move to Panama: a month-by-month checklist",
        "description": "A timeline for moving to Panama from twelve months before the move to the first week in the country.",
        "inLanguage": LANG,
        "step": [{"@type": "HowToSection", "name": when,
                  "itemListElement": [{"@type": "HowToStep", "text": text(it)} for it in items]}
                 for when, items in CHECKLIST],
    }, breadcrumb([("Home", "/"), ("Free checklist", "/free-checklist/")])]
    return layout(path="/free-checklist/", title="Free Panama Move Checklist: Month-by-Month Timeline | Panama Expat Life",
                  description="A free month-by-month checklist for moving to Panama: residency documents, pets, banking, health insurance, shipping and your first week.",
                  body=body, schema=schema)


def about_page():
    body = f"""
<article class="article">
  <div class="wrap article-head">
    <nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li aria-current="page">About</li></ol></nav>
    <p class="kicker">About</p>
    <h1>About Panama Expat Life</h1>
    <p class="lead">Panama Expat Life is a practical guide to moving to and living in Panama, written by a team that lives and works in Panama City, Pedas&iacute;, Boquete and beyond.</p>
  </div>
  <div class="wrap prose prose-narrow">
    <h2 id="why">Why we built it</h2>
    <p>Most information about moving to Panama is either years out of date or written to sell something. We wanted one place that covers every region where expats actually live, is honest about the hard parts, and is checked against the current rules.</p>

    <h2 id="standards">Editorial standards</h2>
    <ul>
      <li>Every guide shows the date it was last checked.</li>
      <li>Rules that change often, such as residency requirements, are re-checked regularly against current published guidance and flagged clearly on the page.</li>
      <li>We say when something is uncertain, and point you to a lawyer, doctor or tax adviser when a decision needs one.</li>
      <li>Partners never pay to change what a guide says.</li>
    </ul>

    <h2 id="disclosure">Disclosure</h2>
    <p>Panama Expat Life is run by a team affiliated with <a href="{PANAMA_PROPERTIES_URL}" rel="noopener">Panama Properties</a>, a licensed Panamanian real estate brokerage that represents buyers. Where a guide mentions buying property, we may point readers to Panama Properties.</p>
    <p>Some links on this site are referral partnerships with businesses such as lawyers, insurance brokers, movers and currency transfer services. If you use them, we may receive a fee, at no extra cost to you. We only list businesses we have vetted, and we label paid listings as such.</p>
    <p>Nothing on this site is legal, tax, immigration, financial or medical advice. Always confirm important decisions with a qualified professional.</p>
  </div>
</article>
"""
    schema = [{"@type": "AboutPage", "url": SITE_URL + "/about/", "name": "About Panama Expat Life",
               "about": {"@id": SITE_URL + "/#organization"}},
              breadcrumb([("Home", "/"), ("About", "/about/")])]
    return layout(path="/about/", title="About Panama Expat Life: Who We Are and Our Disclosure",
                  description="Who runs Panama Expat Life, how we keep guides current, and our disclosure about affiliations and referral partners.",
                  body=body, schema=schema)


def privacy_page():
    body = """
<article class="article">
  <div class="wrap article-head">
    <p class="kicker">Privacy</p>
    <h1>Privacy policy</h1>
    <p class="meta">Last updated <time datetime="2026-10-27">October 2026</time></p>
  </div>
  <div class="wrap prose prose-narrow">
    <p>This site does not use cookies, tracking scripts or advertising networks.</p>
    <h2 id="email">Email sign-up</h2>
    <p>If you sign up for the checklist, your email address is stored by our email provider, Kit, and used only to send you the checklist and occasional new guides. Every email includes an unsubscribe link, and you can ask us to delete your details at any time.</p>
    <h2 id="logs">Server logs</h2>
    <p>Our hosting provider, Cloudflare, may keep standard technical logs (such as IP addresses) for security and performance.</p>
    <h2 id="links">Links to other sites</h2>
    <p>Partner and other external sites have their own privacy policies.</p>
  </div>
</article>
"""
    return layout(path="/privacy/", title="Privacy Policy | Panama Expat Life",
                  description="How Panama Expat Life handles your information: no cookies or tracking, and email sign-ups held by Kit.",
                  body=body)


def not_found_page():
    body = """
<section class="wrap article-head notfound">
  <p class="kicker">Page not found</p>
  <h1>We couldn't find that page</h1>
  <p class="lead">It may have moved. Try one of the guides below, or <a href="/">go to the home page</a>.</p>
  <ul class="footer-links">""" + "".join(f'<li><a href="/{s}/">{l}</a></li>' for s, l in NAV) + """</ul>
</section>"""
    return layout(path="/404.html", title="Page not found | Panama Expat Life",
                  description="The page you were looking for could not be found.", body=body, noindex=True)


def sitemap(paths):
    urls = "".join(f"<url><loc>{SITE_URL}{p}</loc><lastmod>{LAST_CHECKED}</lastmod></url>" for p in paths)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n'


ROBOTS = f"""# Panama Expat Life welcomes search engines and AI answer engines.
User-agent: *
Allow: /

# AI crawlers and answer engines (explicitly allowed)
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: Bingbot
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""


def llms_txt():
    lines = [f"# {SITE_NAME}", "", f"> {SITE_TAGLINE}. General information, last checked {LAST_CHECKED_HUMAN}; "
             "not legal, tax, immigration or medical advice.", "",
             "Run by a team affiliated with Panama Properties, a licensed Panamanian real estate brokerage.", "",
             "## Guides", ""]
    for p in PAGES:
        lines.append(f"- [{text(p['h1'])}]({SITE_URL}/{p['slug']}/): {text(p['lead'])}")
    lines += ["", "## Other", "",
              f"- [Free Panama move checklist]({SITE_URL}/free-checklist/): month-by-month moving timeline",
              f"- [About and disclosure]({SITE_URL}/about/)", ""]
    return "\n".join(lines)


HEADERS = """/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  X-Frame-Options: SAMEORIGIN

/style.css
  Cache-Control: public, max-age=86400

/*.svg
  Cache-Control: public, max-age=86400
"""


def write(rel, content):
    f = OUT / rel
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(content, encoding="utf-8")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    for f in STATIC.iterdir():
        shutil.copy(f, OUT / f.name)

    paths = ["/"]
    write("index.html", home_page())
    for p in PAGES:
        write(f"{p['slug']}/index.html", section_page(p))
        paths.append(f"/{p['slug']}/")
    write("free-checklist/index.html", checklist_page()); paths.append("/free-checklist/")
    write("about/index.html", about_page()); paths.append("/about/")
    write("privacy/index.html", privacy_page()); paths.append("/privacy/")
    write("404.html", not_found_page())
    write("sitemap.xml", sitemap(paths))
    write("robots.txt", ROBOTS)
    write("llms.txt", llms_txt())
    write("_headers", HEADERS)
    print(f"Built {len(paths)} pages into {OUT}")


if __name__ == "__main__":
    main()
