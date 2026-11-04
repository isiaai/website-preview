/* Motion for the landing page (scroll reveals; the hero entrance is pure CSS). Runs only when <html> has the "motion" class (set in <head>
   unless the visitor prefers reduced motion). Without it the page is fully static. */
(() => {
  window.claraiMotion = true;
  if (!document.documentElement.classList.contains('motion')) return;

  // sections and cards fade in once as they scroll into view
  const reveal = new IntersectionObserver(entries => entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); reveal.unobserve(e.target); }
  }), { rootMargin: '0px 0px -8% 0px', threshold: 0.15 });
  document.querySelectorAll('.reveal').forEach(el => reveal.observe(el));

  // scroll-linked: jellyfish swim up into their cards, the three logo cubes fly together
  const items = [
    ...[...document.querySelectorAll('.mvp-ico')].map(el => ({ el, start: .95, end: .55, done: 'settled' })),
    ...[...document.querySelectorAll('.logoquote')].map(el => ({ el, start: 1, end: .5, done: 'joined' })),
  ];
  let ticking = false;
  function update() {
    ticking = false;
    const vh = innerHeight;
    for (const it of items) {
      const top = it.el.getBoundingClientRect().top / vh;          // 1 = at the bottom edge, 0 = at the top
      const p = Math.min(1, Math.max(0, (it.start - top) / (it.start - it.end)));
      it.el.style.setProperty('--p', p.toFixed(3));
      it.el.classList.toggle(it.done, p >= 1);
    }
  }
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll);
  update();
})();
