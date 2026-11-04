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

})();
