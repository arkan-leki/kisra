/* Kisra Tech — site behaviour: clients wall, language, nav, reveal */
(() => {
  'use strict';

  /* ---------------- clients ---------------- */
  const CLIENTS = [
    ['shaz-print.png', 'Shaz Print'],
    ['jumla-iraq.png', 'Jumla Iraq'],
    ['ferga.png', 'Ferga'],
    ['poshyashop.png', 'Poshya'],
    ['garmian-university.png', 'Garmian University'],
    ['puk-kalar.png', 'PUK Kalar'],
    ['focus-organization.png', 'Focus Organization'],
    ['gashtkar.png', 'Gashtkar'],
    ['hawre-mkh.png', 'Hawre MKH'],
    ['mr-cafe.png', 'Mr. Cafe'],
    ['alam-al-sawaeq.png', 'Alam Al-Sawaeq'],
    ['brt-company.png', 'BRT Company'],
    ['electrical-point.png', 'Electrical Point'],
    ['master-electric.png', 'Master Electric'],
    ['rad-al-taqa-sulaymaniyah.png', 'Rad Al-Taqa'],
    ['sfrda-1.png', 'Sfrda'],
  ];

  const grid = document.getElementById('clientsGrid');
  if (grid) {
    grid.innerHTML = CLIENTS.map(([file, name]) =>
      `<div class="client" title="${name}"><img src="assets/clients/${file}" alt="${name}" loading="lazy"></div>`
    ).join('');
  }

  /* ---------------- language ---------------- */
  const html = document.documentElement;
  const btn = document.getElementById('langBtn');
  const saved = localStorage.getItem('kisra-lang');
  const qlang = new URLSearchParams(location.search).get('lang');
  if (qlang === 'en' || qlang === 'ckb') setLang(qlang);
  else if (saved === 'en') setLang('en');

  function setLang(lang) {
    html.lang = lang === 'en' ? 'en' : 'ckb';
    html.dir = lang === 'en' ? 'ltr' : 'rtl';
    if (btn) btn.textContent = lang === 'en' ? 'KU' : 'EN';
    localStorage.setItem('kisra-lang', lang);
  }
  if (btn) btn.addEventListener('click', () => {
    setLang(html.lang === 'en' ? 'ckb' : 'en');
  });

  /* ---------------- sticky nav + mobile menu ---------------- */
  const nav = document.getElementById('nav');
  const links = document.getElementById('navLinks');
  const burger = document.getElementById('burger');

  addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', scrollY > 8);
  }, { passive: true });

  if (burger && links) {
    burger.addEventListener('click', () => {
      const open = links.classList.toggle('open');
      burger.setAttribute('aria-expanded', String(open));
    });
    links.addEventListener('click', e => {
      if (e.target.closest('a')) {
        links.classList.remove('open');
        burger.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* ---------------- reveal on scroll ---------------- */
  const items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(entries => {
      for (const en of entries) {
        if (en.isIntersecting) {
          en.target.classList.add('in');
          io.unobserve(en.target);
        }
      }
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    items.forEach((el, i) => {
      el.style.transitionDelay = `${Math.min(i % 4, 3) * 60}ms`;
      io.observe(el);
    });
  } else {
    items.forEach(el => el.classList.add('in'));
  }

  /* ---------------- year ---------------- */
  const y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
