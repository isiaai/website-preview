/* Motion for the landing page. Runs only when <html> has the "motion" class (set in <head>
   unless the visitor prefers reduced motion). Without it the page is fully static. */
(() => {
  window.claraiMotion = true;
  if (!document.documentElement.classList.contains('motion')) return;

  // sections and cards fade in once as they scroll into view
  const reveal = new IntersectionObserver(entries => entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); reveal.unobserve(e.target); }
  }), { rootMargin: '0px 0px -8% 0px', threshold: 0.15 });
  document.querySelectorAll('.reveal').forEach(el => reveal.observe(el));

  // hero: the AI logbook fills itself – entry types in, gets sealed, coaching tip appears, repeat
  const mock = document.querySelector('.mock');
  if (!mock) return;
  const rows = [...mock.querySelectorAll('.mock-list li')];
  const tip = mock.querySelector('.mock-tip');
  const btn = mock.querySelector('.mock-btn');

  // pause while the mock is off screen or the tab is in the background
  let visible = true, wake = null;
  const resume = () => { if (wake) { wake(); wake = null; } };
  new IntersectionObserver(([e]) => { visible = e.isIntersecting; if (visible) resume(); }).observe(mock);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) resume(); });
  const gate = async () => { while (!visible || document.hidden) await new Promise(r => { wake = r; }); };
  const wait = async ms => { await gate(); await new Promise(r => setTimeout(r, ms)); };

  async function type(box, speed) {
    const out = box.querySelector('.typed'), text = box.querySelector('.full').textContent;
    out.classList.add('typing');
    for (let i = 1; i <= text.length; i++) {
      out.textContent = text.slice(0, i);
      await wait(speed + Math.random() * speed);
    }
    out.classList.remove('typing');
  }

  async function play() {
    await wait(900);                       // let the hero intro settle first
    for (;;) {
      for (const row of rows) {
        row.classList.add('on');
        await wait(300);
        await type(row.querySelector('.prompt'), 22);
        await wait(300);
        row.classList.add('sealed-on');
        await wait(650);
      }
      tip.classList.add('on');
      await wait(300);
      await type(tip.querySelector('.tip-text'), 20);
      await wait(400);
      btn.classList.add('pulse');
      await wait(4200);
      // fade everything out, then start over
      [...rows, tip].forEach(el => el.classList.remove('on', 'sealed-on'));
      btn.classList.remove('pulse');
      await wait(600);
      mock.querySelectorAll('.typed').forEach(el => { el.textContent = ''; });
      await wait(400);
    }
  }
  mock.classList.add('live');
  play();
})();
