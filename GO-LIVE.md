# Form145Form146.com — go-live checklist

Brand: NRI Foundation (rename: edit `BRAND` in build.py and `brand` in src/assets/config.js, then `python3 build.py`).

## 1. Hosting (recommended: Cloudflare Pages, free)
15ca15cb.com already sits on Cloudflare, so keep everything there.
1. Cloudflare dashboard → Workers & Pages → Create → Pages → "Upload assets".
2. Upload the contents of `dist/` (or the `form145form146-dist.zip`). Project name: `form145form146`.
3. Custom domains → add `form145form146.com` and `www.form145form146.com`.
   (If the domain is registered elsewhere, first add it to Cloudflare and change the nameservers at the registrar.)
Netlify also works: drag `dist/` onto app.netlify.com/drop; `netlify.toml` already holds the alias-domain 301s.

## 2. 301 redirects for the other domains (Cloudflare)
Add each domain to Cloudflare (Free plan), give it a proxied dummy record (A @ 192.0.2.1, A www 192.0.2.1, orange cloud), then
Rules → Redirect Rules → "Redirect from root/www to…" with status 301, preserve query string:
| From | To |
|---|---|
| form145.com, www.form145.com | https://form145form146.com/form-145 |
| form146.com, www.form146.com | https://form145form146.com/form-146 |
| form15caform15cb.com, www | https://form145form146.com/15ca-15cb |
| 15ca15cb.com (later, when Rohit agrees) | https://form145form146.com/ + path mapping below |
| www.form145form146.com | https://form145form146.com/ (path kept) |

When 15ca15cb.com moves: redirect page-by-page where possible (`/` → `/15ca-15cb`, blog posts → matching `/guides/...`), and do a Change of Address in Google Search Console.

## 3. Lead pipeline (CRM)
- Database: Supabase project "NRI360" (existing), tables `nrif_leads` and `nrif_staff`. SQL: `supabase/001_nrif_crm.sql`.
- Website form inserts leads using the public key (insert-only; nobody can read leads without signing in as staff).
- CRM: https://form145form146.com/crm/ — sign in with an email that is in `nrif_staff`.
- Supabase → Authentication → URL configuration → add `https://form145form146.com/crm/` to Redirect URLs (needed for email sign-in links).
- Add team members: `insert into nrif_staff (email, name, role) values ('person@x.com','Name','agent');`
- Optional later: separate Supabase project for NRI Foundation (currently shares the 360nri project to avoid an extra paid project).

## 4. SEO launch
1. Google Search Console: add domain property, submit `https://form145form146.com/sitemap.xml`.
2. Bing Webmaster Tools: import from Search Console (also feeds ChatGPT/Copilot search).
3. Google Business Profile for NRI Foundation (Bengaluru) with the site link.
4. robots.txt allows AI search bots (GPTBot, ClaudeBot, PerplexityBot) — unlike 15ca15cb.com, which blocks them via Cloudflare. In Cloudflare → Security → Bots, keep "Block AI bots" OFF for this domain.
5. Analytics: add Google Analytics 4 or Cloudflare Web Analytics snippet (app.js already fires a `generate_lead` event if gtag exists).

## 5. Before heavy promotion (needs a CA's eye)
- Have the signing CA (Rohit's team) review the Form 145/146 thresholds and part descriptions on /form-145, /form-146 and the guides.
- Confirm phone/WhatsApp (+91 78900 00890 from the current site) and set up info@form145form146.com.
- Replace sample "Example only" certificate values if desired; add real reviews only once clients agree.

## 6. Social launch tracking
Use UTM links so every lead in the CRM shows its source, e.g.
`https://form145form146.com/?utm_source=instagram&utm_medium=social&utm_campaign=launch_dec26`
Bank/RM referral links: `?ref=hdfc-andheri` (saved as campaign, channel = referral).

## 7. Settings to fill in (build.py, then rebuild)
- `PRICE_STD / PRICE_COMPLEX / PRICE_BANK` — currently ₹999 / ₹1,499 / ₹499.
- `CLAIMS_MODE = "safe"` — switch to "full" to show "Largest issuer in the world", "Lowest fee in the world" and "Government registered: ITD · MCA · MSME · DGFT". Only do this after filling `REGISTRATIONS` (actual numbers) and `CLAIM_EVIDENCE` (the footnote, e.g. certificates issued per year and source).
- `SOCIAL` — WhatsApp channel, YouTube, Instagram, Facebook, LinkedIn, X links (appear in footer + Google's knowledge panel).
- `GA4_ID`, `META_PIXEL_ID` — analytics and Meta ads tracking (lead events fire automatically).
- `TESTIMONIALS` — real clients only, with their consent.
- Bank form PDFs: drop files into `src/assets/forms/<bank-slug>.pdf` (e.g. `hdfc-bank.pdf`); downloads switch on automatically after the visitor leaves their details.
- NRI Foundation logo: send the real logo; it replaces the placeholder globe mark.
