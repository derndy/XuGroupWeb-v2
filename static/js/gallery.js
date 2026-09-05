(() => {
  const root = document.querySelector('[data-gallery-root]');
  const dialog = document.querySelector('#gallery-dialog');

  if (!root || !dialog || typeof dialog.showModal !== 'function') {
    return;
  }

  const items = Array.from(root.querySelectorAll('[data-gallery-item]'));
  const image = dialog.querySelector('[data-gallery-image]');
  const title = dialog.querySelector('[data-gallery-title]');
  const caption = dialog.querySelector('[data-gallery-caption]');
  const counter = dialog.querySelector('[data-gallery-counter]');
  const original = dialog.querySelector('[data-gallery-original]');
  const closeButton = dialog.querySelector('[data-gallery-close]');
  const previousButton = dialog.querySelector('[data-gallery-previous]');
  const nextButton = dialog.querySelector('[data-gallery-next]');

  if (
    items.length === 0 ||
    !image ||
    !title ||
    !caption ||
    !counter ||
    !original ||
    !closeButton ||
    !previousButton ||
    !nextButton
  ) {
    return;
  }

  let currentIndex = 0;
  let trigger = null;

  const render = (index) => {
    currentIndex = (index + items.length) % items.length;
    const item = items[currentIndex];
    const itemTitle = item.dataset.title || '';
    const itemCaption = item.dataset.caption || '';
    const itemAlt = item.dataset.alt || itemTitle;
    const fullSrc = item.dataset.fullSrc || item.href;

    image.src = fullSrc;
    image.alt = itemAlt;
    image.width = Number(item.dataset.fullWidth) || 0;
    image.height = Number(item.dataset.fullHeight) || 0;
    title.textContent = itemTitle;
    caption.textContent = itemCaption;
    counter.textContent = `Photograph ${currentIndex + 1} of ${items.length}`;
    original.href = fullSrc;
  };

  const open = (event, index) => {
    if (
      event.defaultPrevented ||
      event.button !== 0 ||
      event.metaKey ||
      event.ctrlKey ||
      event.shiftKey ||
      event.altKey
    ) {
      return;
    }

    event.preventDefault();
    trigger = items[index];
    render(index);
    dialog.showModal();
    closeButton.focus();
  };

  const close = () => {
    dialog.close();
  };

  items.forEach((item, index) => {
    item.addEventListener('click', (event) => open(event, index));
  });

  closeButton.addEventListener('click', close);
  previousButton.addEventListener('click', () => render(currentIndex - 1));
  nextButton.addEventListener('click', () => render(currentIndex + 1));

  dialog.addEventListener('click', (event) => {
    if (event.target === dialog) {
      close();
    }
  });

  dialog.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowLeft') {
      event.preventDefault();
      render(currentIndex - 1);
    }

    if (event.key === 'ArrowRight') {
      event.preventDefault();
      render(currentIndex + 1);
    }
  });

  dialog.addEventListener('close', () => {
    image.removeAttribute('src');
    image.alt = '';

    if (trigger) {
      trigger.focus();
    }
  });
})();
