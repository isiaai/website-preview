"""Builds the static isiaai.com landing page (EN at /, DE at /de/) plus Impressum and Datenschutz.
Run: python3 build.py
Structure follows "20261030_ISIaAI_Website_Plan_and_Our_Story" (Jule, v0.3, 30 Oct 2026):
Hero -> Problem (two parts) -> How it works -> Who we are -> Contact -> Footer.
"""
import os

# ---- settings you will want to change -------------------------------------------------
BOOKING_URL = ''            # Isaac's booking link. Empty = "Book an appointment" opens an email instead.
LINKEDIN_URL = 'https://www.linkedin.com/company/isiai'   # check spelling (isiai vs isiaai)
EMAIL = 'hello@isiaai.com'
TEAM_PHOTO = ''             # e.g. '/assets/team.jpg' – empty shows a placeholder
# ---------------------------------------------------------------------------------------

def mailto(subject):
    return f"mailto:{EMAIL}?subject={subject.replace(' ', '%20')}"

CHECK = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M5 10.5l3 3 7-7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

SEAL = '''<svg class="seal" viewBox="0 0 120 120" role="img" aria-label="{label}">
<circle cx="60" cy="60" r="57" fill="#13302D"/><circle cx="60" cy="60" r="49" fill="none" stroke="#2DD4BF" stroke-width="1.5" stroke-dasharray="2 3"/>
<defs><path id="sealArc{id}" d="M60 60 m-40 0 a40 40 0 1 1 80 0"/><path id="sealArcB{id}" d="M60 60 m-40 0 a40 40 0 1 0 80 0"/></defs>
<text font-family="Inter,sans-serif" font-size="9.5" font-weight="600" letter-spacing="1.7" fill="#FFFFFF"><textPath href="#sealArc{id}" startOffset="50%" text-anchor="middle">{top}</textPath></text>
<text font-family="Inter,sans-serif" font-size="9.5" font-weight="600" letter-spacing="1.7" fill="#FFD60A"><textPath href="#sealArcB{id}" startOffset="50%" text-anchor="middle" dominant-baseline="hanging">{bottom}</textPath></text>
<g transform="translate(42 38) scale(.1)"><path d="M95 8L182 58L95 108L8 58Z" fill="#C2F7EC"/><path d="M8 58L95 108L95 208L8 158Z" fill="#2DD4BF"/><path d="M95 108L182 58L182 158L95 208Z" fill="#127068"/><path d="M269 8L356 58L269 108L182 58Z" fill="#C2F7EC"/><path d="M182 58L269 108L269 208L182 158Z" fill="#2DD4BF"/><path d="M269 108L356 58L356 158L269 208Z" fill="#127068"/><path d="M182 158L269 208L182 258L95 208Z" fill="#C2F7EC"/><path d="M95 208L182 258L182 358L95 308Z" fill="#2DD4BF"/><path d="M182 258L269 208L269 308L182 358Z" fill="#127068"/></g>
<text x="60" y="88" text-anchor="middle" font-family="Outfit,sans-serif" font-size="10" font-weight="600" fill="#FFFFFF">{mid}</text>
</svg>'''

T = {
'en': dict(
 title='Clarai by ISIaAI – Use AI well. Prove it’s yours.',
 desc='Clarai is software that helps you use AI well and show what is your own work – built by a team in Germany.',
 nav_problem='Why Clarai', nav_how='How it works', nav_who='Who we are', nav_contact='Contact', menu='Menu',
 book='Book an appointment', pilot='Join the pilot',
 hero_eyebrow='Clarai by ISIaAI · Stay human in an AI world',
 hero_title='Use AI well.<br><em>Prove it’s yours.</em>',
 hero_sub='Clarai is software that helps you get better results from AI and show which part of the work is your own – built by a team in Germany.',
 seal_top='AI KNOW-HOW', seal_mid='MADE IN', seal_bottom='GERMANY', seal_label='AI know-how made in Germany',
 mock_label='Illustration of Clarai', mock_title='My AI logbook', mock_sub='Only visible to you',
 mock_rows=[('ChatGPT','Summarise Q3 delivery times per region in 5 bullet points','10:42'),
            ('Claude','Draft two options for renegotiating payment terms','11:15'),
            ('Copilot','Check this paragraph for unclear wording','14:03')],
 mock_sealed='Sealed', mock_tip_t='Coaching tip', mock_tip='Add the format you want – e.g. “as a table with 3 columns”.',
 mock_btn='Create report',
 pr_eyebrow='The problem', pr_title='AI helps every day. But two things are still hard.',
 pr1_t='Using AI well', pr1_b='The prompt that worked last month is lost in an old chat. Results vary from person to person, and nobody shows you how to get better.',
 pr2_t='Proving what’s yours', pr2_b='Your team lead or client asks how AI was used. Nobody can show which part of the work is really your own.',
 how_eyebrow='How it works', how_title='Two technologies. One for each problem.',
 how_sub='Clarai runs in your browser while you use ChatGPT, Claude, Copilot or Gemini as usual.',
 co_for='Solves: using AI well', co_t='Coaching', co_h='Better prompts. Better results.',
 co_b='Coaching gives you instant feedback on your prompts and shows you how to get better results from AI.',
 co_l=['Better results, faster','Skills that grow','Less trial and error'],
 fp_for='Solves: proving what’s yours', fp_t='Fingerprint', fp_h='Your work, verified.',
 fp_b='Fingerprint records each AI interaction while you work and seals it, so you can always show how a result came about. You see every entry and decide what you share.',
 fp_l=['Prove your contribution','Nothing to reconstruct','Private by default'],
 pilot_t='We’re looking for teams to test Clarai with us.', pilot_b='Use it in your daily work for a few weeks and tell us what helps and what doesn’t.',
 who_eyebrow='Who we are', who_title='How do people and AI work well together?',
 photo_t='Team photo coming soon', photo_b='Our team in Germany',
 who_p1='ISIaAI is a project based in Germany. We are an interdisciplinary team from business, research and software development, united by one question: how can people and AI work well together?',
 who_p2='AI is changing the way we work every day. We believe that in all of this, the human contribution should stay visible and valued. That’s what we’re working on, with our first product, Clarai.',
 logo_q='Where our three cubes meet, a fourth one appears. It only exists because the three come together.',
 logo_c='The idea behind our logo: together, we create more than any part alone.',
 c_eyebrow='Contact', c_title='Be part of it.',
 c_body='We’re building this together with the people who use AI in their work. Test Clarai, share your experience or simply follow our journey.',
 c_mail='Or write to us:',
 foot_about='Clarai by ISIaAI – software that helps people use AI well and prove their own part.',
 foot_aiact='Built in Germany with the EU AI Act in mind.',
 foot_legal='Legal', foot_contact='Contact', imprint='Impressum', privacy='Privacy',
 subj_book='Appointment request', subj_pilot='Join the Clarai pilot',
),
'de': dict(
 title='Clarai by ISIaAI – KI gut nutzen. Zeigen, was deins ist.',
 desc='Clarai ist eine Software, die dir hilft, KI gut zu nutzen und zu zeigen, was deine eigene Arbeit ist – entwickelt von einem Team in Deutschland.',
 nav_problem='Warum Clarai', nav_how='So funktioniert’s', nav_who='Wer wir sind', nav_contact='Kontakt', menu='Menü',
 book='Termin buchen', pilot='Beim Pilot mitmachen',
 hero_eyebrow='Clarai by ISIaAI · Mensch bleiben in der KI-Welt',
 hero_title='KI gut nutzen.<br><em>Zeigen, was deins ist.</em>',
 hero_sub='Clarai ist eine Software, die dir hilft, bessere Ergebnisse mit KI zu erzielen und zu zeigen, welcher Teil der Arbeit von dir stammt – entwickelt von einem Team in Deutschland.',
 seal_top='KI-KNOW-HOW', seal_mid='MADE IN', seal_bottom='GERMANY', seal_label='KI-Know-how made in Germany',
 mock_label='Illustration von Clarai', mock_title='Mein KI-Logbuch', mock_sub='Nur für dich sichtbar',
 mock_rows=[('ChatGPT','Fasse die Lieferzeiten aus Q3 je Region in 5 Stichpunkten zusammen','10:42'),
            ('Claude','Entwirf zwei Optionen für neue Zahlungsbedingungen','11:15'),
            ('Copilot','Prüfe diesen Absatz auf unklare Formulierungen','14:03')],
 mock_sealed='Versiegelt', mock_tip_t='Coaching-Tipp', mock_tip='Nenne das gewünschte Format – z. B. „als Tabelle mit 3 Spalten“.',
 mock_btn='Bericht erstellen',
 pr_eyebrow='Das Problem', pr_title='KI hilft jeden Tag. Aber zwei Dinge sind noch schwer.',
 pr1_t='KI gut nutzen', pr1_b='Der Prompt, der letzten Monat funktioniert hat, ist in einem alten Chat verschwunden. Die Ergebnisse sind von Person zu Person verschieden, und niemand zeigt dir, wie es besser geht.',
 pr2_t='Zeigen, was deins ist', pr2_b='Deine Teamleitung oder dein Kunde fragt, wie KI genutzt wurde. Niemand kann zeigen, welcher Teil der Arbeit wirklich von dir ist.',
 how_eyebrow='So funktioniert’s', how_title='Zwei Technologien. Eine für jedes Problem.',
 how_sub='Clarai läuft in deinem Browser, während du ChatGPT, Claude, Copilot oder Gemini wie gewohnt nutzt.',
 co_for='Löst: KI gut nutzen', co_t='Coaching', co_h='Bessere Prompts. Bessere Ergebnisse.',
 co_b='Coaching gibt dir sofort Feedback zu deinen Prompts und zeigt dir, wie du bessere Ergebnisse mit KI erzielst.',
 co_l=['Schneller bessere Ergebnisse','Wachsende Fähigkeiten','Weniger Ausprobieren'],
 fp_for='Löst: zeigen, was deins ist', fp_t='Fingerprint', fp_h='Deine Arbeit, belegt.',
 fp_b='Fingerprint zeichnet jede KI-Interaktion während der Arbeit auf und versiegelt sie, damit du jederzeit zeigen kannst, wie ein Ergebnis entstanden ist. Du siehst jeden Eintrag und entscheidest, was du teilst.',
 fp_l=['Deinen Beitrag belegen','Nichts rekonstruieren','Standardmäßig privat'],
 pilot_t='Wir suchen Teams, die Clarai mit uns testen.', pilot_b='Nutze es ein paar Wochen in deiner täglichen Arbeit und sag uns, was hilft und was nicht.',
 who_eyebrow='Wer wir sind', who_title='Wie arbeiten Mensch und KI gut zusammen?',
 photo_t='Teamfoto folgt bald', photo_b='Unser Team in Deutschland',
 who_p1='ISIaAI ist ein Projekt mit Sitz in Deutschland. Wir sind ein interdisziplinäres Team aus Business, Forschung und Softwareentwicklung, verbunden durch eine Frage: Wie können Menschen und KI gut zusammenarbeiten?',
 who_p2='KI verändert jeden Tag, wie wir arbeiten. Wir glauben, dass dabei der menschliche Beitrag sichtbar und wertgeschätzt bleiben soll. Daran arbeiten wir – mit unserem ersten Produkt, Clarai.',
 logo_q='Wo sich unsere drei Würfel treffen, entsteht ein vierter. Er existiert nur, weil die drei zusammenkommen.',
 logo_c='Die Idee hinter unserem Logo: Gemeinsam schaffen wir mehr als jeder Teil allein.',
 c_eyebrow='Kontakt', c_title='Sei dabei.',
 c_body='Wir entwickeln das gemeinsam mit den Menschen, die KI in ihrer Arbeit nutzen. Teste Clarai, teile deine Erfahrungen oder verfolge einfach unseren Weg.',
 c_mail='Oder schreib uns:',
 foot_about='Clarai by ISIaAI – Software, die Menschen hilft, KI gut zu nutzen und den eigenen Anteil zu belegen.',
 foot_aiact='Entwickelt in Deutschland, mit Blick auf den EU AI Act.',
 foot_legal='Rechtliches', foot_contact='Kontakt', imprint='Impressum', privacy='Datenschutz',
 subj_book='Terminanfrage', subj_pilot='Beim Clarai-Pilot mitmachen',
)}

def head(t, lang, path, noindex=False):
    robots = '<meta name="robots" content="noindex">\n' if noindex else ''
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
{robots}<title>{t['title']}</title>
<meta name="description" content="{t['desc']}">
<meta property="og:title" content="{t['title']}">
<meta property="og:description" content="{t['desc']}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://isiaai.com{path}">
<link rel="canonical" href="https://isiaai.com{path}">
<link rel="alternate" hreflang="en" href="https://isiaai.com/">
<link rel="alternate" hreflang="de" href="https://isiaai.com/de/">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/outfit-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/styles.css">
</head>
<body>'''

def book_href(t):
    return BOOKING_URL or mailto(t['subj_book'])

def nav(t, lang, home):
    pre = '' if home else ('/' if lang == 'en' else '/de/')
    ext = ' target="_blank" rel="noopener"' if BOOKING_URL else ''
    return f'''
<a class="skip" href="#main">{'Skip to content' if lang=='en' else 'Zum Inhalt springen'}</a>
<header class="nav">
  <div class="wrap">
    <a class="logo" href="{'/' if lang=='en' else '/de/'}" aria-label="ISIaAI – home"><img src="/assets/isiaai-logo.svg" alt="ISIaAI" width="82" height="30"></a>
    <nav class="links" id="links" aria-label="Main">
      <a href="{pre}#problem">{t['nav_problem']}</a>
      <a href="{pre}#how">{t['nav_how']}</a>
      <a href="{pre}#who">{t['nav_who']}</a>
      <a href="{pre}#contact">{t['nav_contact']}</a>
    </nav>
    <div class="nav-r">
      <div class="lang" aria-label="Language"><a href="/" hreflang="en" aria-current="{'true' if lang=='en' else 'false'}">EN</a><a href="/de/" hreflang="de" aria-current="{'true' if lang=='de' else 'false'}">DE</a></div>
      <a class="btn btn-teal" href="{book_href(t)}"{ext}>{t['book']}</a>
      <button class="menu-btn" type="button" id="menuBtn" aria-expanded="false" aria-controls="links">{t['menu']}</button>
    </div>
  </div>
</header>'''

def footer(t, lang):
    return f'''
<footer>
  <div class="wrap">
    <div class="f-grid">
      <div class="f-brand">
        <img src="/assets/isiaai-logo-on-dark.svg" alt="ISIaAI" width="82" height="30">
        <p>{t['foot_about']}</p>
        <p class="f-aiact">{t['foot_aiact']}</p>
      </div>
      <div>{SEAL.format(id='f', top=t['seal_top'], mid=t['seal_mid'], bottom=t['seal_bottom'], label=t['seal_label'])}</div>
      <div><h4>{t['foot_legal']}</h4><ul>
        <li><a href="/impressum/">{t['imprint']}</a></li><li><a href="/datenschutz/">{t['privacy']}</a></li></ul></div>
      <div><h4>{t['foot_contact']}</h4><ul>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="{LINKEDIN_URL}" target="_blank" rel="noopener">LinkedIn</a></li></ul></div>
    </div>
    <div class="f-bottom"><span>© 2026 ISIaAI · Inspire Sustainable Innovation for applied Artificial Intelligence</span></div>
  </div>
</footer>
<script>
const b=document.getElementById('menuBtn');
b.addEventListener('click',()=>{{const o=document.body.classList.toggle('menu-open');b.setAttribute('aria-expanded',o);}});
document.querySelectorAll('#links a').forEach(a=>a.addEventListener('click',()=>{{document.body.classList.remove('menu-open');b.setAttribute('aria-expanded','false');}}));
</script>
</body>
</html>
'''

def checks(items):
    return '<ul class="checks">' + ''.join(f'<li>{CHECK}<span>{x}</span></li>' for x in items) + '</ul>'

def mock(t):
    rows = ''.join(f'<li><span class="tool">{a}</span><span class="prompt">{b}</span><span class="time">{c}</span><span class="sealed">{t["mock_sealed"]}</span></li>' for a, b, c in t['mock_rows'])
    return f'''<figure class="mock" aria-label="{t['mock_label']}">
  <div class="mock-bar"><i></i><i></i><i></i><span>Clarai</span></div>
  <div class="mock-body">
    <div class="mock-head"><div><b>{t['mock_title']}</b><small>{t['mock_sub']}</small></div><img src="/assets/pawprint-mark.svg" alt="" width="34" height="34"></div>
    <ul class="mock-list">{rows}</ul>
    <div class="mock-tip"><b>{t['mock_tip_t']}</b>{t['mock_tip']}</div>
    <div class="mock-foot"><span class="mock-btn">{t['mock_btn']}</span></div>
  </div>
  <figcaption>{t['mock_label']}</figcaption>
</figure>'''

def landing(lang):
    t = T[lang]
    ext = ' target="_blank" rel="noopener"' if BOOKING_URL else ''
    pilot = mailto(t['subj_pilot'])
    photo = f'<img src="{TEAM_PHOTO}" alt="{t["photo_b"]}">' if TEAM_PHOTO else f'<div><b>{t["photo_t"]}</b>{t["photo_b"]}</div>'
    seal = SEAL.format(id='h', top=t['seal_top'], mid=t['seal_mid'], bottom=t['seal_bottom'], label=t['seal_label'])
    return head(t, lang, '/' if lang == 'en' else '/de/') + nav(t, lang, True) + f'''
<main id="main">
  <section class="hero">
    <div class="wrap hero-grid">
      <div class="hero-copy">
        <p class="eyebrow">{t['hero_eyebrow']}</p>
        <h1>{t['hero_title']}</h1>
        <p class="lead">{t['hero_sub']}</p>
        <div class="ctas">
          <a class="btn btn-teal btn-arrow" href="{book_href(t)}"{ext}>{t['book']}</a>
          <a class="btn btn-line" href="{pilot}">{t['pilot']}</a>
        </div>
        <div class="hero-seal">{seal}</div>
      </div>
      {mock(t)}
    </div>
  </section>

  <section class="sec paper" id="problem">
    <div class="wrap">
      <p class="eyebrow">{t['pr_eyebrow']}</p>
      <h2 class="h2">{t['pr_title']}</h2>
      <div class="problems">
        <article class="problem"><span class="pnum">1</span><h3>{t['pr1_t']}</h3><p>{t['pr1_b']}</p></article>
        <article class="problem"><span class="pnum">2</span><h3>{t['pr2_t']}</h3><p>{t['pr2_b']}</p></article>
      </div>
    </div>
  </section>

  <section class="sec tech" id="how">
    <div class="wrap">
      <div class="sec-head"><div><p class="eyebrow">{t['how_eyebrow']}</p><h2>{t['how_title']}</h2></div><p class="lead">{t['how_sub']}</p></div>
      <div class="mvps">
        <article class="mvp">
          <span class="tag">{t['co_for']}</span>
          <p class="mvp-name">{t['co_t']}</p><h3>{t['co_h']}</h3><p>{t['co_b']}</p>{checks(t['co_l'])}
        </article>
        <article class="mvp">
          <span class="tag">{t['fp_for']}</span>
          <p class="mvp-name">{t['fp_t']}</p><h3>{t['fp_h']}</h3><p>{t['fp_b']}</p>{checks(t['fp_l'])}
        </article>
      </div>
      <div class="pilotbox">
        <div><h3>{t['pilot_t']}</h3><p>{t['pilot_b']}</p></div>
        <a class="btn btn-yellow btn-arrow" href="{pilot}">{t['pilot']}</a>
      </div>
    </div>
  </section>

  <section class="sec paper" id="who">
    <div class="wrap">
      <p class="eyebrow">{t['who_eyebrow']}</p>
      <h2 class="h2">{t['who_title']}</h2>
      <div class="photo" id="team-photo">{photo}</div>
      <div class="who-grid">
        <div class="who-text"><p>{t['who_p1']}</p><p>{t['who_p2']}</p></div>
        <figure class="logoquote">
          <svg viewBox="0 0 364 366" aria-hidden="true"><path d="M95 8L182 58L95 108L8 58Z" fill="#C2F7EC"/><path d="M8 58L95 108L95 208L8 158Z" fill="#2DD4BF"/><path d="M95 108L182 58L182 158L95 208Z" fill="#127068"/><path d="M269 8L356 58L269 108L182 58Z" fill="#C2F7EC"/><path d="M182 58L269 108L269 208L182 158Z" fill="#2DD4BF"/><path d="M269 108L356 58L356 158L269 208Z" fill="#127068"/><path d="M182 158L269 208L182 258L95 208Z" fill="#C2F7EC"/><path d="M95 208L182 258L182 358L95 308Z" fill="#2DD4BF"/><path d="M182 258L269 208L269 308L182 358Z" fill="#127068"/></svg>
          <blockquote>“{t['logo_q']}”</blockquote>
          <figcaption>{t['logo_c']}</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="sec" id="contact">
    <div class="wrap">
      <div class="cta">
        <div><p class="eyebrow">{t['c_eyebrow']}</p><h2>{t['c_title']}</h2><p>{t['c_body']}</p>
          <p class="mailline">{t['c_mail']} <a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
        <div class="ctas">
          <a class="btn btn-yellow btn-arrow" href="{book_href(t)}"{ext}>{t['book']}</a>
          <a class="btn btn-line" href="{pilot}">{t['pilot']}</a>
        </div>
      </div>
    </div>
  </section>
</main>''' + footer(t, lang)

TODO = lambda s: f'<span class="todo">[{s}]</span>'
IMPRESSUM = f'''<main class="sec" id="main"><div class="wrap legal">
<h1>Impressum</h1>
<p>Angaben gemäß § 5 DDG</p>
<p>ISIaAI {TODO('Rechtsform, z. B. GmbH / UG')}<br>{TODO('Straße und Hausnummer')}<br>{TODO('PLZ Ort')}<br>Deutschland</p>
<h2>Vertreten durch</h2><p>{TODO('Geschäftsführer:in')}</p>
<h2>Kontakt</h2><p>E-Mail: <a href="mailto:{EMAIL}">{EMAIL}</a><br>Telefon: {TODO('Telefonnummer')}</p>
<h2>Registereintrag</h2><p>Registergericht: {TODO('Amtsgericht')}<br>Registernummer: {TODO('HRB …')}</p>
<h2>Umsatzsteuer-ID</h2><p>{TODO('USt-IdNr. gemäß § 27a UStG, falls vorhanden')}</p>
<h2>Verantwortlich für den Inhalt</h2><p>{TODO('Name, Anschrift')} (§ 18 Abs. 2 MStV)</p>
</div></main>'''
DATENSCHUTZ = f'''<main class="sec" id="main"><div class="wrap legal">
<h1>Datenschutzerklärung</h1>
<p>{TODO('Entwurf – bitte vor Veröffentlichung von Alina / rechtlich prüfen lassen')}</p>
<h2>1. Verantwortliche Stelle</h2><p>ISIaAI, {TODO('Anschrift')}, E-Mail: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<h2>2. Hosting</h2><p>Diese Website wird bei Cloudflare, Inc. gehostet. Beim Aufruf verarbeitet der Hoster technisch notwendige Daten (z. B. IP-Adresse, Zeitpunkt, aufgerufene Seite), um die Website auszuliefern und abzusichern (Art. 6 Abs. 1 lit. f DSGVO). {TODO('Details und Auftragsverarbeitungsvertrag ergänzen')}</p>
<h2>3. Cookies und Tracking</h2><p>Wir setzen keine Cookies, keine Analyse-Tools und keine Tracking-Dienste ein. Schriftarten werden lokal von unserem Server geladen.</p>
<h2>4. Kontakt per E-Mail</h2><p>Wenn du uns per E-Mail schreibst oder einen Termin anfragst, verarbeiten wir deine Angaben, um deine Anfrage zu beantworten (Art. 6 Abs. 1 lit. b DSGVO). Wir löschen die Daten, wenn sie dafür nicht mehr nötig sind. {TODO('Speicherdauer, Buchungstool ergänzen')}</p>
<h2>5. Deine Rechte</h2><p>Du hast das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch sowie das Recht, dich bei einer Datenschutz-Aufsichtsbehörde zu beschweren.</p>
<p>Stand: Oktober 2026</p>
</div></main>'''

def legal(body, title, path):
    t = dict(T['de']); t['title'] = f'{title} – ISIaAI'
    return head(t, 'de', path, noindex=True) + nav(t, 'de', False) + body + footer(t, 'de')

def w(path, s):
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    open(path, 'w', encoding='utf-8').write(s)

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    w('index.html', landing('en'))
    w('de/index.html', landing('de'))
    w('impressum/index.html', legal(IMPRESSUM, 'Impressum', '/impressum/'))
    w('datenschutz/index.html', legal(DATENSCHUTZ, 'Datenschutz', '/datenschutz/'))
    print('built')
