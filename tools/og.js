// Generates a 1200x630 social card per page from dist/ (title = page H1).
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const root = process.argv[2], out = process.argv[3]; const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
  const files = []; (function walk(d) { for (const f of fs.readdirSync(d)) { const q = path.join(d, f); if (fs.statSync(q).isDirectory()) { if (!['assets', 'crm'].includes(f)) walk(q); } else if (f === 'index.html') files.push(q); } })(root);
  for (const f of files) {
    const html = fs.readFileSync(f, 'utf8'); let h1 = (html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/) || [, ''])[1].replace(/<span class="was">[\s\S]*?<\/span>/, '').replace(/<[^>]+>/g, '').replace(/&amp;/g, '&').trim();
    const slug = path.relative(root, path.dirname(f)).split(path.sep).join('--') || 'home';
    const eyebrow = (html.match(/<p class="eyebrow">([\s\S]*?)<\/p>/) || [, 'Form 145 · Form 146'])[1].replace(/<[^>]+>/g, '');
    await p.setContent(`<html><head><link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;600&family=Plus+Jakarta+Sans:wght@800&display=swap" rel="stylesheet"></head><body style="margin:0;width:1200px;height:630px;background:#12355f;color:#fff;font-family:Inter,sans-serif;display:flex;flex-direction:column;justify-content:space-between;padding:70px 80px;box-sizing:border-box">
<div style="color:#f0a35e;font-weight:600;letter-spacing:.12em;text-transform:uppercase;font-size:22px">${eyebrow}</div>
<div style="font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;font-size:${h1.length > 60 ? 58 : 72}px;line-height:1.08">${h1}</div>
<div style="display:flex;justify-content:space-between;font-size:24px;font-weight:600"><span>Form145Form146.com · NRI Foundation</span><span style="color:#f0a35e">Form 145 free · Form 146 from ₹999</span></div></body></html>`, { waitUntil: 'networkidle' });
    await p.screenshot({ path: path.join(out, slug + '.png') });
  }
  console.log('og images', files.length); await b.close();
})();
