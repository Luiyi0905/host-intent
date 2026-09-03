# 03-sitio — Host Intent (static source)

Estado: arbol estatico listo, no publicado. Sitio publico en ingles US. Titulo de trabajo: Host Intent. Tagline: Hosting comparisons and deploy notes for small sites. No es un dominio comprado.

Capital 0. Sin CDN de pago, sin fuentes de pago, sin plugins, sin dominio propio. HTML + CSS del sistema. Dependencias: ninguna.

Operador: Luis Hernandez (El Salvador). Esta carpeta no se publica en este paso.

## Preview locally
From this directory, serve the folder on port 8080, then open http://127.0.0.1:8080/
Command: python3 -m http.server 8080
You can also open index.html in a browser. Folder links work more reliably with a local server than with file URLs.
Plain HTML. Zero runtime dependencies.

## Pages hosting later (do not attach in this step)
When a repo exists and Luis approves publish:
1. Copy this tree onto a non-default branch named site (not main, not master).
2. Root layout: these files at repo root; Pages source = branch site, folder /.
3. docs layout: copy these files into docs/ on branch site; Pages source = branch site, folder /docs.
4. Enable Pages in repo Settings. Public URL looks like https://USER.github.io/REPO/
5. Replace placeholder origin https://hostintent.example in sitemap.xml and robots.txt with that Pages URL (keep the subpath if it is a project site).
6. Do not publish from the default branch. Do not add a remote in this pass unless Luis asks later.
Relative URLs so the site works at a project-pages subpath and when opened locally. A local git init without a remote is optional; if you init, stay on branch site.

## Pages (9 HTML intent URLs)
- / hub
- /best-web-hosting-for-beginners/
- /hostinger-vs-cloudways/
- /shared-vs-managed-cloud-hosting/
- /best-hosting-for-students/
- /hostinger-vs-siteground/
- /how-to-deploy-a-static-site/
- /namecheap-hosting-vs-hostinger/
- /about/
Also: css/style.css, robots.txt (Allow), sitemap.xml, favicon.svg.

## FTC

Every public HTML page has a short affiliate disclosure in the header and a fuller one in the footer. /about/ is the canonical methodology and FTC page.
No fake testimonials, no income claims, no we-tested-N-hosts, no unpublished benchmarks.
No trademark-bidding language as a tactic. No health claims.
No invented prices, uptime percentages, or commissions presented as product facts. Where we lack a dated official quote: check the provider current pricing page.

## Outbound links and SubID placeholders

Namecheap, SiteGround, and Cloudways approved. Hostinger stays official:
- https://www.hostinger.com/
- Cloudways tracked: https://www.cloudways.com/en/?id=2203673
- SiteGround tracked: https://www.siteground.com/index.htm?afcode=ca3e5f79665051eeba53d5917cbd94e7
- Namecheap tracked: https://namecheap.pxf.io/c/7699650/1632743/5618?subId1=SLUG&subId2=host-intent
- https://pages.github.com/ on the deploy tutorial

### Where SubIDs will go after approval

Do not add these until a program is approved and Luis confirms the tracking template.
1. If you regenerate HTML from _template.py, add a helper that appends the network click parameters.
2. On each comparison page, replace the plain official href with the tracked URL. Keep the visible text as the official hostname.
3. SubID convention (placeholder, not live): subid1 or clickid (name varies by network) = page slug such as hostinger-vs-cloudways; subid2 = host-intent. Never put PII in SubIDs.
4. When the first tracked link ships, change zero programs approved in About and this README to the program name and date. Header/footer FTC already covers future tracked links.
5. Do not wrap links in redirect scripts. Stay static.

Hostinger affiliate-program terms (publisher T and C, fetched 2026-08-28; not product prices; not you-will-earn) are restated only on /about/: cookie up to 30 days; PayPal min 100 USD; commissions paid after 45 days; hosting commission up to 40 percent on initial 12-month-plus purchase only (no renewals); AI Builder up to 60 percent; max 300 USD per sale.

## Niche lock

English web hosting comparators and tutorials (shared plus managed cloud for small sites / student projects). Do not add courses, AI coding tools, gold, beauty, pets, Amazon, or agricultural machinery.

## What this folder is not

Live: https://luiyi0905.github.io/host-intent/ (branch site). Not an application. No forms, no analytics pixels.
Do not push the default branch.
