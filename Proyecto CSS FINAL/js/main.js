// main.js

function setActiveNav() {
  const links = document.querySelectorAll('nav a.nav-link, nav a');
  const path = window.location.pathname.toLowerCase();
  links.forEach(a => {
    try {
      // reset
      a.classList.remove('text-white', 'font-semibold');
      a.removeAttribute('aria-current');
      const href = a.getAttribute('href');
      if (!href) return;
      if (path.includes('/reviews/') && href.includes('reviews')) { a.classList.add('text-white', 'font-semibold'); a.setAttribute('aria-current','page'); }
      else if (path.includes('/noticias/') && href.includes('noticias')) { a.classList.add('text-white', 'font-semibold'); a.setAttribute('aria-current','page'); }
      else if (path.includes('/guias/') && href.includes('guias')) { a.classList.add('text-white', 'font-semibold'); a.setAttribute('aria-current','page'); }
      else if (path.includes('/contacto/') && href.includes('contacto')) { a.classList.add('text-white', 'font-semibold'); a.setAttribute('aria-current','page'); }
      else if (path.includes('/index/') && href.includes('index')) { a.classList.add('text-white', 'font-semibold'); a.setAttribute('aria-current','page'); }
    } catch(e) { /* ignore */ }
  });
}

function initLoadMore() {
  const btn = document.getElementById('load-more');
  if (!btn) return;
  btn.addEventListener('click', () => {
    const hidden = Array.from(document.querySelectorAll('.news-item.hidden'));
    if (hidden.length === 0) {
      btn.textContent = 'No hay más';
      btn.disabled = true;
      return;
    }
    // reveal up to 2 items
    hidden.slice(0,2).forEach(el => {
      el.classList.remove('hidden');
    });
  });
}

function initGuideSearch() {
  const input = document.getElementById('guide-search');
  if (!input) return;
  input.addEventListener('input', () => {
    const q = input.value.trim().toLowerCase();
    const guides = document.querySelectorAll('#guides article');
    guides.forEach(g => {
      const title = g.getAttribute('data-title') || g.textContent;
      g.style.display = title.toLowerCase().includes(q) ? '' : 'none';
    });
  });
}

function initContactForm() {
  const form = document.getElementById('contact-form');
  if (!form) return;
  const msg = document.getElementById('contact-msg');
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const data = new FormData(form);
    const email = (data.get('email') || '').toString();
    // simple email check
    const ok = /^\S+@\S+\.\S+$/.test(email);
    if (!ok) {
      msg.textContent = 'Introduce un email válido.';
      msg.classList.remove('text-textSecondary');
      msg.classList.add('text-red-400');
      return;
    }
    // Simular envío
    msg.textContent = 'Gracias, mensaje enviado.';
    msg.classList.remove('text-red-400');
    msg.classList.add('text-accent');
    form.reset();
  });
}

// reveal on scroll
function initReveal() {
  const items = document.querySelectorAll('.reveal');
  if (!items.length) return;
  const obs = new IntersectionObserver((entries, ob) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        ob.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });
  items.forEach(i => obs.observe(i));
}

// details modal: opens full content for reviews/guides
function initDetailModals() {
  // create modal once if not present
  if (!document.getElementById('detail-modal')) {
    const modal = document.createElement('div');
    modal.id = 'detail-modal';
    modal.className = 'fixed inset-0 bg-black bg-opacity-60 hidden items-center justify-center z-50';
    modal.innerHTML = `
      <div class="bg-bgSecondary max-w-3xl w-full mx-4 rounded-lg overflow-hidden">
        <div class="flex items-center justify-between p-4 border-b border-neutral-800">
          <h3 id="detail-title" class="text-lg font-semibold"></h3>
          <div class="flex items-center gap-4">
            <a id="detail-open-page" href="#" target="_blank" rel="noopener" class="text-sm text-accent hover:underline hidden">Abrir en página</a>
            <button id="detail-close" aria-label="Cerrar" class="text-textSecondary hover:text-white">✕</button>
          </div>
        </div>
        <div class="p-6 flex gap-6">
          <img id="detail-image" src="" alt="" class="w-40 h-40 object-cover rounded-md hidden">
          <div>
            <div id="detail-meta" class="text-textSecondary text-sm mb-3"></div>
            <div id="detail-content" class="text-textSecondary"></div>
          </div>
        </div>
      </div>
    `;
    document.body.appendChild(modal);
  }

  const modal = document.getElementById('detail-modal');
  const title = document.getElementById('detail-title');
  const image = document.getElementById('detail-image');
  const meta = document.getElementById('detail-meta');
  const content = document.getElementById('detail-content');
  const closeBtn = document.getElementById('detail-close');

  async function openDetail(type, slug, inlineContent) {
    // First, if running file:// try to use embedded SITE_DATA
    let item = null;
    try {
      if (location.protocol === 'file:' && window.SITE_DATA) {
        const list = type === 'guide' ? (window.SITE_DATA.guides || []) : (window.SITE_DATA.reviews || []);
        item = list.find(i => i.slug === slug);
      }
    } catch(e){ /* ignore */ }

    // If not found, try fetching (works when served)
    if (!item) {
      try {
        const resp = await fetch(`/data/${type === 'guide' ? 'guides' : 'reviews'}.json`);
        if (resp.ok) {
          const json = await resp.json();
          const list = type === 'guide' ? (json.guides || []) : (json.reviews || []);
          item = list.find(i => i.slug === slug);
        }
      } catch (e) { /* ignore fetch errors */ }
    }

    // Last fallback: try SITE_DATA again (in case fetch failed earlier)
    if (!item && window.SITE_DATA) {
      const list = type === 'guide' ? (window.SITE_DATA.guides || []) : (window.SITE_DATA.reviews || []);
      item = list.find(i => i.slug === slug);
    }

    // fallback to inline content or not found
    if (!item && inlineContent) {
      title.textContent = slug || (inlineContent.substr(0,40) + '...');
      image.classList.add('hidden');
      meta.textContent = '';
      content.textContent = inlineContent;
      // hide open page link
      const openLink = document.getElementById('detail-open-page');
      if (openLink) { openLink.classList.add('hidden'); openLink.removeAttribute('href'); }
    } else if (!item) {
      title.textContent = 'Contenido no disponible';
      image.classList.add('hidden');
      meta.textContent = '';
      content.textContent = 'Lo sentimos, el contenido aún no está publicado.';
      const openLink = document.getElementById('detail-open-page');
      if (openLink) { openLink.classList.add('hidden'); openLink.removeAttribute('href'); }
    } else {
      title.textContent = item.title;
      if (item.image) { image.src = item.image; image.alt = item.title; image.classList.remove('hidden'); } else { image.classList.add('hidden'); }
      meta.textContent = `${item.date || ''} ${item.platform ? ' · ' + item.platform : ''} ${item.score ? ' · Puntuación: ' + item.score : ''}`;
      content.textContent = item.content || item.summary || '';
      // set open page link
      const openLink = document.getElementById('detail-open-page');
      if (openLink) {
        const dir = type === 'guide' ? 'guias' : 'reviews';
        let href;
        if (location.pathname.includes(`/${dir}/`)) {
          href = `./${slug}.html`;
        } else {
          if (location.protocol === 'file:') href = `../${dir}/${slug}.html`;
          else href = `/${dir}/${slug}.html`;
        }
        openLink.href = href;
        openLink.classList.remove('hidden');
        openLink.setAttribute('target','_blank');
      }
    }

    modal.classList.remove('hidden');
    modal.classList.add('flex');
    document.body.style.overflow = 'hidden';
  }

  function closeDetail() {
    modal.classList.remove('flex');
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  }

  // delegate clicks
  document.addEventListener('click', (e) => {
    const btn = e.target.closest('.open-detail');
    if (!btn) return;
    e.preventDefault();
    const type = btn.dataset.type || (location.pathname.includes('/guias/') ? 'guide' : 'review');
    const slug = btn.dataset.slug || '';
    const inline = btn.dataset.content || '';
    openDetail(type, slug, inline);
  });

  // close handlers
  closeBtn.addEventListener('click', closeDetail);
  modal.addEventListener('click', (e) => { if (e.target === modal) closeDetail(); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !modal.classList.contains('hidden')) closeDetail(); });
}

// on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  setActiveNav();
  initLoadMore();
  initGuideSearch();
  initContactForm();
  initDetailModals();
  initReveal();
});
