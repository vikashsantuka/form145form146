#!/usr/bin/env python3
"""Static site generator for Form145Form146.com.

Usage:
  python3 build.py            -> dist/      production build (clean URLs, absolute canonical links)
  python3 build.py --preview  -> preview/   flat .html files with relative links (for the shareable preview)

Rename the brand or domain by changing BRAND / DOMAIN below and rebuilding.
"""
import json, os, re, shutil, sys, html
from datetime import date

BRAND = "NRI Foundation"
DOMAIN = "https://form145form146.com"
SITE_NAME = "Form145Form146.com"
PHONE = "+91 78900 00890"
PHONE_TEL = "+917890000890"
WHATSAPP = "917890000890"
EMAIL = "info@form145form146.com"
CITY = "Bengaluru, India"
REVIEWED = "November 2026"
TODAY = date.today().isoformat()

# ---- Prices (change here, rebuild) ----
PRICE_STD, PRICE_COMPLEX, PRICE_BANK = "₹999", "₹1,499", "₹499"

# ---- "Why us" claims ----
# "safe": wording we can stand behind today. "full": the original 15ca15cb.com claims (largest issuer, lowest fee in
# the world, government registrations). Switch to "full" only once REGISTRATIONS and CLAIM_EVIDENCE are filled in.
CLAIMS_MODE = "full"  # confirmed by Vikash 25 Nov 2026; Rohit holds the supporting documents
REGISTRATIONS = {"Income Tax Dept (PAN/TAN)": "", "MCA (CIN/LLPIN)": "", "MSME (Udyam)": "", "DGFT (IEC)": ""}
CLAIM_EVIDENCE = "*Based on NRI Foundation records of certificates issued and on published fees of other online providers, November 2026. Registration details available on request."  # e.g. "*Based on 12,400 certificates issued in FY 2025-26, audited by ..."

# ---- Social profiles (shown in footer and schema once filled) ----
SOCIAL = {"WhatsApp Channel": "", "YouTube": "", "Instagram": "", "Facebook": "", "LinkedIn": "", "X": ""}

# ---- Analytics (leave empty to load nothing) ----
GA4_ID = ""        # e.g. "G-XXXXXXX"
META_PIXEL_ID = "" # e.g. "123456789012345"

# ---- Testimonials: add only real clients who agreed to be quoted ----
TESTIMONIALS = []  # e.g. [("Selling my flat in Pune...", "R. Nair", "Dubai, UAE", "Rental income")]

PREVIEW = "--preview" in sys.argv
OUT = "preview" if PREVIEW else "dist"

sys.path.insert(0, os.path.dirname(__file__))
import content  # noqa: E402

PAGES = []  # dicts: slug, title, desc, body, schema(list), crumbs(list of (name, slug)), noindex, priority


def page(**kw):
    kw.setdefault("schema", [])
    kw.setdefault("crumbs", [])
    kw.setdefault("noindex", False)
    kw.setdefault("priority", "0.7")
    kw.setdefault("nav", "")
    PAGES.append(kw)


def url(slug, current_slug=""):
    """Link to a page. slug '' = home. Preview mode uses relative .html paths."""
    if slug.startswith("http") or slug.startswith("#") or slug.startswith("mailto:") or slug.startswith("tel:"):
        return slug
    anchor = ""
    if "#" in slug:
        slug, anchor = slug.split("#", 1)
        anchor = "#" + anchor
    if not PREVIEW:
        return ("/" + slug if slug else "/") + anchor
    depth = current_slug.count("/")
    prefix = "../" * depth
    target = (slug if slug else "index") + ".html"
    return prefix + target + anchor


def asset(path, current_slug=""):
    if not PREVIEW:
        return "/" + path
    return "../" * current_slug.count("/") + path


def abs_url(slug):
    return DOMAIN + ("/" + slug if slug else "/")


LOGO_SVG = """<svg width="34" height="34" viewBox="0 0 34 34" aria-hidden="true"><rect x="1" y="1" width="32" height="32" rx="8" fill="var(--brand)"/><path d="M10 9h10l4 4v12H10z" fill="none" stroke="var(--surface)" stroke-width="2"/><path d="M13 17h8M13 21h5" stroke="var(--accent)" stroke-width="2" stroke-linecap="round"/></svg>"""

NAV = [
    ("Form 145", "form-145"),
    ("Form 146", "form-146"),
    ("Send money abroad", "send-money-abroad"),
    ("Banks", "banks"),
    ("Pricing", "pricing"),
    ("Guides", "guides"),
    ("FAQ", "faq"),
]


def render(p):
    slug = p["slug"]
    L = lambda s: url(s, slug)  # noqa: E731
    A = lambda s: asset(s, slug)  # noqa: E731
    body = p["body"](L) if callable(p["body"]) else p["body"]

    crumbs_html = ""
    crumb_schema = None
    if p["crumbs"]:
        items = [("Home", "")] + p["crumbs"] + [(p.get("crumb", p["h1"] if "h1" in p else p["title"]), slug)]
        parts = []
        for i, (n, s) in enumerate(items):
            if i == len(items) - 1:
                parts.append(f'<span aria-current="page">{html.escape(n)}</span>')
            else:
                parts.append(f'<a href="{L(s)}">{html.escape(n)}</a>')
        crumbs_html = '<nav class="crumbs wrap" aria-label="Breadcrumb">' + '<span aria-hidden="true">/</span>'.join(parts) + "</nav>"
        crumb_schema = {
            "@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": abs_url(s)} for i, (n, s) in enumerate(items)],
        }

    schemas = [org_schema()] + list(p["schema"]) + ([crumb_schema] if crumb_schema else [])
    if slug == "":
        schemas.append(website_schema())
    schema_html = "\n".join(
        '<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False) + "</script>" for s in schemas
    )

    nav_html = "".join(
        f'<a href="{L(s)}"{" aria-current=\"page\"" if (p["nav"] == s or slug == s) else ""}>{n}</a>' for n, s in NAV
    )
    canonical = abs_url(slug)
    robots = "noindex, nofollow" if p["noindex"] else "index, follow, max-image-preview:large"
    title = p["title"]
    if len(html.unescape(title)) > 62 and " | " in title:
        title = title.rsplit(" | ", 1)[0]  # drop the site-name suffix so the useful words fit in search results
    desc = html.escape(p["desc"], quote=True)
    og_type = "article" if slug.startswith("guides/") else "website"

    head = f"""<title>{html.escape(title)}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{canonical}">
<link rel="alternate" hreflang="x-default" href="{canonical}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{BRAND} · {SITE_NAME}">
<meta property="og:title" content="{html.escape(title, quote=True)}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{DOMAIN}/assets/og/{og_name(slug)}.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title, quote=True)}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{DOMAIN}/assets/og/{og_name(slug)}.png">
<meta name="theme-color" content="#12355f">
<link rel="icon" href="{A('assets/favicon.svg')}" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Plus+Jakarta+Sans:wght@600;700;800&family=IBM+Plex+Mono:wght@500&display=swap">
<link rel="stylesheet" href="{A('assets/site.css')}">
{schema_html}"""

    header = f"""<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="{L('')}">{LOGO_SVG}<span>{SITE_NAME}<small>by {BRAND}</small></span></a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="nav" id="site-nav" aria-label="Main">{nav_html}<a class="btn btn-primary btn-sm" href="{L('get-started')}">Get started</a></nav>
  </div>
</header>"""

    footer = footer_html(L, A)
    scripts = f"""<a class="wa-float" href="https://wa.me/{WHATSAPP}?text={'Hi%20NRI%20Foundation%2C%20I%20need%20help%20with%20Form%20145%2F146'}" target="_blank" rel="noopener">WhatsApp us</a>
<script src="{A('assets/config.js')}"></script>
<script src="{A('assets/app.js')}" defer></script>"""

    share = share_bar(p, L) if slug.split("/")[0] in ("guides", "repatriate", "send-money-from-india-to") and "/" in slug else ""
    main = f'<main id="main">{crumbs_html}{body}{share}</main>'
    if PREVIEW and slug == "":
        # The preview host wraps the start page in its own document skeleton.
        return f'<meta name="claude:viewport-fit-sides" content="cover">\n{head}\n{header}\n{main}\n{footer}\n{scripts}\n'
    return f"""<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{head}
</head>
<body>
{header}
{main}
{footer}
{scripts}
</body>
</html>
"""


def footer_html(L, A):
    c = content
    col = lambda items: "".join(f'<li><a href="{L(s)}">{html.escape(n)}</a></li>' for n, s in items)  # noqa: E731
    services = [("Form 145 filing (free)", "form-145"), ("Form 146 CA certificate", "form-146"), ("15CA / 15CB", "15ca-15cb"),
                ("Send money abroad", "send-money-abroad"), ("Pricing", "pricing"), ("How it works", "how-it-works")]
    cases = [(u["short"], "repatriate/" + u["slug"]) for u in c.USE_CASES]
    countries = [(f"Send money to {x['name']}", "send-money-from-india-to/" + x["slug"]) for x in c.COUNTRIES[:6]]
    quick = [("Talk to a CA", "talk-to-ca"), ("Request a callback", "talk-to-ca#callback"), ("Ask a question", "ask-a-question"), ("Download sample certificate", "downloads#sample"),
             ("Download RDF", "downloads#rdf"), ("Bank forms", "bank-forms"), ("Open NRE / NRO account", "open-nri-account"), ("Best rate in your bank", "bank-rate-assistance")]
    company = [("About " + BRAND, "about"), ("For banks", "bank-partners"), ("Guides", "guides"), ("FAQ", "faq"), ("Contact", "get-started"),
               ("Privacy", "privacy"), ("Terms", "terms"), ("Disclaimer", "disclaimer")]
    A_LOGO, A_LOGO2 = A("assets/nri-foundation-logo.png"), A("assets/nri-foundation-logo@2x.png")
    social_html = ('<p class="small">' + " · ".join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in SOCIAL.items() if u) + "</p>") if any(SOCIAL.values()) else ""
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="logo" href="{L('')}">{LOGO_SVG}<span>{SITE_NAME}<small>by {BRAND}</small></span></a>
        <p style="margin:14px 0 0"><img class="nrif-logo" src="{A_LOGO}" srcset="{A_LOGO2} 2x" alt="{BRAND} logo" width="104" height="70" loading="lazy"></p>
        <p class="muted small" style="margin-top:12px">Form 145 and Form 146 (formerly Form 15CA and 15CB) plus bank paperwork for NRIs and businesses sending money out of India. By NRIs, for NRIs.</p>
        <p class="small">Call or WhatsApp: <a href="tel:{PHONE_TEL}">{PHONE}</a><br>Email: <a href="mailto:{EMAIL}">{EMAIL}</a><br>{CITY}</p>
        {social_html}
      </div>
      <div><p class="foot-h">Services</p><ul>{col(services)}</ul></div>
      <div><p class="foot-h">Repatriate</p><ul>{col(cases)}</ul></div>
      <div><p class="foot-h">Quick links</p><ul>{col(quick)}</ul></div>
      <div><p class="foot-h">{BRAND}</p><ul>{col(company)}</ul></div>
    </div>
    <p class="legal">© {date.today().year} {BRAND}. {SITE_NAME} is an initiative of {BRAND}. Certificates in Form 146 are issued by independent practising Chartered Accountants. We are not a bank and never hold or move your money; remittances are made by your own bank. Information on this site is general guidance, last reviewed {REVIEWED}, and not tax or legal advice for your specific case.</p>
  </div>
</footer>"""


def og_name(slug):
    return slug.replace("/", "--") or "home"


def share_bar(p, L):
    from urllib.parse import quote
    u = abs_url(p["slug"]) + "?utm_source=share&utm_medium=social"
    t = quote(p.get("h1", p["title"]))
    q = quote(u, safe="")
    links = [("WhatsApp", f"https://wa.me/?text={t}%20{q}"), ("LinkedIn", f"https://www.linkedin.com/sharing/share-offsite/?url={q}"),
             ("Facebook", f"https://www.facebook.com/sharer/sharer.php?u={q}"), ("X", f"https://twitter.com/intent/tweet?url={q}&text={t}")]
    a = "".join(f'<a href="{h}" target="_blank" rel="noopener">{n}</a>' for n, h in links)
    return f'<div class="wrap share"><span class="muted small">Know someone sending money out of India? Share this:</span><div class="bank-chips">{a}</div></div>'


def org_schema():
    return {
        "@context": "https://schema.org", "@type": "ProfessionalService", "@id": DOMAIN + "/#org",
        "name": BRAND, "alternateName": [SITE_NAME, "Form 145 Form 146", "15CA 15CB"],
        "url": DOMAIN + "/", "logo": DOMAIN + "/assets/nri-foundation-logo@2x.png", "image": DOMAIN + "/assets/og.png",
        "telephone": PHONE_TEL, "email": EMAIL,
        "address": {"@type": "PostalAddress", "addressLocality": "Bengaluru", "addressRegion": "Karnataka", "addressCountry": "IN"},
        "areaServed": ["IN", "US", "GB", "CA", "AU", "AE", "SG", "DE", "NZ"],
        "priceRange": "₹0 – ₹1,499",
        "sameAs": [v for v in SOCIAL.values() if v],
        "knowsAbout": ["Form 145", "Form 146", "Form 15CA", "Form 15CB", "NRO repatriation", "outward remittance", "DTAA", "TDS on remittances"],
    }


def website_schema():
    return {"@context": "https://schema.org", "@type": "WebSite", "@id": DOMAIN + "/#website", "name": SITE_NAME,
            "url": DOMAIN + "/", "publisher": {"@id": DOMAIN + "/#org"}, "inLanguage": "en-IN"}


def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in faqs]}


def service_schema(name, desc, price=None, slug=""):
    s = {"@context": "https://schema.org", "@type": "Service", "name": name, "description": desc, "provider": {"@id": DOMAIN + "/#org"},
         "areaServed": "Worldwide", "serviceType": "Tax compliance for foreign remittance", "url": abs_url(slug)}
    if price is not None:
        s["offers"] = {"@type": "Offer", "price": str(price), "priceCurrency": "INR", "availability": "https://schema.org/InStock"}
    return s


def article_schema(p):
    return {"@context": "https://schema.org", "@type": "Article", "headline": p["h1"], "description": p["desc"],
            "datePublished": p.get("date", "2026-11-25"), "dateModified": TODAY, "author": {"@type": "Organization", "name": BRAND + " CA desk"},
            "publisher": {"@id": DOMAIN + "/#org"}, "mainEntityOfPage": abs_url(p["slug"]), "image": DOMAIN + "/assets/og.png", "inLanguage": "en-IN"}


def write(path, text):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full) or ".", exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    shutil.copytree("src/assets", os.path.join(OUT, "assets"))
    forms_dir = os.path.join("src", "assets", "forms")
    bank_forms = {}
    for bslug, bname in content.BANKS:
        if os.path.exists(os.path.join(forms_dir, bslug + ".pdf")):
            bank_forms[bname] = "assets/forms/" + bslug + ".pdf"
    with open(os.path.join(OUT, "assets", "config.js"), "a", encoding="utf-8") as f:
        f.write("window.NRIF_CONFIG.bankForms = " + json.dumps(bank_forms) + ";\n")
        f.write("window.NRIF_CONFIG.ga4 = " + json.dumps(GA4_ID) + "; window.NRIF_CONFIG.metaPixel = " + json.dumps(META_PIXEL_ID) + ";\n")
    content.register(sys.modules[__name__])
    for p in PAGES:
        slug = p["slug"]
        if PREVIEW:
            path = (slug or "index") + ".html"
        elif slug == "404":
            path = "404.html"
        else:
            path = (slug + "/index.html") if slug else "index.html"
        write(path, render(p))
    if not PREVIEW:
        sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        for p in PAGES:
            if p["noindex"]:
                continue
            sm.append(f"  <url><loc>{abs_url(p['slug'])}</loc><lastmod>{TODAY}</lastmod><priority>{p['priority']}</priority></url>")
        sm.append("</urlset>")
        write("sitemap.xml", "\n".join(sm) + "\n")
        for name in ("robots.txt", "llms.txt", "_redirects", "_headers", "netlify.toml"):
            src = os.path.join("src", name)
            if os.path.exists(src):
                with open(src, encoding="utf-8") as f:
                    write(name, f.read().replace("{{DOMAIN}}", DOMAIN).replace("{{BRAND}}", BRAND))
        if os.path.isdir("src/crm"):
            shutil.copytree("src/crm", os.path.join(OUT, "crm"))
    print(f"Built {len(PAGES)} pages into {OUT}/")


if __name__ == "__main__":
    main()
