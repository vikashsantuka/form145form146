/* NRI Foundation site script: mobile menu, UTM capture, lead form submission to the CRM (Supabase). */
(function () {
  var CFG = window.NRIF_CONFIG || {};

  // Mobile menu
  var t = document.querySelector('.menu-toggle');
  var nav = document.getElementById('site-nav');
  if (t && nav) t.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    t.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  // Remember first-touch attribution for this visit
  function store(k, v) { try { sessionStorage.setItem(k, v); } catch (e) {} }
  function read(k) { try { return sessionStorage.getItem(k) || ''; } catch (e) { return ''; } }
  var qs = new URLSearchParams(location.search);
  ['utm_source', 'utm_medium', 'utm_campaign', 'ref'].forEach(function (k) {
    if (qs.get(k) && !read('nrif_' + k)) store('nrif_' + k, qs.get(k).slice(0, 100));
  });
  if (!read('nrif_landing')) store('nrif_landing', location.pathname);
  if (!read('nrif_referrer') && document.referrer && document.referrer.indexOf(location.host) === -1) store('nrif_referrer', document.referrer.slice(0, 300));

  var cfgScript = document.querySelector('script[src$="assets/config.js"]');
  var BASE = cfgScript ? cfgScript.src.replace(/assets\/config\.js.*$/, '') : '/';

  // Analytics (only if IDs are set in build.py)
  if (CFG.ga4) {
    var g = document.createElement('script'); g.async = true; g.src = 'https://www.googletagmanager.com/gtag/js?id=' + CFG.ga4; document.head.appendChild(g);
    window.dataLayer = window.dataLayer || []; window.gtag = function () { dataLayer.push(arguments); }; gtag('js', new Date()); gtag('config', CFG.ga4);
  }
  if (CFG.metaPixel) {
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', CFG.metaPixel); fbq('track', 'PageView');
  }

  // "Transfer funds to <country>" picker
  document.querySelectorAll('form.country-picker').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var v = f.querySelector('select').value;
      var msg = f.querySelector('.form-msg');
      if (!v) { if (msg) msg.textContent = 'Select a destination country to continue.'; return; }
      location.href = v;
    });
  });

  function waLink(text) {
    return 'https://wa.me/' + (CFG.whatsapp || '') + '?text=' + encodeURIComponent('[Form145Form146] ' + text);
  }

  document.querySelectorAll('form.lead-form').forEach(function (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var msg = form.querySelector('.form-msg');
      var btn = form.querySelector('button[type="submit"]');
      var f = new FormData(form);
      if (f.get('website')) return; // honeypot
      var name = (f.get('name') || '').toString().trim();
      var phone = (f.get('phone') || '').toString().trim();
      var email = (f.get('email') || '').toString().trim();
      if (!name || (!phone && !email)) {
        msg.className = 'form-msg err';
        msg.textContent = 'Please add your name and a phone/WhatsApp number or email so we can reach you.';
        return;
      }
      var lead = {
        name: name.slice(0, 120),
        phone: phone.slice(0, 40) || null,
        email: email.slice(0, 200) || null,
        country: (f.get('country') || '').toString().slice(0, 60) || null,
        purpose: (f.get('purpose') || '').toString().slice(0, 60) || null,
        amount_band: (f.get('amount_band') || '').toString().slice(0, 40) || null,
        bank: (f.get('bank') || '').toString().slice(0, 60) || null,
        message: (function () {
          var m = (f.get('message') || '').toString();
          form.querySelectorAll('[name^="x_"]').forEach(function (el) {
            if (el.value) m += (m ? '\n' : '') + (el.getAttribute('data-label') || el.name.slice(2)) + ': ' + el.value;
          });
          return m.slice(0, 2000) || null;
        })(),
        lead_type: (f.get('lead_type') || 'nri').toString(),
        channel: read('nrif_ref') ? 'referral' : 'direct',
        source_page: location.pathname.slice(0, 300),
        landing_page: read('nrif_landing').slice(0, 300) || null,
        referrer: read('nrif_referrer') || null,
        utm_source: read('nrif_utm_source') || null,
        utm_medium: read('nrif_utm_medium') || null,
        utm_campaign: read('nrif_utm_campaign') || read('nrif_ref') || null
      };
      var summary = 'Hi, I need help with Form 145/146.\nName: ' + lead.name +
        (lead.country ? '\nCountry: ' + lead.country : '') +
        (lead.purpose ? '\nPurpose: ' + lead.purpose : '') +
        (lead.amount_band ? '\nAmount: ' + lead.amount_band : '') +
        (lead.bank ? '\nBank: ' + lead.bank : '');
      btn.disabled = true; btn.textContent = 'Sending…';

      function done(ok) {
        btn.disabled = false; btn.textContent = btn.getAttribute('data-label') || 'Submit';
        if (ok) {
          form.reset();
          msg.className = 'form-msg ok';
          msg.innerHTML = 'Thank you, ' + escapeHtml(name.split(' ')[0]) + '. A remittance specialist will call or WhatsApp you within one working day (IST). ' +
            'Want to start now? <a href="' + waLink(summary) + '" target="_blank" rel="noopener">Message us on WhatsApp</a>.';
          if (window.gtag) window.gtag('event', 'generate_lead', { purpose: lead.purpose || '' });
          if (window.fbq) window.fbq('track', 'Lead');
          if (form.hasAttribute('data-download')) {
            var files = (CFG.bankForms || {});
            var link = lead.bank && files[lead.bank];
            msg.innerHTML = link
              ? 'Thank you. <a href="' + BASE + link + '" target="_blank" rel="noopener"><b>Download the ' + escapeHtml(lead.bank) + ' remittance forms</b></a>. We will also WhatsApp you a filled-in checklist.'
              : 'Thank you. We will WhatsApp or email you the current ' + escapeHtml(lead.bank || 'bank') + ' remittance forms within one working hour (IST). <a href="' + waLink('Hi, please send me the ' + (lead.bank || '') + ' remittance forms. Name: ' + lead.name) + '" target="_blank" rel="noopener">Get them on WhatsApp now</a>.';
          }
        } else {
          msg.className = 'form-msg err';
          msg.innerHTML = 'We could not save your request just now. Please <a href="' + waLink(summary) + '" target="_blank" rel="noopener">send it on WhatsApp</a> or call ' + (CFG.phoneDisplay || '') + '.';
        }
      }
      if (!CFG.supabaseUrl || !CFG.supabaseKey) { done(false); return; }
      fetch(CFG.supabaseUrl + '/rest/v1/nrif_leads', {
        method: 'POST',
        headers: { 'apikey': CFG.supabaseKey, 'Content-Type': 'application/json', 'Prefer': 'return=minimal' },
        body: JSON.stringify(lead)
      }).then(function (r) { done(r.ok); }).catch(function () { done(false); });
    });
  });

  function escapeHtml(s) { return s.replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
})();
