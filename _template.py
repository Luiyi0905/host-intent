"""Tiny local helper: not required to preview. HTML files are the site."""
from __future__ import annotations

NAV = [
    ("", "Home"),
    ("best-web-hosting-for-beginners/", "Beginners"),
    ("best-hosting-for-students/", "Students"),
    ("shared-vs-managed-cloud-hosting/", "Shared vs cloud"),
    ("how-to-deploy-a-static-site/", "Deploy a static site"),
    ("hostinger-vs-cloudways/", "Hostinger vs Cloudways"),
    ("hostinger-vs-siteground/", "Hostinger vs SiteGround"),
    ("namecheap-hosting-vs-hostinger/", "Namecheap vs Hostinger"),
    ("about/", "About"),
]


def prefix(depth: int) -> str:
    return "" if depth == 0 else "../"


def page(
    *,
    depth: int,
    slug: str,
    title: str,
    description: str,
    body: str,
    updated: str = "2026-08-28",
) -> str:
    p = prefix(depth)
    css = f"{p}css/style.css"
    home = p if p else "./"
    about = f"{p}about/"
    fav = f"{p}favicon.svg"
    canon = "/" if not slug else f"/{slug.strip("/")}/"
    nav_bits = []
    for href, label in NAV:
        current = (href.rstrip("/") == slug.rstrip("/")) or (href == "" and slug == "")
        url = home if href == "" else f"{p}{href}"
        ac = ' aria-current="page"' if current else ""
        nav_bits.append(f'<a href="{url}"{ac}>{label}</a>')
    nav = "\n        ".join(nav_bits)
    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — Host Intent</title>
  <meta name="description" content="{description}">
  <meta name="author" content="Luis Hernández">
  <link rel="icon" href="{fav}" type="image/svg+xml">
  <link rel="stylesheet" href="{css}">
</head>
<body>
  <a class="skip" href="#content">Skip to content</a>
  <header class="site">
    <div class="wrap">
      <p class="brand"><a href="{home}">Host Intent</a></p>
      <p class="tagline">Hosting comparisons and deploy notes for small sites.</p>
      <p class="ftc-banner"><strong>Affiliate disclosure.</strong> Host Intent is a free site. Some links go to hosting companies. If you later buy through a tracked affiliate link, we may earn a commission at no extra cost to you. <strong>Zero programs are approved as of {updated}</strong>, so outbound links on this page are official marketing URLs — not query-string affiliate links. We do not promise income, rankings, or “best” scores. Full note: <a href="{about}">About</a>.</p>
      <nav class="primary" aria-label="Primary">{nav}
      </nav>
    </div>
  </header>
  <main id="content">
    {body}
    <p class="meta">Page updated {updated}. This site is new; we have not run speed labs or long-term uptime logs. Prices change — check each provider’s current pricing page.</p>
  </main>
  <footer class="site">
    <div class="wrap">
      <p class="ftc-footer"><strong>FTC affiliate disclosure.</strong> Host Intent may earn a commission if you purchase hosting through a future affiliate link. That does not change the price you pay. As of {updated} we have <strong>no approved affiliate programs</strong> and <strong>no tracked links</strong>. We do not invent testimonials, income claims, or unpublished benchmarks. Methodology and operator details: <a href="{about}">About</a>.</p>
      <nav aria-label="Footer">{nav}
      </nav>
      <p>Host Intent is a placeholder name, not a purchased domain. Operator: Luis Hernández, El Salvador. Public copy in US English.</p>
      <p>Canonical path for this page: <code>{canon}</code></p>
    </div>
  </footer>
</body>
</html>
"""
