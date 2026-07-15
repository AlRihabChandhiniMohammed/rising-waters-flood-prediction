/* =========================================================
   RISING WATERS — script.js
   ========================================================= */

document.addEventListener('DOMContentLoaded', () => {

  /* ---------- mobile nav toggle ---------- */
  const navToggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => {
      navToggle.classList.toggle('open');
      navLinks.classList.toggle('open');
    });
    navLinks.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => {
        navToggle.classList.remove('open');
        navLinks.classList.remove('open');
      });
    });
  }

  /* ---------- scroll reveal ---------- */
  const revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealEls.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });
    revealEls.forEach(el => io.observe(el));
  } else {
    revealEls.forEach(el => el.classList.add('in-view'));
  }

  /* ---------- button ripple ---------- */
  document.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('click', function (e) {
      const rect = this.getBoundingClientRect();
      const ripple = document.createElement('span');
      const size = Math.max(rect.width, rect.height) * 1.4;
      ripple.style.cssText = `
        position:absolute; border-radius:50%; pointer-events:none;
        width:${size}px; height:${size}px;
        left:${e.clientX - rect.left - size / 2}px;
        top:${e.clientY - rect.top - size / 2}px;
        background:rgba(255,255,255,0.35);
        transform:scale(0); opacity:1;
        animation:ripple-anim .6s ease-out;
      `;
      this.style.position = this.style.position || 'relative';
      this.style.overflow = 'hidden';
      this.appendChild(ripple);
      setTimeout(() => ripple.remove(), 650);
    });
  });

  const styleTag = document.createElement('style');
  styleTag.textContent = `@keyframes ripple-anim{ to{ transform:scale(1); opacity:0; } }`;
  document.head.appendChild(styleTag);

  /* ---------- animated confidence bar (result pages) ---------- */
  const fill = document.querySelector('.confidence-fill');
  if (fill) {
    const target = fill.getAttribute('data-confidence') || '0';
    requestAnimationFrame(() => {
      setTimeout(() => { fill.style.width = target + '%'; }, 300);
    });
  }

  /* ---------- prediction form validation ---------- */
  const form = document.getElementById('predict-form');
  if (form) {
    const inputs = form.querySelectorAll('input[type="number"]');
    const submitBtn = form.querySelector('.btn-primary');

    const showError = (input, msg) => {
      const wrap = input.closest('.field');
      const errEl = wrap.querySelector('.field-error');
      input.classList.add('invalid');
      if (errEl) { errEl.textContent = msg; errEl.classList.add('show'); }
    };

    const clearError = (input) => {
      const wrap = input.closest('.field');
      const errEl = wrap.querySelector('.field-error');
      input.classList.remove('invalid');
      if (errEl) { errEl.textContent = ''; errEl.classList.remove('show'); }
    };

   const validateField = (input) => {
  const value = input.value.trim();

  if (value === '') {
    showError(input, 'This field is required');
    return false;
  }

  if (isNaN(value)) {
    showError(input, 'Numbers only');
    return false;
  }

  const num = parseFloat(value);

  // Check minimum
  if (input.min !== "" && num < parseFloat(input.min)) {
    showError(input, `Minimum value is ${input.min}`);
    return false;
  }

  // Check maximum
  if (input.max !== "" && num > parseFloat(input.max)) {
    showError(input, `Maximum value is ${input.max}`);
    return false;
  }

  clearError(input);
  return true;
};
    inputs.forEach(input => {
      input.addEventListener('blur', () => validateField(input));
      input.addEventListener('input', () => {
        if (input.classList.contains('invalid')) validateField(input);
      });
    });

    form.addEventListener('submit', (e) => {
      let allValid = true;
      inputs.forEach(input => {
        if (!validateField(input)) allValid = false;
      });

      if (!allValid) {
        e.preventDefault();
        const firstInvalid = form.querySelector('.invalid');
        if (firstInvalid) firstInvalid.focus({ preventScroll: false });
        return;
      }

      if (submitBtn) {
        submitBtn.classList.add('is-loading');
        submitBtn.disabled = true;
      }
      // form submits normally to Flask backend ("/predict")
    });
  }

});