// ══════════════════════════════════════════════
//  PORTFOLIO — script.js
// ══════════════════════════════════════════════

// ── NAVBAR SCROLL EFFECT ──────────────────────
const navbar = document.getElementById('navbar');

window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 50);
  highlightActiveLink();
});

// ── HAMBURGER TOGGLE ──────────────────────────
const hamburger = document.getElementById('hamburger');
const navLinks  = document.getElementById('navLinks');

hamburger.addEventListener('click', () => {
  navLinks.classList.toggle('open');
});

// Close menu on link click
navLinks.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => navLinks.classList.remove('open'));
});

// ── ACTIVE NAV LINK ON SCROLL ─────────────────
function highlightActiveLink() {
  const sections = document.querySelectorAll('section[id]');
  const links    = document.querySelectorAll('.nav-links a');
  let current    = '';

  sections.forEach(section => {
    if (window.scrollY >= section.offsetTop - 140) {
      current = section.id;
    }
  });

  links.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') === '#' + current) {
      link.classList.add('active');
    }
  });
}

// ── SKILL BARS — animate when visible ─────────
function animateSkillBars(entries, observer) {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const bar = entry.target.querySelector('.skill-fill');
      if (bar) {
        bar.style.width = bar.dataset.level + '%';
      }
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}

const skillObserver = new IntersectionObserver(animateSkillBars, { threshold: 0.2 });
document.querySelectorAll('.skill-card').forEach((card, i) => {
  card.style.transitionDelay = (i * 60) + 'ms';
  skillObserver.observe(card);
});

// ── FADE IN PROJECT & EDU CARDS ON SCROLL ─────
function fadeInCards(entries, observer) {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => entry.target.classList.add('visible'), i * 80);
      observer.unobserve(entry.target);
    }
  });
}

const cardObserver = new IntersectionObserver(fadeInCards, { threshold: 0.1 });

document.querySelectorAll('.project-card, .edu-card').forEach(el => {
  cardObserver.observe(el);
});
