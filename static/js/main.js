/* ============================================================
   main.js — Portfolio JavaScript
   ============================================================ */

// ── 1. DARK MODE ──────────────────────────────────────────────
const html = document.documentElement;
const themeToggle = document.getElementById('themeToggle');

function applyTheme(theme) {
  html.setAttribute('data-theme', theme);
    if (theme === 'dark') {
    themeToggle.innerHTML = '<i class="bi bi-brightness-high"></i>';
  } else {
    themeToggle.innerHTML = '<i class="bi bi-moon-fill"></i>';
}
}
(function initTheme() {
  const saved = localStorage.getItem('theme');
  // Default is dark — only switch to light if explicitly saved
  applyTheme(saved === 'dark' ? 'dark' : 'light');
})();

themeToggle.addEventListener('click', () => {
  const current = html.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  applyTheme(next);
  localStorage.setItem('theme', next);
});

// ── 2. HAMBURGER MENU ─────────────────────────────────────────
const navbar = document.getElementById('navbar');
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');

hamburger.addEventListener('click', () => {
  navbar.classList.toggle('nav-open');
});

navLinks.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    navbar.classList.remove('nav-open');
  });
});

// ── 3. ACTIVE NAV LINK ────────────────────────────────────────
const allNavLinks = navLinks.querySelectorAll('a');

function setActiveLink(href) {
  allNavLinks.forEach(a => {
    a.classList.remove('active');
    if (a.getAttribute('href') === href) {
      a.classList.add('active');
    }
  });
}

function updateActiveFromPath() {
  const path = window.location.pathname;
  const hash = window.location.hash;

  if (path.startsWith('/projects/') && path.length > '/projects/'.length) {
    setActiveLink('/projects/');
  } else if (path === '/projects/') {
    setActiveLink('/projects/');
  } else if (path === '/about/') {
    setActiveLink('/about/');
  } else if (hash === '#skills') {
    setActiveLink('/#skills');
  } else if (hash === '#contact') {
    setActiveLink('/#contact');
  } else if (path === '/') {
    setActiveLink('/');
  } else {
    setActiveLink('');
  }
}

updateActiveFromPath();
window.addEventListener('hashchange', updateActiveFromPath);

// IntersectionObserver for active nav on scroll (home page only)
if (window.location.pathname === '/') {
  const sectionMap = {
    'hero': '/',
    'skills': '/#skills',
    'featured-projects': '/#skills',
    'contact': '/#contact',
  };

  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const href = sectionMap[entry.target.id];
        if (href) setActiveLink(href);
      }
    });
  }, { rootMargin: '-40% 0px -55% 0px', threshold: 0 });

  ['hero', 'skills', 'featured-projects', 'contact'].forEach(id => {
    const el = document.getElementById(id);
    if (el) sectionObserver.observe(el);
  });
}

// ── 4. SMOOTH SCROLL for anchor links ─────────────────────────
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const targetId = this.getAttribute('href').slice(1);
    const target = document.getElementById(targetId);
    if (target) {
      e.preventDefault();
      const top = target.getBoundingClientRect().top + window.scrollY - 70;
      window.scrollTo({ top, behavior: 'smooth' });
    }
  });
});

// ── 5. CROSS-PAGE SCROLL (hash on load) ───────────────────────
window.addEventListener('load', () => {
  if (window.location.hash && window.location.pathname === '/') {
    const target = document.getElementById(window.location.hash.slice(1));
    if (target) {
      setTimeout(() => {
        const top = target.getBoundingClientRect().top + window.scrollY - 70;
        window.scrollTo({ top, behavior: 'smooth' });
      }, 100);
    }
  }
});

// ── 6. NAVBAR SCROLL EFFECT ───────────────────────────────────
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 50);
}, { passive: true });

// ── 7. INTERSECTION OBSERVER ANIMATIONS ──────────────────────
const fadeEls = document.querySelectorAll('.fade-in');

if (fadeEls.length > 0) {
  const fadeObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        fadeObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  fadeEls.forEach((el) => {
    const siblings = Array.from(el.parentElement.querySelectorAll('.fade-in'));
    const idx = siblings.indexOf(el);
    el.style.transitionDelay = `${idx * 0.06}s`;
    fadeObserver.observe(el);
  });
}
