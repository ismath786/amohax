// main.js

document.addEventListener('DOMContentLoaded', () => {
  const toggleButton = document.querySelector('.menu-toggle');
  const navLinks = document.querySelector('.nav-links');
  const navLinkItems = document.querySelectorAll('.nav-links a');

  function openMenu() {
    navLinks.classList.add('open');
    toggleButton.setAttribute('aria-expanded', 'true');
    toggleButton.setAttribute('aria-label', 'Close menu');
  }

  function closeMenu() {
    navLinks.classList.remove('open');
    toggleButton.setAttribute('aria-expanded', 'false');
    toggleButton.setAttribute('aria-label', 'Open menu');
  }

  toggleButton.addEventListener('click', () => {
    const expanded = toggleButton.getAttribute('aria-expanded') === 'true';
    if (expanded) {
      closeMenu();
    } else {
      openMenu();
    }
  });

  // Close menu when any nav link is clicked (on mobile)
  navLinkItems.forEach(link => {
    link.addEventListener('click', () => {
      if (window.innerWidth <= 768) {
        closeMenu();
      }
    });
  });

  // Optional: close menu when clicking outside (mobile)
  document.addEventListener('click', (e) => {
    if (window.innerWidth <= 768) {
      const isClickInside = e.target.closest('nav.navbar');
      if (!isClickInside && navLinks.classList.contains('open')) {
        closeMenu();
      }
    }
  });

  // Handle window resize — reset menu as per screen width
  window.addEventListener('resize', () => {
    if (window.innerWidth > 768) {
      navLinks.classList.remove('open');
      navLinks.style.maxHeight = null;
      toggleButton.setAttribute('aria-expanded', 'false');
      toggleButton.setAttribute('aria-label', 'Open menu');
    }
  });
});
