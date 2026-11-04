# isiaai.com

Static landing page for ISIaAI (EN at `/`, DE at `/de/`) plus Impressum and Datenschutz.
No framework, no build step for hosting, no cookies or tracking, fonts self-hosted (Inter, Outfit – OFL).

## Edit texts
All copy lives in `build.py` (dict `T`, keys `en` / `de`). After editing run:

    python3 build.py

and commit the regenerated `index.html`, `de/index.html`, `impressum/index.html`, `datenschutz/index.html`.

## Motion
Animations live in `assets/motion.js` + the `/* motion */` block in `assets/styles.css`. Visitors with "reduce motion" turned on get the static page.

## Deploy (Cloudflare Pages)
Workers & Pages → Create → Pages → Connect to Git → this repo.
Framework preset: None · Build command: *(empty)* · Output directory: `/`.
Every push to `main` deploys automatically. Then add the custom domain `isiaai.com`.

## Before going live
- Impressum: fill the yellow placeholders (legal form, address, managing director, register, VAT ID)
- Datenschutz: legal check (Alina)
- Team photo: set TEAM_PHOTO in build.py (put the image in `assets/`)
- Booking link: set BOOKING_URL in build.py (Isaac)
- LinkedIn: check LINKEDIN_URL spelling
- EU AI Act line in footer: wording check (Alina)
