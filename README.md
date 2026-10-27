# Panama Expat Life

Source for PanamaExpatLife.com, a practical guide to moving to and living in Panama.

The site is plain static HTML with no JavaScript, so search engines and AI answer engines
read every word directly. Structured data (JSON-LD), a sitemap, robots.txt and llms.txt are
generated for every build.

## Structure

- `build/content.py` – all page text
- `build/config.py` – site settings (including the Kit form ID for email sign-ups)
- `build/build.py` – generates the site
- `build/static/` – stylesheet, icons and images
- `site/` – the finished site that Cloudflare Pages publishes

## Updating

Edit the content, run `python3 build/build.py`, and commit both `build/` and `site/`.

## Cloudflare Pages settings

- Framework preset: None
- Build command: (leave empty)
- Build output directory: `site`
