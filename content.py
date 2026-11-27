"""Page content for Form145Form146.com. Edit copy here, then run build.py."""
import html as _h

PURPOSES = ["Property sale proceeds", "Rental income", "Inheritance", "NRO balance / FD interest", "Shares, mutual funds, dividends",
            "Gift or family maintenance", "Business payment to overseas vendor", "Talk to a CA / callback", "Question",
            "Open NRE / NRO account", "Preferential rate at my bank", "Bank forms download", "Other"]
AMOUNTS = ["Under ₹5 lakh", "₹5 – 25 lakh", "₹25 lakh – 1 crore", "₹1 – 5 crore", "Above ₹5 crore", "Not sure yet"]
RES_COUNTRIES = ["United States", "United Kingdom", "Canada", "Australia", "United Arab Emirates", "Singapore", "Germany", "New Zealand",
                 "Saudi Arabia", "Qatar", "Netherlands", "France", "Ireland", "Hong Kong", "India (resident)", "Other"]

COUNTRIES = [
    dict(slug="usa", name="the USA", short="USA", cur="USD", tax="US", note="US citizens and green-card holders report foreign accounts (FBAR/FATCA) in the US, so keep the Form 146 certificate and bank advice for your US tax file."),
    dict(slug="uk", name="the UK", short="UK", cur="GBP", tax="UK", note="UK residents should keep the CA certificate and TDS proof; it supports a foreign tax credit claim on your Self Assessment where India has already taxed the income."),
    dict(slug="canada", name="Canada", short="Canada", cur="CAD", tax="Canadian", note="Canadian residents report worldwide income, so the Indian TDS shown on your Form 146 helps you claim a foreign tax credit with the CRA."),
    dict(slug="australia", name="Australia", short="Australia", cur="AUD", tax="Australian", note="Australian tax residents can usually offset Indian tax paid; the Form 146 and TDS certificate are the evidence your accountant will ask for."),
    dict(slug="uae", name="the UAE", short="UAE", cur="AED", tax="UAE", note="The UAE has no personal income tax, so getting the Indian TDS right first time matters: a Tax Residency Certificate from the UAE can lower Indian TDS under the India–UAE DTAA on some income."),
    dict(slug="singapore", name="Singapore", short="Singapore", cur="SGD", tax="Singapore", note="Singapore does not tax most foreign-sourced personal income, so DTAA relief in India is often the only way to reduce tax on interest or dividends."),
    dict(slug="germany", name="Germany", short="Germany", cur="EUR", tax="German", note="German residents can generally credit Indian tax against German tax on the same income; keep Form 146 and Form 16A/TDS proof."),
    dict(slug="new-zealand", name="New Zealand", short="New Zealand", cur="NZD", tax="New Zealand", note="New Zealand residents are taxed on worldwide income and can usually claim credit for Indian tax paid; your Form 146 records what was deducted."),
]

BANKS = [
    ("axis-bank", "Axis Bank"), ("hdfc-bank", "HDFC Bank"), ("icici-bank", "ICICI Bank"), ("idfc-first-bank", "IDFC FIRST Bank"),
    ("sbi", "State Bank of India (SBI)"), ("bank-of-baroda", "Bank of Baroda"), ("bank-of-india", "Bank of India"), ("yes-bank", "Yes Bank"),
    ("dbs-bank", "DBS Bank India"), ("kotak-mahindra-bank", "Kotak Mahindra Bank"), ("hsbc", "HSBC India"), ("standard-chartered", "Standard Chartered India"),
]

USE_CASES = [
    dict(slug="property-sale-proceeds", short="Property sale proceeds", title="Repatriate property sale proceeds from India",
         intro="Sold a flat, plot or house in India? The buyer has deducted TDS, the money is sitting in your NRO account, and your bank wants Form 145 and Form 146 before it will send it abroad.",
         points=["Sale deed, buyer's TDS certificate and Form 26AS/AIS entry", "Purchase deed (or inheritance papers) to show cost of acquisition", "Capital gains computation: long-term gains on property held over 24 months are taxed at 12.5% plus surcharge and cess for NRIs",
                 "If too much TDS was deducted, we tell you how much you can claim back through your Indian return", "Up to USD 1 million per financial year can go out from NRO balances; larger amounts are planned across years"],
         faq=[("Do I need Form 146 to repatriate property sale proceeds?", "Almost always. Sale proceeds are usually above ₹5 lakh and the gain is taxable, so banks ask for the CA certificate (Form 146) along with Form 145."),
              ("Can I send the full sale amount abroad in one go?", "From an NRO account you can send up to USD 1 million per financial year, including sale proceeds. If the amount is larger we plan the transfer across financial years.")]),
    dict(slug="rental-income", short="Rental income", title="Repatriate rental income from India",
         intro="Rent from your Indian property lands in your NRO account after the tenant deducts TDS. Sending it abroad needs a Form 145 declaration and, above the threshold, a Form 146 CA certificate.",
         points=["Rent agreement and tenant TDS certificates", "NRO statement showing rent credits", "Municipal tax and standard deduction worked into the tax computation",
                 "One certificate can cover a year's accumulated rent", "We remind you before your next annual transfer"],
         faq=[("Can I repatriate rent every month?", "Yes, but most NRIs batch it quarterly or yearly to save on certificate and bank charges. We can set up a yearly reminder."),
              ("My tenant did not deduct TDS. What now?", "The tax still has to be paid. Our CA computes it, you pay it as self-assessment tax, and the certificate then reflects that the tax is settled.")]),
    dict(slug="inheritance", short="Inheritance", title="Repatriate inherited money from India",
         intro="India has no inheritance tax, but banks still need proof that the money you inherited is clean and tax-settled before it can leave the country.",
         points=["Will, probate or succession certificate, or legal heir certificate", "Death certificate and proof of relationship", "Bank or demat statements of the deceased",
                 "Income earned after the death (interest, rent) is taxable in your hands and is computed separately", "Up to USD 1 million per financial year from your NRO account"],
         faq=[("Is inherited money taxable in India?", "The inheritance itself is not taxed. Income that the inherited assets earn after you receive them, and gains when you sell them, are taxable."),
              ("I inherited a property and sold it. Which page applies?", "Both. The sale is a capital gains case, and the original cost is the cost to the previous owner. Start with the property sale page or simply ask us.")]),
    dict(slug="nro-account-balance", short="NRO balance and FD interest", title="Transfer your NRO account balance abroad",
         intro="Your NRO account collects pension, interest, dividends and old savings. Moving that balance to your overseas account is legal up to USD 1 million a year with Form 145 and Form 146.",
         points=["NRO statement and FD interest certificates", "TDS certificates (usually 30% plus cess on NRO interest unless a DTAA rate applies)", "Tax Residency Certificate and Form 10F to claim the lower DTAA rate",
                 "Source of the original deposit if the bank asks", "Option to move money NRO to NRE within the same USD 1 million limit"],
         faq=[("Can I move NRO money to my NRE account instead?", "Yes. An NRO to NRE transfer counts towards the same USD 1 million yearly limit and needs the same Form 145 and Form 146 paperwork."),
              ("Why was 30% deducted from my NRO interest?", "That is the default TDS rate for non-residents. With a Tax Residency Certificate and Form 10F, many DTAAs cap tax on interest at 10% to 15%.")]),
    dict(slug="shares-mutual-funds", short="Shares and mutual funds", title="Repatriate money from shares and mutual funds",
         intro="Redeemed mutual funds or sold shares held through your NRO demat? The gains have been taxed at source, and Form 145/146 lets you move the proceeds out.",
         points=["Capital gains statement from the fund house or broker", "Contract notes and demat holding statement", "Dividend TDS certificates",
                 "Short-term and long-term gains computed with current rates", "Portfolio investment (PIS/NRO) routing checked"],
         faq=[("Are mutual fund redemptions for NRIs taxed at source?", "Yes, fund houses deduct TDS on capital gains for NRIs. The certificate confirms the tax and the amount you can send out.")]),
    dict(slug="gift-family-maintenance", short="Gifts and family support", title="Send money abroad as a gift or for family",
         intro="Parents in India gifting money to children abroad, or supporting a family member overseas, use the Liberalised Remittance Scheme. Some of these need Form 145, and the right paperwork avoids TCS surprises.",
         points=["Resident individuals can send up to USD 250,000 per financial year under LRS", "TCS may be collected above ₹10 lakh a year on some LRS purposes and adjusts against the sender's tax",
                 "Gift deed and relationship proof", "Form A2 and the bank's LRS declaration", "We check whether Form 145 is needed at all for your purpose"],
         faq=[("Do gifts to children abroad need Form 146?", "Usually not, because a gift from your own taxed savings is not income of the recipient in India. The bank may still ask for Form 145 or a declaration, and we prepare it.")]),
    dict(slug="business-payments", short="Business payments abroad", title="Form 145/146 for payments to overseas vendors",
         intro="Indian companies, startups and freelancers paying foreign vendors for software, consulting, royalties or services must deduct the right tax and file Form 145 and Form 146 before the bank releases the payment.",
         points=["Invoice and agreement with the overseas party", "Vendor's Tax Residency Certificate, Form 10F and no-PE declaration for DTAA rates", "Equalisation levy and TDS position checked",
                 "Gross-up computation when you bear the tax", "Monthly or per-invoice certificates with quick turnaround"],
         faq=[("Does every payment to a foreign vendor need Form 146?", "No. Some payments are on the exempt list and need no form, and small taxable payments may need only Form 145. We check each payment type."),
              ("Can you handle a monthly volume of invoices?", "Yes. Businesses get a fixed monthly rate and a single point of contact. Ask for a quote.")]),
]

FAQS = [
    ("What are Form 145 and Form 146?", "They are the new names for Form 15CA and Form 15CB. Form 145 is the online declaration you file on the income tax portal before money is sent abroad. Form 146 is the certificate from a practising Chartered Accountant that confirms the nature of the payment, the tax due and the TDS rate. They replaced 15CA and 15CB from 1 April 2026 under the Income-tax Act, 2025 and the Income-tax Rules, 2026."),
    ("Is Form 145 the same as Form 15CA?", "Yes, in purpose. Form 145 does the job Form 15CA used to do, and Form 146 does the job of Form 15CB. Banks now ask for the new forms, but many people and even some bank staff still say 15CA/15CB."),
    ("When do I need Form 146 (the CA certificate)?", "When the money you are sending is taxable in India and the amount is above the threshold (₹5 lakh in a financial year under the old rules, which the new rules broadly carried forward), the bank will ask for Form 146 alongside Form 145. Property sale proceeds, rent, NRO interest and business payments abroad commonly need it. We confirm this free for your case."),
    ("How much does it cost?", "Form 145 filing is free. A Form 146 CA certificate with complete bank paperwork costs ₹999 for standard cases (rent, NRO interest, savings, dividends, gifts) and ₹1,499 for property sale, inheritance and business payments, which include a capital gains or tax computation. Customers referred by a partner bank pay ₹499. Courier, notarisation and apostille are charged at actual cost and agreed upfront."),
    ("How fast will I get my certificate?", "Usually within 24 to 48 working hours after we have your complete documents. Simple NRO interest or rent cases are often done the same day."),
    ("Do I need to visit India or my bank branch?", "No. The work is done online and over WhatsApp. Most banks accept the remittance request through internet banking, email from your registered address or your relationship manager. Where a bank insists on originals, we arrange pick-up or courier."),
    ("Which banks do you work with?", "All of them. The forms are the same for every bank. We regularly prepare paperwork for Axis, HDFC, ICICI, SBI, Kotak, IDFC FIRST, Bank of Baroda, Bank of India, Yes Bank, DBS, HSBC and Standard Chartered, and we keep their current remittance forms ready."),
    ("How much money can an NRI send out of India each year?", "From NRO balances, including sale proceeds of assets, up to USD 1 million per financial year, after taxes are paid. NRE and FCNR balances are freely repatriable. Residents can send up to USD 250,000 a year under the Liberalised Remittance Scheme."),
    ("Do I need Form 145/146 to send money from my NRE account?", "Usually not, because NRE balances are already tax-paid or exempt and freely repatriable. Some banks still ask for a declaration. Tell us your bank and we will tell you exactly what it wants."),
    ("Can you reduce the tax I pay?", "We apply the lowest legal rate. That includes DTAA rates with your country of residence when you have a Tax Residency Certificate and Form 10F, correct capital gains computation, and claiming back excess TDS through your Indian return."),
    ("What if my bank rejects the remittance?", "We fix it. Common reasons are a mismatch between Form 145 and Form 146, the wrong purpose code on Form A2, or missing source-of-funds documents. Corrections for our own certificates are free."),
    ("Is my data safe?", "Documents are shared over encrypted channels and only with the CA working on your case. We never ask for your internet banking password or OTP, and we never receive or move your money: your bank sends it directly to your overseas account."),
    ("Who signs Form 146?", "An independent practising Chartered Accountant with a valid UDIN for each certificate. You can verify the UDIN on the ICAI website."),
    ("Do you help businesses paying overseas vendors?", "Yes. Indian companies paying for foreign software, services, royalties or consulting need the same forms. We offer per-invoice and monthly plans."),
    ("What happens if Form 145/146 is wrong or not filed?", "The payer can face penalties and interest for short deduction of tax, and banks can hold the transfer. Getting the nature of payment, the DTAA position and the tax right the first time avoids both."),
]

GUIDES = [
    dict(slug="15ca-15cb-replaced-by-form-145-146", h1="15CA and 15CB are now Form 145 and Form 146: what changed in 2026",
         desc="From 1 April 2026 Form 15CA became Form 145 and Form 15CB became Form 146. What changed, what stayed the same, and what NRIs should do now.",
         read="5 min", body="""
<p>If your bank asked you for "Form 145 and Form 146" and you have only ever heard of 15CA and 15CB, you are not alone. The new Income-tax Act, 2025 and the Income-tax Rules, 2026 came into force on 1 April 2026 and renumbered almost every form. The remittance forms were renamed along with them.</p>
<h2>The short version</h2>
<div class="table-wrap"><table><thead><tr><th>Old name (till 31 March 2026)</th><th>New name (from 1 April 2026)</th><th>What it is</th></tr></thead><tbody>
<tr><td>Form 15CA</td><td><b>Form 145</b></td><td>Online declaration by the person sending money abroad, filed on the income tax e-filing portal</td></tr>
<tr><td>Form 15CB</td><td><b>Form 146</b></td><td>Certificate from a practising Chartered Accountant on the nature of the payment, tax due and TDS rate</td></tr>
<tr><td>Rule 37BB</td><td>Rule 220</td><td>The rule that sets out when the forms are needed</td></tr>
</tbody></table></div>
<h2>What stayed the same</h2>
<ul>
<li>The purpose: India wants tax settled before taxable money leaves the country.</li>
<li>The order: the CA certificate (Form 146) is prepared first, then the declaration (Form 145) is filed referencing it, then both go to the bank with Form A2.</li>
<li>Who signs: Form 146 still has to be issued by a practising CA with a UDIN.</li>
<li>The limits: NRIs can still repatriate up to USD 1 million a financial year from NRO balances.</li>
</ul>
<h2>What changed</h2>
<ul>
<li>Form names and section references. Certificates and declarations now refer to the 2025 Act, so a template from last year is out of date.</li>
<li>Portal workflows were updated for the new forms. Drafts saved under the old forms cannot be reused.</li>
<li>Banks updated their checklists at different speeds. Some branches still print "15CA/15CB" on their forms; the content they need is the new form.</li>
</ul>
<h2>What you should do</h2>
<p>If you are sending money abroad in the 2026-27 financial year, make sure the certificate you hand your bank is a Form 146 under the new Act. A 15CB issued before 1 April 2026 will not be accepted for a new remittance. If you have a transfer in progress, <a href="{get-started}">send us your details</a> and we will check what your bank needs, free.</p>
"""),
    dict(slug="how-nris-repatriate-money-from-india", h1="How NRIs repatriate money from India in 2026: step by step",
         desc="A practical 2026 guide for NRIs moving money from India to their overseas account: NRO vs NRE, Form 145 and 146, Form A2, limits and timelines.",
         read="7 min", body="""
<p>Moving your own money out of India is legal and routine, but the paperwork trips people up. Here is the process we follow for thousands of NRIs, in the order it actually happens.</p>
<h2>1. Work out which account the money is in</h2>
<p><b>NRE and FCNR</b> balances are freely repatriable. You can usually transfer them online with no Form 145/146. <b>NRO</b> balances (rent, pension, interest, sale proceeds, inheritance, old savings) can go out up to <b>USD 1 million per financial year</b>, after tax is settled. That is where Form 145 and Form 146 come in.</p>
<h2>2. Collect the source documents</h2>
<ul><li>PAN card and passport/visa or OCI card</li><li>NRO bank statement for the period</li><li>Proof of where the money came from: sale deed, rent agreement, will, FD certificates, capital gains statement</li><li>TDS certificates and your Form 26AS / AIS</li><li>Tax Residency Certificate and Form 10F if you want a lower DTAA rate</li></ul>
<h2>3. Get Form 146 from a Chartered Accountant</h2>
<p>The CA checks the nature of the money, computes the tax, applies any DTAA benefit and certifies it in Form 146 with a UDIN.</p>
<h2>4. File Form 145 on the income tax portal</h2>
<p>Form 145 is filed from your PAN login, referencing the Form 146 details. We prepare it with you so the two forms match exactly, which is the number one reason banks bounce requests.</p>
<h2>5. Submit to your bank with Form A2</h2>
<p>Your bank needs Form 145 acknowledgement, Form 146, Form A2 (the FEMA remittance application with the right purpose code) and its own request letter. Many banks accept these online or by email from your registered address.</p>
<h2>6. The bank sends the money</h2>
<p>Once the bank's treasury clears it, the money typically reaches your overseas account in one to three working days. Ask your bank for its card rate and whether a better rate is available for larger amounts.</p>
<h2>How long does it take end to end?</h2>
<p>With complete documents: certificate in 24 to 48 hours, bank processing two to five working days. Delays almost always come from missing source documents, so start with step 2.</p>
"""),
    dict(slug="do-i-need-form-146", h1="Do I need Form 146? When the CA certificate is required",
         desc="Not every remittance needs a CA certificate. When you need Form 146, when Form 145 alone is enough, and when you need neither.",
         read="5 min", body="""
<p>Banks often ask for "both forms" by default. Sometimes that is right, sometimes it costs you time for nothing. Here is how the decision works.</p>
<h2>You usually need Form 145 and Form 146 when</h2>
<ul><li>The money is taxable in India (rent, interest, capital gains, business income, fees, royalties), and</li><li>The amount sent in the financial year is above ₹5 lakh, and</li><li>You do not have a specific order from the tax department for a lower or nil deduction.</li></ul>
<h2>Form 145 alone may be enough when</h2>
<ul><li>The taxable amount is small (within the threshold), or</li><li>You hold a tax officer's certificate or order for lower or nil deduction, in which case that order replaces the CA's work for the rate.</li></ul>
<h2>Neither form may be needed when</h2>
<ul><li>The payment is on the specified exempt list (for example many LRS remittances by residents, such as education fees or travel), or</li><li>You are sending money from an NRE or FCNR account that is already freely repatriable.</li></ul>
<div class="note">These are the rules as broadly carried forward into the 2026 Rules. Your bank's own checklist can be stricter. We check your case and your bank's requirement free before you pay anything.</div>
<h2>Why getting this right matters</h2>
<p>A wrong "not needed" can mean a held remittance or a penalty notice later. A wrong "needed" just costs you money. We tell you which one it is.</p>
"""),
    dict(slug="nri-property-sale-repatriation", h1="Selling property in India as an NRI: getting the sale proceeds abroad",
         desc="TDS, capital gains at 12.5%, lower TDS certificates, the USD 1 million limit and the Form 145/146 paperwork to repatriate property sale proceeds.",
         read="8 min", body="""
<p>Property sales are the biggest single reason NRIs come to us. The amounts are large, the buyer deducts a lot of tax, and banks scrutinise every document.</p>
<h2>Before the sale: TDS by the buyer</h2>
<p>When an NRI sells property, the buyer must deduct tax at source on the capital gain, and in practice often on the whole sale price. If your actual gain is small, apply for a <b>lower deduction certificate</b> before registration so the buyer deducts less. This alone can save lakhs that would otherwise wait for a refund.</p>
<h2>Capital gains in 2026</h2>
<ul><li>Property held for more than 24 months: long-term capital gain taxed at 12.5% plus surcharge and cess for NRIs, without indexation.</li><li>Held for 24 months or less: short-term gain taxed at slab rates.</li><li>Reinvestment in a residential house or specified bonds can reduce or remove the tax, within limits.</li></ul>
<h2>After the sale: moving the money</h2>
<ol><li>Sale proceeds go to your NRO account.</li><li>A CA computes the actual gain and tax and issues Form 146.</li><li>You file Form 145 and submit both to the bank with Form A2.</li><li>Up to USD 1 million per financial year can be sent out from NRO; larger amounts are spread across financial years.</li></ol>
<h2>Documents checklist</h2>
<ul><li>Sale deed and purchase deed (or inheritance documents)</li><li>Buyer's TDS certificate and AIS/26AS</li><li>Bank statement showing the sale credit</li><li>Cost of improvement bills, if any</li><li>PAN, passport, and TRC/Form 10F if relevant</li></ul>
<p>Excess TDS is not lost. You claim it back when you file your Indian return, and we can handle that too.</p>
"""),
    dict(slug="nro-vs-nre-repatriation", h1="NRO vs NRE: which account to use for repatriation",
         desc="NRE is freely repatriable, NRO is capped at USD 1 million a year. How the two accounts differ for tax and for sending money abroad.",
         read="4 min", body="""
<div class="table-wrap"><table><thead><tr><th></th><th>NRE account</th><th>NRO account</th></tr></thead><tbody>
<tr><td>Money that goes in</td><td>Foreign earnings sent to India</td><td>Income earned in India: rent, pension, dividends, sale proceeds</td></tr>
<tr><td>Interest tax in India</td><td>Exempt</td><td>Taxable, TDS usually 30% plus cess (lower under DTAA)</td></tr>
<tr><td>Repatriation</td><td>Fully and freely repatriable</td><td>Up to USD 1 million per financial year</td></tr>
<tr><td>Form 145 / 146</td><td>Usually not needed</td><td>Usually needed for taxable amounts</td></tr>
</tbody></table></div>
<h2>Which should you use?</h2>
<p>Keep foreign earnings in NRE: they stay tax-free and you can take them back anytime. Indian income must go to NRO by law. To move NRO money abroad, or into your NRE account, you need the Form 145/146 paperwork and it counts towards the USD 1 million limit.</p>
<h2>Common mistake</h2>
<p>Depositing Indian rent or sale proceeds into an NRE account. Banks will flag it, and fixing it later is harder than doing it right now. If this has already happened, talk to us before your next transfer.</p>
"""),
    dict(slug="why-banks-reject-remittances", h1="Why banks reject NRI remittances: 7 common Form 145/146 mistakes",
         desc="The seven paperwork errors that make banks hold or return outward remittances, and how to avoid each one.",
         read="5 min", body="""
<ol>
<li><b>Old forms.</b> A Form 15CB issued under the old Act for a remittance made after 1 April 2026. Banks now need Form 146.</li>
<li><b>Mismatched amounts.</b> The amount, currency or beneficiary on Form 145 does not match Form 146 or Form A2.</li>
<li><b>Wrong purpose code.</b> Form A2 needs the RBI purpose code that matches the nature of the money, for example repatriation of sale proceeds versus family maintenance.</li>
<li><b>No source of funds.</b> A large NRO balance with no sale deed, will, or statement to show where it came from.</li>
<li><b>DTAA claimed without documents.</b> A lower treaty rate on Form 146 without a valid Tax Residency Certificate and Form 10F.</li>
<li><b>Limit crossed.</b> NRO transfers that together exceed USD 1 million in the financial year.</li>
<li><b>Wrong account.</b> Indian income parked in an NRE account, or a beneficiary account not in the NRI's name.</li>
</ol>
<p>Each of these is avoidable with a five-minute check before submission. We do that check on every case, and fix our own certificates free if a bank raises a query.</p>
"""),
    dict(slug="repatriate-inheritance-nri", h1="Is inherited money taxable for NRIs? How to repatriate an inheritance",
         desc="No inheritance tax in India, but documents and income after inheritance matter. How NRIs move inherited money abroad with Form 145 and 146.",
         read="5 min", body="""
<p>India does not tax inheritance. What it does tax is the income your inherited assets earn after they become yours, and gains when you sell them. Banks therefore want to see both the inheritance trail and a tax position before money leaves.</p>
<h2>Documents banks look for</h2>
<ul><li>Will and probate, or a succession certificate, or a legal heir certificate</li><li>Death certificate</li><li>Statements showing the transfer of assets to you</li><li>Your PAN and NRO account details</li></ul>
<h2>Tax steps</h2>
<ul><li>Interest or rent earned after the date of inheritance is your income and is taxed.</li><li>If you sell inherited property or shares, the cost and holding period of the previous owner carry over to you.</li><li>Form 146 records the inherited amount as non-taxable and any income or gains as taxable.</li></ul>
<h2>How much can go out?</h2>
<p>Up to USD 1 million per financial year from NRO balances, including inherited money. For larger estates we plan the transfers over successive years.</p>
"""),
    dict(slug="usd-1-million-repatriation-limit", h1="The USD 1 million NRO repatriation limit explained",
         desc="What counts towards the USD 1 million a year NRO limit, what does not, and how to plan larger transfers across financial years.",
         read="4 min", body="""
<p>NRIs and OCI holders can remit up to <b>USD 1 million per financial year</b> (April to March) from their NRO account balances. This covers sale proceeds of assets, inheritance, rent, pension and other balances, after tax is settled.</p>
<h2>What counts</h2>
<ul><li>All transfers from NRO accounts to overseas accounts</li><li>Transfers from NRO to NRE accounts</li><li>Transfers across all your banks combined</li></ul>
<h2>What does not count</h2>
<ul><li>Transfers from NRE or FCNR accounts, which are freely repatriable</li><li>Current income such as rent or dividends that is repatriated as current income (banks treat this separately, so ask which category your bank uses)</li></ul>
<h2>Planning a larger amount</h2>
<p>If you have, say, ₹15 crore of sale proceeds, plan to send part of it in March and the next part in April: two financial years, a few weeks apart. Each tranche needs its own Form 145 and Form 146. We schedule this for you.</p>
"""),
]


GUIDE_SEO = {'15ca-15cb-replaced-by-form-145-146': '15CA & 15CB are now Form 145 & 146: what changed (2026)', 'how-nris-repatriate-money-from-india': 'How NRIs repatriate money from India (2026 guide)', 'nri-property-sale-repatriation': 'NRI property sale: repatriate sale proceeds from India', 'repatriate-inheritance-nri': 'Inherited money for NRIs: tax and repatriation', 'why-banks-reject-remittances': 'Why banks reject remittances: 7 Form 145/146 mistakes'}


def lead_form(L, heading="Get your Form 145 and Form 146", sub="Free check of what your bank needs. A specialist calls or WhatsApps you within one working day.",
              purpose="", lead_type="nri", fid="lead", show_bank=True, extra="", download=False, button="Get my free check", short=False):
    opts = lambda items, sel="": "".join(f'<option{" selected" if i == sel else ""}>{_h.escape(i)}</option>' for i in items)  # noqa: E731
    bank_opts = "".join(f"<option>{_h.escape(n)}</option>" for _, n in BANKS) + "<option>Other bank</option>"
    bank_field = f"""<div><label for="{fid}-bank">Your bank in India</label><select id="{fid}-bank" name="bank"><option value="">Select</option>{bank_opts}</select></div>""" if show_bank else ""
    if short:
        return f"""<form class="form-card lead-form" id="{fid}" novalidate{' data-download' if download else ''}>
  <h2 class="form-title">{heading}</h2><p class="muted small" style="margin:0">{sub}</p>
  <input type="hidden" name="lead_type" value="{lead_type}"><input type="hidden" name="purpose" value="{_h.escape(purpose)}">
  <div class="hp" aria-hidden="true"><label for="{fid}-website">Website</label><input id="{fid}-website" name="website" tabindex="-1" autocomplete="off"></div>
  <div class="form-grid">
    {extra}
    <div><label for="{fid}-name">Full name</label><input id="{fid}-name" name="name" autocomplete="name" required></div>
    <div><label for="{fid}-phone">Phone / WhatsApp</label><input id="{fid}-phone" name="phone" type="tel" autocomplete="tel" placeholder="+44 7700 900123"></div>
    <div class="full"><label for="{fid}-email">Email (optional)</label><input id="{fid}-email" name="email" type="email" autocomplete="email"></div>
    <div class="full"><label class="consent"><input type="checkbox" required checked> I agree to be contacted by phone, WhatsApp or email about my request.</label></div>
    <div class="full"><button class="btn btn-primary" type="submit" data-label="{button}">{button}</button></div>
  </div>
  <div class="form-msg" role="status" aria-live="polite"></div>
</form>"""
    return f"""<form class="form-card lead-form" id="{fid}" novalidate>
  <h2 class="form-title">{heading}</h2>
  <p class="muted small" style="margin:0">{sub}</p>
  <input type="hidden" name="lead_type" value="{lead_type}">
  <div class="hp" aria-hidden="true"><label for="{fid}-website">Website</label><input id="{fid}-website" name="website" tabindex="-1" autocomplete="off"></div>
  <div class="form-grid">
    <div class="full"><label for="{fid}-name">Full name</label><input id="{fid}-name" name="name" autocomplete="name" required></div>
    <div><label for="{fid}-phone">Phone / WhatsApp</label><input id="{fid}-phone" name="phone" type="tel" autocomplete="tel" placeholder="+1 555 123 4567"></div>
    <div><label for="{fid}-email">Email</label><input id="{fid}-email" name="email" type="email" autocomplete="email"></div>
    <div><label for="{fid}-country">You live in</label><select id="{fid}-country" name="country"><option value="">Select</option>{opts(RES_COUNTRIES)}</select></div>
    <div><label for="{fid}-purpose">Money is from</label><select id="{fid}-purpose" name="purpose"><option value="">Select</option>{opts(PURPOSES, purpose)}</select></div>
    <div><label for="{fid}-amount">Approximate amount</label><select id="{fid}-amount" name="amount_band"><option value="">Select</option>{opts(AMOUNTS)}</select></div>
    {bank_field}
    {extra}
    <div class="full"><label for="{fid}-message">Anything else? (optional)</label><textarea id="{fid}-message" name="message" placeholder="e.g. Sold a flat in Pune in October, ₹1.2 crore in NRO, want to send to the UK"></textarea></div>
    <div class="full"><label class="consent"><input type="checkbox" required checked> I agree to be contacted by phone, WhatsApp or email about my request. We never share your details.</label></div>
    <div class="full"><button class="btn btn-primary" type="submit" data-label="{button}">{button}</button></div>
  </div>
  <div class="form-msg" role="status" aria-live="polite"></div>
</form>"""


def faq_block(items):
    return '<div class="faq">' + "".join(f"<details><summary>{_h.escape(q)}</summary><div><p>{a}</p></div></details>" for q, a in items) + "</div>"


def cta_band(L, text="Sending money out of India? Start with a free check.", button="Get started"):
    import build as b
    return f"""<section class="band-ink"><div class="wrap" style="display:flex;flex-wrap:wrap;gap:20px;align-items:center;justify-content:space-between">
<div><h2 style="margin:0">{text}</h2><p style="margin:.4em 0 0">Free Form 145. Form 146 with full bank paperwork from ₹999. Certificate in 24 to 48 hours.</p></div>
<div class="btn-row"><a class="btn btn-primary" href="{L('get-started')}">{button}</a><a class="btn btn-ghost" style="color:#fff;border-color:rgba(255,255,255,.4)" href="{b.wa_link()}" target="_blank" rel="noopener">WhatsApp +91 78900 00890</a></div>
</div></section>"""


def cert_mock():
    return """<div aria-hidden="true">
<div class="cert"><div class="cert-head"><b>Form 146</b><span class="pill">CA certificate</span></div>
<dl><dt>Remitter</dt><dd>NRO A/c · PAN ABCPE••••K</dd><dt>Nature</dt><dd>Sale of residential property</dd><dt>Amount</dt><dd>₹1,20,00,000</dd><dt>DTAA</dt><dd>India–UK · TRC on file</dd><dt>UDIN</dt><dd>26•••••••BKXQ1234</dd></dl>
<p style="margin:12px 0 0;display:flex;justify-content:space-between;align-items:center"><span class="muted small">Example only</span><span class="stamp">Certified</span></p></div>
<div class="cert"><div class="cert-head"><b>Form 145</b><span class="pill pill-accent">Filed free</span></div>
<dl><dt>Acknowledgement</dt><dd>1452627••••••</dd><dt>Bank</dt><dd>Form A2 · purpose code checked</dd><dt>Status</dt><dd>Ready for bank</dd></dl></div>
</div>"""


def register(b):
    page = b.page

    # ---------------- Home ----------------
    def home(L):
        uc_cards = "".join(f'<a class="card" href="{L("repatriate/" + u["slug"])}"><h3>{u["short"]}</h3><p class="muted">{u["intro"][:120].rsplit(" ",1)[0]}…</p><span class="more">See documents and steps →</span></a>' for u in USE_CASES[:6])
        bank_chips = "".join(f'<a href="{L("banks/" + s)}">{_h.escape(n)}</a>' for s, n in BANKS)
        country_chips = "".join(f'<a href="{L("send-money-from-india-to/" + c["slug"])}">{c["short"]}</a>' for c in COUNTRIES)
        guide_cards = "".join(f'<a class="card" href="{L("guides/" + g["slug"])}"><span class="pill">{g["read"]} read</span><h3 style="margin-top:10px">{g["h1"]}</h3><span class="more">Read guide →</span></a>' for g in GUIDES[:3])
        return f"""
<section class="hero"><div class="wrap hero-grid">
<div>
  <p class="eyebrow">For NRIs and businesses sending money out of India</p>
  <h1>Form 145 &amp; Form 146, done for you<span class="was">The new Form 15CA and 15CB, with your bank paperwork included</span></h1>
  <p class="lead">Free Form 145 filing. A CA-signed Form 146 certificate with every bank document you need, from ₹999. Your money moves from your NRO account to your account abroad, without a trip to India.</p>
  <ul class="ticks"><li>Certificate in 24 to 48 hours once documents are in</li><li>Any bank, any amount, any country</li><li>Lowest legal tax: DTAA rates, correct capital gains, excess TDS reclaimed</li></ul>
  <div class="btn-row"><a class="btn btn-primary" href="{L('get-started')}">Get my free check</a><a class="btn btn-ghost" href="{L('talk-to-ca')}">Talk to a CA</a></div>
  {country_picker(L)}
  <a class="initiative" style="margin-top:18px;display:inline-flex" href="{L('about')}"><span>An initiative of</span>{logo_img(b, 40)}</a>
</div>
{cert_mock()}
</div></section>

<section style="padding-block:28px"><div class="wrap">{quick_actions(L)}</div></section>

<section><div class="wrap">
  <p class="eyebrow">What you need</p>
  <h2>Two forms, one bank submission</h2>
  <div class="grid g3" style="margin-top:20px">
    <a class="card" href="{L('form-145')}"><span class="pill pill-accent">Free</span><h3 style="margin-top:10px">Form 145 (was 15CA)</h3><p class="muted">Your online declaration on the income tax portal before money goes abroad. We prepare and file it with you at no charge.</p><span class="more">About Form 145 →</span></a>
    <a class="card" href="{L('form-146')}"><span class="pill">From ₹999</span><h3 style="margin-top:10px">Form 146 (was 15CB)</h3><p class="muted">The Chartered Accountant's certificate of the nature of the money, the tax and the TDS rate, with a UDIN your bank can verify.</p><span class="more">About Form 146 →</span></a>
    <a class="card" href="{L('send-money-abroad')}"><span class="pill">Included</span><h3 style="margin-top:10px">Bank paperwork</h3><p class="muted">Form A2 with the right purpose code, your bank's request letter and a document pack that matches both forms exactly.</p><span class="more">Send money abroad →</span></a>
  </div>
</div></section>

{why_us(b, L)}
{testimonials(b)}
<section><div class="wrap">
  <p class="eyebrow">How it works</p>
  <h2>From NRO account to your account abroad in five steps</h2>
  <ol class="steps" style="margin-top:20px">
    <li><b>Tell us</b>Fill the short form or WhatsApp us. Free check of what your bank needs.</li>
    <li><b>Share documents</b>Upload on WhatsApp or email. A specialist tells you exactly what is missing.</li>
    <li><b>CA certifies</b>A practising CA computes the tax and issues Form 146 with UDIN.</li>
    <li><b>Form 145 filed</b>We file Form 145 with you on the portal, matched to the certificate.</li>
    <li><b>Bank sends money</b>You submit the pack; your bank remits to your overseas account.</li>
  </ol>
</div></section>

<section><div class="wrap">
  <p class="eyebrow">Where is the money from?</p>
  <h2>Repatriation help for every situation</h2>
  <div class="grid g3" style="margin-top:20px">{uc_cards}</div>
</div></section>

<section class="band"><div class="wrap grid g2" style="align-items:start">
  <div>
    <p class="eyebrow">Banks</p><h2>We work with every bank</h2>
    <p class="muted">Same forms, different checklists. We keep each bank's current remittance forms and know what its branches ask for.</p>
    <div class="bank-chips">{bank_chips}</div>
    <p style="margin-top:14px"><a class="btn btn-ghost btn-sm" href="{L('bank-forms')}">Download bank forms for remittance</a></p>
  </div>
  <div>
    <p class="eyebrow">Countries</p><h2>Send money to wherever you live</h2>
    <p class="muted">DTAA rates, tax residency certificates and home-country reporting, handled for each country.</p>
    <div class="bank-chips">{country_chips}</div>
  </div>
</div></section>

<section><div class="wrap">
  <p class="eyebrow">Pricing</p><h2>Simple, near-free pricing</h2>
  <div class="price-grid" style="margin-top:20px">{price_cards(L)}</div>
</div></section>

<section class="band"><div class="wrap">
  <p class="eyebrow">Guides</p><h2>Understand it before you send it</h2>
  <div class="grid g3" style="margin-top:20px">{guide_cards}</div>
  <p style="margin-top:16px"><a href="{L('guides')}">All guides →</a></p>
</div></section>

<section><div class="wrap grid g2" style="align-items:start">
  <div><p class="eyebrow">FAQ</p><h2>Questions NRIs ask us most</h2>{faq_block(FAQS[:6])}<p style="margin-top:16px"><a href="{L('faq')}">All questions →</a></p></div>
  <div class="sticky-side">{lead_form(L, fid="home")}</div>
</div></section>
"""
    page(slug="", title="Form 145 & 146 (new 15CA/15CB) for NRIs | Form 145 free",
         desc="Form 145 and Form 146 (formerly 15CA/15CB) for NRIs. Form 145 filed free, CA-signed Form 146 with bank paperwork from ₹999, ready in 24-48 hours.",
         h1="Form 145 & Form 146", body=home, priority="1.0",
         schema=[b.faq_schema(FAQS[:6]), b.service_schema("Form 145 and Form 146 for foreign remittance", "Free Form 145 filing and CA-certified Form 146 with bank paperwork for NRI repatriation and outward remittances.", 999, "")])

    # ---------------- Form 145 ----------------
    f145_faq = [FAQS[0], FAQS[1], ("Can I file Form 145 myself?", "Yes, from your own PAN login on the income tax e-filing portal. Most errors come from mismatches with Form 146 and the bank form, which is why we prepare it with you for free."),
                ("Is Form 145 needed for NRE transfers?", FAQS[8][1])]
    page(slug="form-145", nav="form-145", title="Form 145 (formerly Form 15CA): filing for NRIs, free | " + b.SITE_NAME,
         desc="Form 145 is the new Form 15CA under the Income-tax Rules 2026. Who must file it, the parts, documents needed and free filing support for NRIs and businesses.",
         h1="Form 145", crumbs=[], body=lambda L: f"""
<section class="hero"><div class="wrap hero-grid"><div>
<p class="eyebrow">Formerly Form 15CA</p>
<h1>Form 145: the remittance declaration, filed free</h1>
<p class="lead">Form 145 is the online declaration the person sending money abroad files on the income tax portal. Since 1 April 2026 it replaces Form 15CA. Banks will not release most taxable remittances without its acknowledgement.</p>
<div class="btn-row"><a class="btn btn-primary" href="{L('get-started')}">File my Form 145 free</a><a class="btn btn-ghost" href="{L('form-146')}">Do I also need Form 146?</a></div>
</div>{cert_mock()}</div></section>
<section><div class="wrap article-grid"><div class="prose">
<h2>Who files Form 145?</h2>
<p>The <b>remitter</b>: the person or business sending money to a non-resident or to their own account abroad. For an NRI moving money from an NRO account, that is the NRI. For a company paying a foreign vendor, that is the company.</p>
<h2>When is it needed?</h2>
<ul><li>Any remittance of money that is chargeable to tax in India, such as sale proceeds, rent, interest, dividends, fees or royalties.</li><li>Large taxable remittances also need a CA certificate in <a href="{L('form-146')}">Form 146</a> first.</li><li>Payments on the specified exempt list, and transfers from NRE/FCNR accounts, usually need no Form 145.</li></ul>
<h2>Which part do you fill?</h2>
<p>Like the old 15CA, Form 145 has different parts depending on the case. Broadly:</p>
<div class="table-wrap"><table><thead><tr><th>Your situation</th><th>What applies</th></tr></thead><tbody>
<tr><td>Taxable, within the small-amount threshold</td><td>Short declaration, no CA certificate</td></tr>
<tr><td>You hold a tax officer's lower or nil deduction order</td><td>Declaration quoting that order</td></tr>
<tr><td>Taxable, above the threshold</td><td>Declaration based on the CA's Form 146</td></tr>
<tr><td>Not chargeable to tax</td><td>Declaration of non-taxable nature (if the bank needs it)</td></tr>
</tbody></table></div>
<p class="muted small">We pick the right part for you; the portal will not let you change it after submission.</p>
<h2>Documents for Form 145</h2>
<ul><li>PAN and e-filing portal login (we guide you through adding us as an authorised CA)</li><li>Details of the person receiving the money and their bank abroad</li><li>Amount in foreign currency and rupees, and the nature/purpose of the payment</li><li>Form 146 acknowledgement number, where a CA certificate is needed</li></ul>
<h2>Common Form 145 errors</h2>
<p>The amount, currency or beneficiary differs from Form 146; the wrong part is chosen; or an old 15CA template is used. Read <a href="{L('guides/why-banks-reject-remittances')}">why banks reject remittances</a>.</p>
<h2>Questions</h2>{faq_block(f145_faq)}
</div><aside class="sticky-side">{lead_form(L, heading="File Form 145 free", fid="f145")}</aside></div></section>
{cta_band(L)}""", schema=[b.faq_schema(f145_faq), b.service_schema("Form 145 filing (formerly Form 15CA)", "Free preparation and filing of Form 145 remittance declarations for NRIs and businesses.", 0, "form-145")])

    # ---------------- Form 146 ----------------
    f146_faq = [FAQS[2], FAQS[12], FAQS[4], FAQS[9], ("Will my bank accept a Form 146 from you?", "Yes. Form 146 is a statutory certificate signed by a practising CA with a UDIN. Banks accept it from any practising CA; we also format the pack to each bank's checklist.")]
    page(slug="form-146", nav="form-146", title="Form 146 (formerly 15CB) CA certificate from ₹999 | " + b.SITE_NAME,
         desc="Form 146 is the new Form 15CB: a practising CA's certificate for foreign remittances. CA-signed with UDIN in 24-48 hours, from ₹999 with full bank paperwork.",
         h1="Form 146", body=lambda L: f"""
<section class="hero"><div class="wrap hero-grid"><div>
<p class="eyebrow">Formerly Form 15CB</p>
<h1>Form 146: the CA certificate your bank asks for</h1>
<p class="lead">Form 146 is a Chartered Accountant's certificate that confirms what the money is, how much tax is due, and the TDS rate, including any DTAA benefit. It replaced Form 15CB from 1 April 2026. We issue it with a UDIN in 24 to 48 hours, with every bank document included, for ₹999.</p>
<div class="btn-row"><a class="btn btn-primary" href="{L('get-started')}">Get my Form 146</a><a class="btn btn-ghost" href="{L('pricing')}">See pricing</a></div>
</div>{cert_mock()}</div></section>
<section><div class="wrap article-grid"><div class="prose">
<h2>What the CA certifies</h2>
<ul><li>Name and details of the remitter and the person receiving the money</li><li>The nature of the remittance and whether it is taxable in India</li><li>The tax computation and the rate of TDS, under the Act or under the DTAA, whichever is better for you</li><li>Whether tax has been deducted or paid, with challan details</li></ul>
<h2>When you need it</h2>
<p>When the money is taxable and the amount is above the threshold, banks ask for Form 146 before Form 145 can be filed. Common cases: <a href="{L('repatriate/property-sale-proceeds')}">property sale proceeds</a>, <a href="{L('repatriate/rental-income')}">rent</a>, <a href="{L('repatriate/nro-account-balance')}">NRO interest</a>, <a href="{L('repatriate/shares-mutual-funds')}">capital gains on shares</a> and <a href="{L('repatriate/business-payments')}">business payments to foreign vendors</a>. Not sure? Read <a href="{L('guides/do-i-need-form-146')}">Do I need Form 146?</a></p>
<h2>DTAA: paying less tax, legally</h2>
<p>India has tax treaties with over 90 countries. With a Tax Residency Certificate from your country and Form 10F, interest, dividends and some fees can be taxed at the treaty rate instead of the higher domestic rate. We apply it on the certificate wherever you qualify.</p>
<h2>Documents we need</h2>
<ul><li>PAN, passport or OCI card</li><li>NRO bank statement and the source documents (sale deed, rent agreement, will, capital gains statement, invoice)</li><li>TDS certificates and AIS/Form 26AS</li><li>Tax Residency Certificate and Form 10F, if claiming DTAA</li><li>Beneficiary bank details abroad</li></ul>
<h2>Why choose us over a local CA</h2>
<ul><li>Remittance is all we do, so certificates match bank checklists the first time</li><li>Form 145 filing and bank paperwork included, not extra</li><li>WhatsApp updates in your time zone; no office visits</li><li>Free corrections if your bank raises a query on our certificate</li></ul>
<h2>Questions</h2>{faq_block(f146_faq)}
</div><aside class="sticky-side">{lead_form(L, heading="Get your Form 146", fid="f146")}</aside></div></section>
{cta_band(L)}""", schema=[b.faq_schema(f146_faq), b.service_schema("Form 146 CA certificate (formerly Form 15CB)", "CA-signed Form 146 certificate with UDIN and complete bank paperwork for outward remittances.", 999, "form-146")])

    # ---------------- 15CA/15CB legacy keyword page ----------------
    legacy_faq = [FAQS[1], ("Will my bank still accept Form 15CA/15CB?", "Not for remittances from 1 April 2026. Banks need Form 145 and Form 146 under the new Act. If your bank's form still says 15CA/15CB, it means the new forms."),
                  FAQS[3]]
    page(slug="15ca-15cb", title="15CA 15CB online for NRIs: now Form 145 & 146 | " + b.SITE_NAME,
         desc="Looking for Form 15CA and 15CB? From 1 April 2026 they are Form 145 and Form 146. Free 15CA (Form 145) filing and 15CB (Form 146) CA certificate from ₹999.",
         h1="15CA and 15CB", body=lambda L: f"""
<section class="hero"><div class="wrap hero-grid"><div>
<p class="eyebrow">15CA 15CB online</p>
<h1>Looking for 15CA and 15CB? They are now Form 145 and Form 146</h1>
<p class="lead">From 1 April 2026, Form 15CA became <a href="{L('form-145')}">Form 145</a> and Form 15CB became <a href="{L('form-146')}">Form 146</a>. Same job, new names under the Income-tax Act, 2025. We have been preparing these certificates for NRIs for years under both names.</p>
<div class="btn-row"><a class="btn btn-primary" href="{L('get-started')}">Get my 15CA/15CB done</a></div>
</div>{cert_mock()}</div></section>
<section><div class="wrap prose">
<h2>Old name, new name</h2>
<div class="table-wrap"><table><thead><tr><th>You searched for</th><th>Your bank now needs</th><th>Price with us</th></tr></thead><tbody>
<tr><td>Form 15CA</td><td>Form 145</td><td>Free</td></tr><tr><td>Form 15CB (CA certificate)</td><td>Form 146</td><td>From ₹999 with bank paperwork</td></tr></tbody></table></div>
<p>Read the full explainer: <a href="{L('guides/15ca-15cb-replaced-by-form-145-146')}">15CA and 15CB are now Form 145 and Form 146</a>.</p>
<h2>Questions</h2>{faq_block(legacy_faq)}
</div></section>{cta_band(L)}""", schema=[b.faq_schema(legacy_faq)], priority="0.9")

    # ---------------- How it works ----------------
    howto = {"@context": "https://schema.org", "@type": "HowTo", "name": "How to repatriate money from India with Form 145 and Form 146",
             "totalTime": "P5D", "step": [{"@type": "HowToStep", "position": i + 1, "name": n, "text": t} for i, (n, t) in enumerate([
                 ("Request a free check", "Tell us where the money is from, how much, which bank and where you live."),
                 ("Share documents", "Send PAN, NRO statement and source documents over WhatsApp or email."),
                 ("CA issues Form 146", "A practising Chartered Accountant computes the tax and issues Form 146 with UDIN."),
                 ("File Form 145", "Form 145 is filed on the income tax portal matched to the certificate."),
                 ("Bank remits", "Submit Form 145, Form 146 and Form A2 to your bank, which sends the money abroad.")])]}
    page(slug="how-it-works", title="How it works: repatriate money from India in 5 steps | " + b.SITE_NAME,
         desc="The five steps from your NRO account to your overseas account: free check, documents, Form 146 by a CA, Form 145 filing, bank remittance. Timelines included.",
         h1="How it works", body=lambda L: f"""
<section class="hero"><div class="wrap"><p class="eyebrow">How it works</p><h1>Your money abroad in about a week</h1><p class="lead prose">Most delays come from missing documents, not from the tax work. Here is exactly what happens, and how long each step takes.</p></div></section>
<section><div class="wrap">
<ol class="steps">
<li><b>Free check · 10 minutes</b>Fill the form or WhatsApp us. We tell you which forms your case and your bank need.</li>
<li><b>Documents · your pace</b>Send PAN, NRO statement and source documents. We send a checklist made for your case.</li>
<li><b>Form 146 · 24 to 48 hours</b>A practising CA computes the tax, applies DTAA and issues the certificate with UDIN.</li>
<li><b>Form 145 · same day</b>Filed on the portal from your login with our help, matched line for line.</li>
<li><b>Bank · 2 to 5 working days</b>You submit the pack; your bank sends the money to your overseas account.</li>
</ol>
<div class="grid g3" style="margin-top:32px">
<div class="card"><h3>We never touch your money</h3><p class="muted">Your bank remits directly from your account to your account. We only do the paperwork.</p></div>
<div class="card"><h3>Never share passwords</h3><p class="muted">We will never ask for internet banking passwords or OTPs. Portal access is through the official authorised-CA route.</p></div>
<div class="card"><h3>Originals, only if needed</h3><p class="muted">If your bank insists on signed originals, we arrange pick-up or courier at actual cost.</p></div>
</div></div></section>{cta_band(L)}""", schema=[howto])

    # ---------------- Pricing ----------------
    pricing_faq = [FAQS[3], ("Why is it so cheap?", f"{b.BRAND} is built by NRIs for NRIs. We keep the certificate near cost so that every NRI can repatriate legally and without stress, and we earn on optional services such as tax returns and complex advisory."),
                   ("Are there hidden charges?", "No. Anything outside the standard package, such as notarisation, apostille or a lower TDS certificate application, is quoted and agreed before we start.")]
    page(slug="pricing", nav="pricing", title="Pricing: Form 145 free, Form 146 from ₹999 | " + b.SITE_NAME,
         desc="Form 145 filing free. Form 146 with bank paperwork ₹999, or ₹1,499 for property sale and capital gains cases. ₹499 via partner banks. No hidden fees.",
         h1="Pricing", body=lambda L: f"""
<section class="hero"><div class="wrap"><p class="eyebrow">Pricing</p><h1>Near-free, and the same quality for everyone</h1><p class="lead prose">No pay-what-you-like guessing. One clear price for the certificate and all the bank paperwork, and an upfront quote for anything unusual.</p></div></section>
<section><div class="wrap"><div class="price-grid">{price_cards(L)}</div>
<div class="callout" style="margin-top:18px"><b>How we compare.</b> Online CA services we checked in November 2026 publish ₹2,999 to ₹5,000 + GST per remittance for the same Form 145 + Form 146 package, and none offer Form 145 free.</div>
<p class="muted small" style="margin-top:14px">Prices in Indian rupees, exclusive of GST where applicable. Courier, notarisation, apostille, digital signature and stamp duty for gift deeds are charged at actual cost.</p>
<h2 style="margin-top:40px">Add-ons</h2>
<div class="table-wrap"><table><thead><tr><th>Service</th><th>Price</th></tr></thead><tbody>
<tr><td>Capital gains computation for property or shares</td><td>Quoted upfront, typically included for single-property cases</td></tr>
<tr><td>Lower or nil TDS certificate application (before a property sale)</td><td>Quoted upfront</td></tr>
<tr><td>Indian income tax return for NRIs (claim back excess TDS)</td><td>Quoted upfront</td></tr>
<tr><td>Business plans: monthly Form 145/146 for overseas vendor payments</td><td>Fixed monthly fee, <a href="{L('get-started')}">ask for a quote</a></td></tr>
</tbody></table></div>
<h2 style="margin-top:40px">Questions</h2>{faq_block(pricing_faq)}
</div></section>{cta_band(L)}""", schema=[b.faq_schema(pricing_faq), b.service_schema("Form 146 CA certificate with bank paperwork", "Form 146 with Form 145 filing and bank paperwork.", 999, "pricing")])

    # ---------------- Send money abroad hub ----------------
    page(slug="send-money-abroad", nav="send-money-abroad", title="Send money abroad from India (NRO repatriation) | " + b.SITE_NAME,
         desc="Send money from India to your overseas account: NRO repatriation up to USD 1 million a year, Form 145/146, Form A2 and bank paperwork, for every situation.",
         h1="Send money abroad", body=lambda L: f"""
<section class="hero"><div class="wrap hero-grid"><div>
<p class="eyebrow">Repatriation</p><h1>Send your money from India to your account abroad</h1>
<p class="lead">Rent, sale proceeds, inheritance, savings: NRIs can move up to USD 1 million every financial year from NRO accounts once tax is settled. We prepare every document so your bank says yes the first time.</p>
<div class="btn-row"><a class="btn btn-primary" href="{L('get-started')}">Start my transfer paperwork</a></div></div>{cert_mock()}</div></section>
<section><div class="wrap"><h2>Choose your situation</h2><div class="grid g3" style="margin-top:16px">
{''.join(f'<a class="card" href="{L("repatriate/" + u["slug"])}"><h3>{u["short"]}</h3><p class="muted">{u["intro"]}</p><span class="more">Documents and steps →</span></a>' for u in USE_CASES)}
</div></div></section>
<section class="band"><div class="wrap"><h2>Choose your country</h2><div class="bank-chips" style="margin-top:12px">
{''.join(f'<a href="{L("send-money-from-india-to/" + c["slug"])}">Send money to {c["name"]}</a>' for c in COUNTRIES)}</div></div></section>
{cta_band(L)}""", priority="0.9")

    # ---------------- Use case pages ----------------
    for u in USE_CASES:
        purpose_map = {"property-sale-proceeds": PURPOSES[0], "rental-income": PURPOSES[1], "inheritance": PURPOSES[2], "nro-account-balance": PURPOSES[3],
                       "shares-mutual-funds": PURPOSES[4], "gift-family-maintenance": PURPOSES[5], "business-payments": PURPOSES[6]}
        lt = "business" if u["slug"] == "business-payments" else "nri"

        def body(L, u=u, lt=lt):
            pts = "".join(f"<li>{p}</li>" for p in u["points"])
            return f"""
<section class="hero"><div class="wrap"><p class="eyebrow">Repatriate · {u['short']}</p><h1>{u['title']}</h1><p class="lead prose">{u['intro']}</p>
<div class="btn-row"><a class="btn btn-primary" href="#lead-{u['slug']}">Get a free check</a><a class="btn btn-ghost" href="{b.wa_link('Hi, I need Form 146 for ' + u['short'].lower())}" target="_blank" rel="noopener">WhatsApp us</a></div></div></section>
<section><div class="wrap article-grid"><div class="prose">
<h2>What we handle</h2><ul>{pts}</ul>
<h2>The process</h2>
<ol><li>Free check of your documents and your bank's checklist.</li><li>CA computes the tax and issues <a href="{L('form-146')}">Form 146</a> with UDIN.</li><li><a href="{L('form-145')}">Form 145</a> filed free, matched to the certificate.</li><li>Form A2 and bank letter prepared; you submit, the bank remits.</li></ol>
<h2>Price</h2><p>Form 145 free. Form 146 with bank paperwork {'₹1,499 including the tax computation' if u['slug'] in ('property-sale-proceeds','inheritance','business-payments','shares-mutual-funds') else '₹999'}. Anything extra is quoted before we start. <a href="{L('pricing')}">See pricing</a>.</p>
<h2>Questions</h2>{faq_block(u['faq'])}
</div><aside class="sticky-side" id="lead-{u['slug']}">{lead_form(L, purpose=purpose_map.get(u['slug'], ''), lead_type=lt, fid='uc')}</aside></div></section>{cta_band(L)}"""
        page(slug="repatriate/" + u["slug"], nav="send-money-abroad", title=f"{u['title']} | Form 145/146",
             desc=(u["intro"][:150].rsplit(" ", 1)[0] + "…"), h1=u["title"], crumb=u["short"], crumbs=[("Send money abroad", "send-money-abroad")],
             body=body, schema=[b.faq_schema(u["faq"]), b.service_schema(u["title"], u["intro"], 999, "repatriate/" + u["slug"])], priority="0.8")

    # ---------------- Country pages ----------------
    for c in COUNTRIES:
        cfaq = [(f"How do I send money from my NRO account to {c['name']}?", f"Get Form 146 from a CA, file Form 145, and submit both with Form A2 to your Indian bank. The bank converts rupees to {c['cur']} and sends it to your account in {c['name']}. Up to USD 1 million per financial year can go from NRO balances."),
                (f"Can I use the India–{c['short']} tax treaty?", f"India has a Double Taxation Avoidance Agreement with {c['short'].replace('the ', '')}. With a Tax Residency Certificate from {c['name']} and Form 10F, interest, dividends and some fees can be taxed at the lower treaty rate on your Form 146."),
                ("How long does it take?", FAQS[4][1])]

        def body(L, c=c, cfaq=cfaq):
            return f"""
<section class="hero"><div class="wrap hero-grid"><div><p class="eyebrow">India to {c['short']}</p>
<h1>Send money from India to {c['name']}</h1>
<p class="lead">Move your NRO balance, rent or property sale proceeds from India to your {c['cur']} account in {c['name']}. We prepare Form 145, Form 146 and your bank's paperwork, and apply the India–{c['short'].replace('the ','')} tax treaty where it helps.</p>
<div class="btn-row"><a class="btn btn-primary" href="#lead-c">Get a free check</a></div></div>{cert_mock()}</div></section>
<section><div class="wrap article-grid"><div class="prose">
<h2>What you need</h2><ul><li>Form 146 from a practising CA, with DTAA rate if you have a Tax Residency Certificate from {c['name']}</li><li>Form 145 filed on the income tax portal (free with us)</li><li>Form A2 and your bank's remittance request</li><li>Your {c['cur']} account details: account number or IBAN, SWIFT/BIC, bank address</li></ul>
<h2>Tax at home in {c['name']}</h2><p>{c['note']} This is general information; check with your {c['tax']} tax adviser for your own filing.</p>
<h2>Limits</h2><p>Up to USD 1 million per financial year from NRO accounts, including sale proceeds and inheritance. NRE and FCNR balances can be sent freely.</p>
<h2>Getting a good exchange rate</h2><p>Banks quote a card rate. For larger transfers, ask your relationship manager for a better rate before you submit, and compare with the reference rate on the day.</p>
<h2>Questions</h2>{faq_block(cfaq)}
<p>Related: <a href="{L('repatriate/property-sale-proceeds')}">property sale proceeds</a> · <a href="{L('repatriate/rental-income')}">rental income</a> · <a href="{L('guides/how-nris-repatriate-money-from-india')}">step-by-step guide</a></p>
</div><aside class="sticky-side" id="lead-c">{lead_form(L, fid='ct')}</aside></div></section>{cta_band(L)}"""
        page(slug="send-money-from-india-to/" + c["slug"], nav="send-money-abroad", title=f"Send money from India to {c['name']} (NRO to {c['cur']}) | Form 145/146",
             desc=f"Repatriate NRO funds, rent or property sale proceeds from India to {c['name']}. Form 145 free, Form 146 from ₹999 with DTAA, bank paperwork included.",
             h1=f"Send money from India to {c['name']}", crumb=c["short"], crumbs=[("Send money abroad", "send-money-abroad")], body=body,
             schema=[b.faq_schema(cfaq)], priority="0.7")

    # ---------------- Banks ----------------
    page(slug="banks", nav="banks", title="Form 145/146 for every bank: HDFC, ICICI, SBI, Axis | " + b.SITE_NAME,
         desc="Bank-wise Form 145 and Form 146 help for outward remittance: Axis, HDFC, ICICI, SBI, Kotak, IDFC FIRST, Bank of Baroda, DBS, HSBC, Standard Chartered and more.",
         h1="Banks", body=lambda L: f"""
<section class="hero"><div class="wrap"><p class="eyebrow">Banks</p><h1>Form 145 and Form 146 for your bank</h1><p class="lead prose">The forms are the same everywhere, but every bank has its own request letter, A2 format and checklist. Pick your bank to see what it asks for.</p></div></section>
<section><div class="wrap grid g3">{''.join(f'<a class="card" href="{L("banks/" + s)}"><h3>{_h.escape(n)}</h3><p class="muted">Outward remittance documents, Form A2 and Form 145/146 for {_h.escape(n)} NRO accounts.</p><span class="more">See checklist →</span></a>' for s, n in BANKS)}</div>
<p class="muted small" style="margin-top:16px">Bank names are used only to describe which bank's paperwork we prepare. {b.BRAND} is independent and not affiliated with these banks unless stated.</p></div></section>
<section class="band"><div class="wrap grid g2" style="align-items:center"><div><h2>Are you a bank?</h2><p class="muted">Refer customers who need Form 145/146 and we return them with a complete, bank-ready pack at ₹499. No change to your remittance relationship with the customer.</p><a class="btn btn-primary" href="{L('bank-partners')}">Bank partnerships</a></div></div></section>""", priority="0.8")

    for s, n in BANKS:
        bfaq = [(f"What documents does {n} need for an NRO outward remittance?", f"Typically Form 145 acknowledgement, Form 146 CA certificate, Form A2, {n}'s own remittance request or letter, PAN, and proof of the source of funds. Branches can ask for more on large amounts; we prepare the full pack."),
                (f"Can I send money abroad from {n} without visiting the branch?", "In most cases yes, through internet banking, email from your registered address or your relationship manager. If originals are required, we arrange pick-up or courier."),
                ("How much does it cost?", FAQS[3][1])]

        def body(L, n=n, bfaq=bfaq):
            return f"""
<section class="hero"><div class="wrap"><p class="eyebrow">Bank checklist</p><h1>Form 145 and Form 146 for {_h.escape(n)}</h1>
<p class="lead prose">Sending money abroad from your {_h.escape(n)} NRO account? We prepare the certificate, file the declaration and fill {_h.escape(n)}'s remittance forms so the branch can process it without back-and-forth.</p>
<div class="btn-row"><a class="btn btn-primary" href="#lead-b">Get a free check</a></div></div></section>
<section><div class="wrap article-grid"><div class="prose">
<h2>{_h.escape(n)} remittance checklist</h2>
<ul><li>Form 146 CA certificate with UDIN</li><li>Form 145 acknowledgement from the income tax portal</li><li>Form A2 with the correct RBI purpose code</li><li>{_h.escape(n)} outward remittance request / NRO repatriation letter</li><li>PAN, passport or OCI card</li><li>Source-of-funds documents (sale deed, rent agreement, will, statements)</li><li>Overseas beneficiary details: account/IBAN, SWIFT, bank address</li></ul>
<div class="note">Branch checklists change. We confirm {_h.escape(n)}'s current requirement with you before submission.</div>
<h2>Download {_h.escape(n)} remittance forms</h2><p>Get {_h.escape(n)}'s current outward remittance request, Form A2 and NRO repatriation letter. <a href="{L('bank-forms')}">Get the {_h.escape(n)} forms →</a></p>
<h2>Tips for a smooth {_h.escape(n)} transfer</h2>
<ul><li>Use the same name spelling on every form as on your {_h.escape(n)} account.</li><li>Ask your relationship manager for the exchange rate on large amounts before submitting.</li><li>Keep the SWIFT copy (MT103) the bank gives you; your overseas bank may ask for it.</li></ul>
<h2>Questions</h2>{faq_block(bfaq)}
</div><aside class="sticky-side" id="lead-b">{lead_form(L, fid='bk')}</aside></div></section>{cta_band(L)}"""
        page(slug="banks/" + s, nav="banks", title=f"{n.split(' (')[0]} Form 145/146 & remittance forms | {b.SITE_NAME}",
             desc=f"Form 145, Form 146 (15CA/15CB) and Form A2 for {n} NRO outward remittance. Checklist, process and CA certificate from ₹999.",
             h1=f"Form 145 and Form 146 for {n}", crumb=n, crumbs=[("Banks", "banks")], body=body, schema=[b.faq_schema(bfaq)], priority="0.6")

    # ---------------- Bank partners ----------------
    page(slug="bank-partners", title="Bank partnerships: Form 145/146 for your NRI customers | " + b.SITE_NAME,
         desc="For banks and NRI desks: refer customers who need Form 145 and Form 146. Bank-ready packs at ₹499 in 24-48 hours, with no change to your remittance.",
         h1="Bank partnerships", body=lambda L: f"""
<section class="hero"><div class="wrap hero-grid"><div><p class="eyebrow">For banks, NRI desks and wealth teams</p>
<h1>Stop losing remittances to paperwork</h1>
<p class="lead">Customers drop off when they hear "get a 15CB from a CA". Refer them to us and they come back with a complete, bank-ready Form 145, Form 146 and A2 pack in 24 to 48 hours.</p>
<ul class="ticks"><li>₹499 per certificate for bank-referred customers</li><li>Your checklist and formats, every time</li><li>We never handle the remittance or approach your customer for other banking</li><li>Single point of contact for your branches and RMs</li></ul></div>
{lead_form(L, heading="Talk to our partnerships team", sub="Tell us about your bank or branch network. We reply within one working day.", lead_type="bank_partner", fid="bp", show_bank=False)}</div></section>
<section><div class="wrap grid g3">
<div class="card"><h3>Higher conversion</h3><p class="muted">Customers who would have parked money in NRO complete their remittance with you.</p></div>
<div class="card"><h3>Fewer reworks</h3><p class="muted">Certificates match your checklist, so operations spend less time on queries.</p></div>
<div class="card"><h3>Simple to start</h3><p class="muted">A referral link and a WhatsApp line for RMs. No integration needed to begin.</p></div>
</div></section>""", priority="0.6")

    # ---------------- Guides ----------------
    page(slug="guides", nav="guides", title="Guides: Form 145, Form 146 and NRI repatriation | " + b.SITE_NAME,
         desc="Plain-English guides on Form 145 and Form 146 (15CA/15CB), NRO repatriation, property sale proceeds, inheritance and why banks reject remittances.",
         h1="Guides", body=lambda L: f"""
<section class="hero"><div class="wrap"><p class="eyebrow">Guides</p><h1>NRI repatriation guides</h1><p class="lead prose">Written by our CA desk, reviewed {b.REVIEWED}, in plain English.</p></div></section>
<section><div class="wrap grid g3">{''.join(f'<a class="card" href="{L("guides/" + g["slug"])}"><span class="pill">{g["read"]} read</span><h3 style="margin-top:10px">{g["h1"]}</h3><p class="muted">{g["desc"]}</p><span class="more">Read →</span></a>' for g in GUIDES)}</div></section>""", priority="0.8")

    for g in GUIDES:
        def body(L, g=g):
            txt = g["body"].replace("{get-started}", L("get-started"))
            others = "".join(f'<li><a href="{L("guides/" + o["slug"])}">{o["h1"]}</a></li>' for o in GUIDES if o["slug"] != g["slug"])[:2000]
            return f"""
<section><div class="wrap article-grid" style="padding-top:20px"><article class="prose">
<p class="eyebrow">Guide</p><h1>{g['h1']}</h1>
<p class="meta">By the {b.BRAND} CA desk · Reviewed {b.REVIEWED} · {g['read']} read</p>
{txt}
<div class="callout" style="margin-top:28px"><b>Need this done for you?</b> Form 145 is free and Form 146 with bank paperwork is from ₹999. <a href="{L('get-started')}">Get a free check</a>.</div>
<h2>More guides</h2><ul>{others}</ul>
<p class="muted small">General information, not advice for your specific situation. Rules change; we update these guides when they do.</p>
</article><aside class="sticky-side">{lead_form(L, fid='gd')}</aside></div></section>"""
        gp = dict(slug="guides/" + g["slug"], h1=g["h1"], desc=g["desc"])
        page(slug="guides/" + g["slug"], nav="guides", title=GUIDE_SEO.get(g["slug"], g["h1"]) + " | " + b.SITE_NAME, desc=g["desc"], h1=g["h1"], crumb="Guide",
             crumbs=[("Guides", "guides")], body=body, schema=[b.article_schema(gp)], priority="0.7")

    # ---------------- FAQ ----------------
    page(slug="faq", nav="faq", title="Form 145 & Form 146 FAQ (15CA/15CB questions answered) | " + b.SITE_NAME,
         desc="Answers to the most common questions about Form 145, Form 146, 15CA/15CB, NRO repatriation limits, DTAA, timelines, pricing and bank rejections.",
         h1="FAQ", body=lambda L: f"""
<section class="hero"><div class="wrap"><p class="eyebrow">FAQ</p><h1>Form 145 and Form 146 questions, answered</h1></div></section>
<section><div class="wrap article-grid"><div class="prose" style="max-width:none">{faq_block(FAQS)}</div><aside class="sticky-side">{lead_form(L, heading="Ask us anything", fid="fq")}</aside></div></section>""",
         schema=[b.faq_schema(FAQS)], priority="0.8")

    # ---------------- Get started ----------------
    page(slug="get-started", title="Get started: free check for Form 145 / 146 | " + b.SITE_NAME,
         desc="Tell us where your money is from and where it is going. A remittance specialist calls or WhatsApps you within one working day. Form 145 free, Form 146 ₹999.",
         h1="Get started", body=lambda L: f"""
<section class="hero"><div class="wrap hero-grid" style="align-items:start"><div>
<p class="eyebrow">Get started</p><h1>Tell us about your transfer</h1>
<p class="lead">Two minutes now saves days later. We check what your bank needs, tell you the documents and the price, and only then start.</p>
<ul class="ticks"><li>Reply within one working day (IST), often within the hour</li><li>Talk to a real person on WhatsApp or phone</li><li>No payment until you approve the quote</li></ul>
<div class="card" style="margin-top:20px"><h3>Prefer to talk?</h3><p>Call or WhatsApp <a href="tel:{b.PHONE_TEL}">{b.PHONE}</a><br>Email <a href="mailto:{b.EMAIL}">{b.EMAIL}</a><br>Monday to Saturday, 9 am to 9 pm IST</p></div>
</div>{lead_form(L, fid="gs")}</div></section>""", priority="0.9")

    # ---------------- About ----------------
    page(slug="about", title=f"About {b.BRAND} | {b.SITE_NAME}",
         desc=f"{b.BRAND} is built by NRIs for NRIs: near-free Form 145/146 and repatriation help, run with independent practising Chartered Accountants.",
         h1="About", body=lambda L: f"""
<section class="hero"><div class="wrap"><p style="margin:0 0 12px">{logo_img(b, 90)}</p><p class="eyebrow">About us</p><h1>By NRIs, for NRIs</h1><p class="lead prose">{b.BRAND} started because getting your own money out of India was harder than it should be. Local CAs charged what they liked, banks bounced forms, and NRIs abroad had no one to call at a sensible hour.</p></div></section>
<section><div class="wrap prose">
<h2>What we believe</h2><ul><li>Repatriating your own money legally should be close to free.</li><li>Every NRI deserves the same quality of help, whatever the amount.</li><li>Tax should be the lowest the law allows, never more and never less.</li></ul>
<h2>How we work</h2><p>Our remittance specialists handle documents and bank checklists. Certificates in Form 146 are issued by independent practising Chartered Accountants with UDIN. We never hold, route or convert your money: your bank sends it directly to your account abroad.</p>
<h2>Where we are</h2><p>{b.CITY}. Serving NRIs in the USA, UK, Canada, Australia, the Gulf, Singapore, Europe and beyond.</p>
</div></section>{why_us(b, L)}{cta_band(L)}""", priority="0.5")

    # ---------------- Legal ----------------
    legal = {
        "privacy": ("Privacy policy", f"""<p>{b.BRAND} collects the details you give us (name, contact details, country, purpose and documents) only to prepare your Form 145, Form 146 and bank paperwork and to contact you about your request.</p>
<h2>How we use your data</h2><ul><li>To assess your case and prepare documents</li><li>To share documents with the Chartered Accountant certifying your case</li><li>To contact you by phone, WhatsApp or email about your request</li></ul>
<h2>What we never do</h2><ul><li>Sell or rent your data</li><li>Ask for banking passwords or OTPs</li><li>Hold or move your money</li></ul>
<h2>Storage and retention</h2><p>Lead details are stored in a secured database with access limited to our team. Documents are retained as long as professional and legal record-keeping rules require, then deleted.</p>
<h2>Your rights</h2><p>Ask us at {b.EMAIL} to see, correct or delete your data, subject to legal retention requirements. This policy follows the Digital Personal Data Protection Act, 2023.</p>"""),
        "terms": ("Terms of use", f"""<p>By using {b.SITE_NAME} you agree to these terms.</p><h2>Our service</h2><p>We prepare documentation for outward remittances. Certificates are issued by independent practising Chartered Accountants based on the information and documents you provide. You are responsible for their accuracy and completeness.</p>
<h2>Fees</h2><p>Fees are as shown on the pricing page or as quoted to you in writing before work starts. Third-party costs are charged at actuals.</p><h2>Limits</h2><p>Your bank decides whether and when to process a remittance. We are not liable for bank delays, exchange rates or decisions of tax authorities.</p><h2>Contact</h2><p>{b.EMAIL}</p>"""),
        "disclaimer": ("Disclaimer", f"""<p>The information on this website is general guidance on Indian tax and foreign exchange rules for remittances, last reviewed {b.REVIEWED}. It is not tax, legal or financial advice for your situation. Laws, rates and bank requirements change. {b.BRAND} is not a bank or an authorised dealer and does not hold, route or convert customer funds. Bank names are used only to describe which bank's paperwork we prepare and do not imply affiliation unless stated.</p>"""),
    }
    for s, (t, body_html) in legal.items():
        page(slug=s, title=f"{t} | {b.SITE_NAME}", desc=f"{t} for {b.SITE_NAME}, an initiative of {b.BRAND}, which prepares Form 145 and Form 146 for NRIs and businesses.", h1=t,
             body=f'<section><div class="wrap prose"><h1>{t}</h1>{body_html}</div></section>', priority="0.2")

    register_extra(b)

    page(slug="404", noindex=True, title="Page not found | " + b.SITE_NAME, desc="This page has moved. Find Form 145 and Form 146 (formerly 15CA/15CB) help for NRIs on Form145Form146.com.", h1="Not found",
         body=lambda L: f'<section class="hero"><div class="wrap prose"><h1>We could not find that page</h1><p class="lead">It may have moved when 15CA/15CB became Form 145/146.</p><div class="btn-row"><a class="btn btn-primary" href="{L("")}">Go to home</a><a class="btn btn-ghost" href="{L("get-started")}">Get a free check</a></div></div></section>')


def price_cards(L):
    return f"""
<div class="price"><span class="pill pill-accent">Always free</span><h3>Form 145</h3><div class="amt">₹0</div><ul><li>Right part chosen for your case</li><li>Filed with you on the income tax portal</li><li>Acknowledgement ready for your bank</li></ul><a class="btn btn-ghost" href="{L('get-started')}">File free</a></div>
<div class="price featured"><span class="pill">Most NRIs choose this</span><h3>Form 146 · standard</h3><div class="amt">₹999 <small>per certificate</small></div><ul><li>Rent, NRO balance and FD interest, dividends, gifts</li><li>CA-signed Form 146 with UDIN</li><li>Form 145 filing, Form A2 and bank letter</li><li>DTAA rate applied where you qualify</li><li>Free corrections if the bank asks</li></ul><a class="btn btn-primary" href="{L('get-started')}">Get started</a></div>
<div class="price"><span class="pill">With tax computation</span><h3>Form 146 · property &amp; capital gains</h3><div class="amt">₹1,499 <small>per certificate</small></div><ul><li>Property sale, inheritance, shares, business payments</li><li>Capital gains or tax computation included</li><li>Everything in standard</li><li>Excess TDS flagged for refund</li></ul><a class="btn btn-ghost" href="{L('get-started')}">Get started</a></div>
<div class="price"><span class="pill">Through your bank</span><h3>Bank-referred customers</h3><div class="amt">₹499 <small>per certificate</small></div><ul><li>Standard package</li><li>When a partner bank refers you</li><li>Pack formatted to that bank's checklist</li></ul><a class="btn btn-ghost" href="{L('bank-partners')}">For banks</a></div>"""


# ======================= Round 2 additions =======================
NRIF_LOGO = """<svg width="44" height="44" viewBox="0 0 44 44" aria-hidden="true"><circle cx="22" cy="22" r="20" fill="none" stroke="var(--brand)" stroke-width="2.5"/><path d="M4 22h36M22 2c6 6 6 34 0 40M22 2c-6 6-6 34 0 40" fill="none" stroke="var(--brand)" stroke-width="1.6"/><circle cx="22" cy="22" r="6" fill="var(--accent)"/></svg>"""


def logo_img(b, h=56):
    src = b.asset("assets/nri-foundation-logo.png", "")
    src2 = b.asset("assets/nri-foundation-logo@2x.png", "")
    return f'<img class="nrif-logo" src="{src}" srcset="{src2} 2x" alt="{b.BRAND} logo" width="{int(h*320/215)}" height="{h}" loading="lazy">'


def country_picker(L):
    opts = "".join(f'<option value="{L("send-money-from-india-to/" + c["slug"])}">{c["short"]}</option>' for c in COUNTRIES)
    return f"""<form class="country-picker" aria-label="Transfer funds out of India">
<label for="cp-country">Transfer funds out of India to</label>
<div class="picker-row"><select id="cp-country"><option value="">Select destination country</option>{opts}<option value="{L('send-money-abroad')}">Other countries</option></select>
<button class="btn btn-primary" type="submit">Start transfer →</button></div><div class="form-msg small" role="status"></div></form>"""


QUICK = [("Talk to a CA", "talk-to-ca", "Free 10-minute call with a Chartered Accountant"),
         ("Request a callback", "talk-to-ca#callback", "We call you at a time that suits your time zone"),
         ("Ask a question", "ask-a-question", "Get a written answer from our CA desk"),
         ("Sample certificate", "downloads#sample", "See what a Form 146 looks like"),
         ("Download RDF", "downloads#rdf", "Remittance Details Form to start your case"),
         ("Bank forms", "bank-forms", "Remittance forms for 12 banks"),
         ("Open NRE / NRO account", "open-nri-account", "Help choosing and opening the right account"),
         ("Best rate in your bank", "bank-rate-assistance", "Ask your own bank for its preferential rate")]


def quick_actions(L):
    return '<nav class="quick" aria-label="Quick actions">' + "".join(
        f'<a href="{L(s)}"><b>{n}</b><span>{d}</span></a>' for n, s, d in QUICK) + "</nav>"


def why_us(b, L):
    full = b.CLAIMS_MODE == "full"
    regs = " · ".join(f"{k.split(' (')[0]} {v}".strip() for k, v in b.REGISTRATIONS.items() if v) if full else ""
    items = [
        ("Largest* Form 145/146 (15CA/15CB) issuer in the world" if full else "Remittance certificates are all we do",
         "Thousands of NRIs and businesses trust us with their remittance paperwork." if full else "Specialists in Form 145/146, so your pack matches what banks ask for the first time."),
        ("Lowest fee in the world*" if full else "Among the lowest fees anywhere",
         f"Form 145 free, Form 146 from {b.PRICE_STD}. Online CA services we checked in November 2026 charge ₹2,999 to ₹5,000 + GST per remittance."),
        ("Government registered" if full else "Independent practising CAs",
         (("Registered with " + regs + ".") if regs else "Registered with the Income Tax Department, MCA, MSME (Udyam) and DGFT. Every Form 146 is signed by a practising CA with UDIN.") if full else "Every Form 146 is signed by a practising Chartered Accountant with a UDIN you can verify on the ICAI website."),
        ("Any bank, any amount", "From a ₹50,000 rent transfer to crores of sale proceeds, with every Indian bank."),
        ("100% remote documentation", "WhatsApp, email and video call. Door-step pick-up when a bank needs signed originals."),
        ("100% safe and secure", "We never ask for banking passwords or OTPs, and we never hold or move your money."),
        ("Certificate in 24 to 48 hours", "Once documents are complete. Simple cases are often done the same day."),
        ("Digital, with a real office", f"Online first, with a team you can visit in {b.CITY}."),
    ]
    cards = "".join(f'<div class="why"><h3>{_h.escape(t)}</h3><p class="muted">{_h.escape(d)}</p></div>' for t, d in items)
    foot = f'<p class="muted small" style="margin-top:12px">{_h.escape(b.CLAIM_EVIDENCE)}</p>' if full and b.CLAIM_EVIDENCE else ""
    return f"""<section class="band"><div class="wrap">
<div class="why-head"><div><p class="eyebrow">Why us</p><h2>By NRIs, for NRIs</h2></div>
<a class="initiative" href="{L('about')}"><span>An initiative of</span>{logo_img(b)}</a></div>
<div class="why-grid">{cards}</div>{foot}</div></section>"""


def testimonials(b):
    if not b.TESTIMONIALS:
        return ""
    cards = "".join(f'<figure class="card"><blockquote>“{_h.escape(q)}”</blockquote><figcaption><b>{_h.escape(n)}</b><br><span class="muted small">{_h.escape(w)} · {_h.escape(t)}</span></figcaption></figure>' for q, n, w, t in b.TESTIMONIALS)
    return f'<section><div class="wrap"><p class="eyebrow">Clients</p><h2>What NRIs say</h2><div class="grid g3">{cards}</div></div></section>'


TIME_FIELDS = """<div><label for="{fid}-tz">Your time zone</label><select id="{fid}-tz" name="x_tz" data-label="Time zone"><option value="">Select</option><option>India (IST)</option><option>UK / Europe</option><option>US East</option><option>US West</option><option>Canada</option><option>Gulf (GST)</option><option>Singapore / HK</option><option>Australia / NZ</option></select></div>
<div><label for="{fid}-when">Best time to call</label><select id="{fid}-when" name="x_when" data-label="Best time"><option value="">Any time</option><option>Morning</option><option>Afternoon</option><option>Evening</option><option>Weekend</option></select></div>"""


def register_extra(b):
    page = b.page

    page(slug="talk-to-ca", title="Talk to a CA about Form 145/146: free 10-minute call",
         desc="Book a free 10-minute call with a Chartered Accountant about Form 145, Form 146 or repatriating money from India, at a time that suits your time zone.",
         h1="Talk to a CA", body=lambda L: f"""
<section class="hero"><div class="wrap hero-grid" style="align-items:start"><div>
<p class="eyebrow">Talk to a CA · Request a callback</p><h1>Speak to a Chartered Accountant, free</h1>
<p class="lead">A 10-minute call is usually enough to know which forms you need, what tax applies, and what it will cost. No obligation.</p>
<ul class="ticks"><li>Calls in your time zone, Monday to Saturday</li><li>Questions on Form 145/146, DTAA, capital gains, NRO limits</li><li>Or WhatsApp <a href="{b.wa_link('Hi, I want to talk to a CA about Form 145/146')}" target="_blank" rel="noopener">{b.PHONE}</a> right now</li></ul>
</div><div id="callback">{lead_form(L, heading="Request a callback", sub="Tell us when to call. A CA desk member calls you back.", purpose="Talk to a CA / callback", fid="cb", short=True, button="Request my callback", extra=TIME_FIELDS.replace("{fid}", "cb"))}</div></div></section>
<section><div class="wrap grid g3">
<div class="card"><h3>Before the call</h3><p class="muted">Keep your bank name, where the money came from and the rough amount handy.</p></div>
<div class="card"><h3>During the call</h3><p class="muted">We tell you the forms, documents, tax position and price for your case.</p></div>
<div class="card"><h3>After the call</h3><p class="muted">You get a written checklist on WhatsApp or email. Start whenever you are ready.</p></div>
</div></section>""", priority="0.8")

    page(slug="ask-a-question", title="Ask a question about Form 145/146 or NRI repatriation | " + b.SITE_NAME,
         desc="Ask our CA desk any question on Form 145, Form 146 (15CA/15CB), NRO repatriation, DTAA or bank remittance. Free written answer, usually the same day.",
         h1="Ask a question", body=lambda L: f"""
<section class="hero"><div class="wrap hero-grid" style="align-items:start"><div>
<p class="eyebrow">Ask a question</p><h1>Ask our CA desk anything</h1>
<p class="lead">Form 145, Form 146, DTAA, NRO limits, property sale tax, bank queries. You get a written answer, usually the same working day. Useful questions are added, without your name, to our <a href="{L('faq')}">FAQ</a>.</p>
</div>{lead_form(L, heading="Your question", sub="We reply on WhatsApp or email.", purpose="Question", fid="qa", button="Send my question")}</div></section>
<section class="band"><div class="wrap"><h2>Answered already</h2>{faq_block(FAQS[:8])}<p style="margin-top:14px"><a href="{L('faq')}">All questions →</a></p></div></section>""", priority="0.6")

    page(slug="downloads", title="Sample Form 146 certificate & Remittance Details Form download",
         desc="Download a sample Form 146 (15CB) CA certificate, the Remittance Details Form (RDF) to start your case, and bank remittance forms for 12 Indian banks.",
         h1="Downloads", body=lambda L: f"""
<section class="hero"><div class="wrap"><p class="eyebrow">Downloads</p><h1>Sample certificate, RDF and bank forms</h1><p class="lead prose">Everything you need to see what you will get and to start your case.</p></div></section>
<section><div class="wrap grid g3">
<div class="card" id="sample"><span class="pill">PDF · 1 page</span><h3 style="margin-top:10px">Sample Form 146 certificate</h3><p class="muted">An illustrative Form 146 (formerly 15CB) with example values, so you know what your bank will receive.</p><a class="btn btn-ghost" href="{b.asset('assets/downloads/sample-form-146-certificate.pdf', '')}" target="_blank" rel="noopener">Download sample (PDF)</a></div>
<div class="card" id="rdf"><span class="pill">PDF · 2 pages</span><h3 style="margin-top:10px">Remittance Details Form (RDF)</h3><p class="muted">Fill it in, sign it and send it to us on WhatsApp or email. It gives our CA everything needed to start.</p><a class="btn btn-primary" href="{b.asset('assets/downloads/remittance-details-form.pdf', '')}" target="_blank" rel="noopener">Download RDF (PDF)</a></div>
<div class="card"><span class="pill">12 banks</span><h3 style="margin-top:10px">Bank remittance forms</h3><p class="muted">Outward remittance request, Form A2 and NRO repatriation letters for Axis, HDFC, ICICI, SBI and more.</p><a class="btn btn-ghost" href="{L('bank-forms')}">Get bank forms</a></div>
</div></section>{cta_band(L)}""", priority="0.6")

    bank_opts = "".join(f"<option>{_h.escape(n)}</option>" for _, n in BANKS)
    bank_sel = '<div class="full"><label for="bf-bank">Which bank?</label><select id="bf-bank" name="bank" required><option value="">Select your bank</option>' + bank_opts + "</select></div>"
    page(slug="bank-forms", title="Bank remittance forms download: HDFC, ICICI, SBI, Axis",
         desc="Download outward remittance forms, Form A2 and NRO repatriation letters for 12 Indian banks, with the Form 145/146 checklist each bank asks for.",
         h1="Bank forms", body=lambda L: f"""
<section class="hero"><div class="wrap hero-grid" style="align-items:start"><div>
<p class="eyebrow">Download bank forms for remittance</p><h1>Remittance forms for your bank</h1>
<p class="lead">Every bank has its own outward remittance request, Form A2 format and NRO repatriation letter. Pick your bank and we send you the current set, with a checklist of what to attach.</p>
<div class="bank-chips">{''.join(f'<a href="{L("banks/" + s)}">{_h.escape(n)}</a>' for s, n in BANKS)}</div>
</div>{lead_form(L, heading="Get your bank's forms", sub="Instant download where available, otherwise on WhatsApp within one working hour.", purpose="Bank forms download", fid="bf", short=True, download=True, button="Get the forms", extra=bank_sel)}</div></section>
<section><div class="wrap prose"><h2>Why we send them rather than link them</h2><p>Banks update their forms without notice and branch versions differ. Sending the current set with a checklist saves you a rejected submission.</p></div></section>""", priority="0.8")

    page(slug="open-nri-account", title="Open an NRE or NRO account: which one and how | " + b.SITE_NAME,
         desc="Need an NRE or NRO account to receive or repatriate money? We help you pick the right account and prepare documents for your bank's opening process.",
         h1="Open NRE / NRO account", body=lambda L: f"""
<section class="hero"><div class="wrap hero-grid" style="align-items:start"><div>
<p class="eyebrow">Open NRE / NRO account</p><h1>The right account before the money moves</h1>
<p class="lead">Rent and sale proceeds must land in an NRO account; foreign earnings belong in NRE. Getting this right first makes Form 145/146 and repatriation simple later.</p>
<ul class="ticks"><li>Which account you need: NRE, NRO or both</li><li>Document checklist for your bank's own opening process</li><li>Help converting an old resident savings account to NRO</li></ul>
<p class="muted small">Accounts are opened by the bank through its official process. We do not take deposits and are not paid by banks to recommend them.</p>
</div>{lead_form(L, heading="Get help opening an account", sub="Tell us where you live; we suggest the account type and send the checklist.", purpose="Open NRE / NRO account", fid="oa", short=True, button="Help me open an account")}</div></section>
<section><div class="wrap"><h2>NRE vs NRO at a glance</h2><div class="table-wrap"><table><thead><tr><th></th><th>NRE</th><th>NRO</th></tr></thead><tbody>
<tr><td>Use it for</td><td>Money earned abroad</td><td>Income in India: rent, pension, dividends, sale proceeds</td></tr>
<tr><td>Interest</td><td>Tax-free in India</td><td>Taxable, TDS applies</td></tr><tr><td>Sending money back abroad</td><td>Free</td><td>Up to USD 1 million a year with Form 145/146</td></tr></tbody></table></div>
<p style="margin-top:14px"><a href="{L('guides/nro-vs-nre-repatriation')}">Read the full NRO vs NRE guide →</a></p></div></section>""", priority="0.6")

    page(slug="bank-rate-assistance", title="Get your bank's preferential rate on a large remittance",
         desc="Sending a large amount abroad? We help you ask your own bank for its preferential (corporate) rate. No live rates; your bank sets the rate and sends the money.",
         h1="Best rate in your bank", body=lambda L: f"""
<section class="hero"><div class="wrap hero-grid" style="align-items:start"><div>
<p class="eyebrow">Book the best rate in your bank</p><h1>Ask your bank for its preferential rate</h1>
<p class="lead">On large transfers, many banks can offer better than their standard card rate if you ask the right desk before submitting. We help you prepare the request and the paperwork together.</p>
<ul class="ticks"><li>Who to ask in your bank and when</li><li>Your Form 145/146 pack ready so the rate request is not wasted</li><li>Your bank sets the rate and sends the money; we only help with the request</li></ul>
<div class="note">We do not quote, compare or sell exchange rates, and we never handle or convert your money. Any rate is offered by your own bank.</div>
</div>{lead_form(L, heading="Help me ask my bank", sub="Tell us your bank and rough amount.", purpose="Preferential rate at my bank", fid="br")}</div></section>""", priority="0.5")
