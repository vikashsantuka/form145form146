// Placeholder bank form packs: a checklist PDF per bank until the bank's own forms are supplied (same filename replaces it).
const { chromium } = require('playwright');
const banks = JSON.parse(process.argv[2]);
(async () => { const b = await chromium.launch(); const p = await b.newPage();
for (const [slug, name] of banks) {
  await p.setContent(`<html><head><meta charset="utf-8"><style>@page{size:A4;margin:16mm}body{font:12px/1.55 Helvetica,Arial,sans-serif;color:#111}h1{color:#12355f;font-size:20px;margin:0}
  .top{border-bottom:3px solid #b3540c;padding-bottom:8px;margin-bottom:14px}h2{font-size:13px;background:#eaf0f8;color:#12355f;padding:5px 8px;margin:16px 0 6px}li{margin-bottom:4px}.note{background:#fff5e8;border:1px solid #e3b27a;padding:8px 10px}</style></head><body>
  <div class="top"><h1>${name}: outward remittance form pack</h1><div>Form 145 / Form 146 (formerly 15CA / 15CB) · NRI Foundation · Form145Form146.com</div></div>
  <div class="note"><b>${name}'s own request forms are being updated in this pack.</b> Message us on WhatsApp <b>+91 78900 00890</b> or email <b>info@form145form146.com</b> with "${name} forms" and we send the current set the same working day.</div>
  <h2>What ${name} usually asks for (NRO outward remittance)</h2><ol>
  <li>Form 146 (CA certificate) with UDIN</li><li>Form 145 acknowledgement from the income tax portal</li><li>Form A2 (FEMA application) with the correct purpose code</li>
  <li>${name} outward remittance request / NRO repatriation letter, signed</li><li>PAN card and passport or OCI card</li><li>Source-of-funds documents: sale deed, rent agreement, will or succession papers, FD/interest certificates</li>
  <li>Beneficiary details abroad: account number or IBAN, SWIFT/BIC, bank name and address</li><li>Tax Residency Certificate and Form 10F if a DTAA rate is used</li></ol>
  <h2>Tips</h2><ul><li>Use the same name spelling as on your ${name} account on every document.</li><li>For large amounts, ask your relationship manager about the bank's preferential rate before submitting.</li><li>Keep the SWIFT copy (MT103) for your overseas bank.</li></ul>
  <h2>Let us do it for you</h2><p>Form 145 free · Form 146 with all ${name} paperwork ₹999 (standard) or ₹1,499 (property sale, inheritance, capital gains). Start at <b>form145form146.com/get-started</b>.</p></body></html>`);
  await p.pdf({ path: 'src/assets/forms/' + slug + '.pdf', format: 'A4', printBackground: true }); }
await b.close(); console.log('forms', banks.length); })();
