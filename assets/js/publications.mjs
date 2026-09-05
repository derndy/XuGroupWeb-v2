// The HTML is the complete index; this module only narrows the visible records.
export function normalizeText(value) {
  return value.normalize('NFKC').toLowerCase().replace(/\s+/gu, ' ').trim();
}

export function matchesPublication(record, filters) {
  const words = normalizeText(filters.query).split(' ').filter(Boolean);
  return (!filters.year || record.year === filters.year)
    && (!filters.type || record.types.includes(filters.type))
    && words.every((word) => record.search.includes(word));
}

// Retain existing /publication/#article-journal and #working%20paper bookmarks.
// Year anchors and unknown/malformed fragments must not hide the whole archive.
export function typeFromHash(hash, allowedTypes) {
  let key;
  try {
    key = decodeURIComponent(hash.replace(/^#/, ''));
  } catch {
    return '';
  }
  key = normalizeText(key).replace(/ /g, '-');
  return allowedTypes.includes(key) ? key : '';
}

export function bindPublicationBrowser(root, location, history, events) {
  const form = root.querySelector('[data-publication-filters]');
  const query = form.elements.namedItem('q');
  const type = form.elements.namedItem('type');
  const year = form.elements.namedItem('year');
  const count = root.querySelector('[data-publication-count]');
  const empty = root.querySelector('[data-publication-empty]');
  const allowedTypes = Array.from(type.options, (option) => option.value).filter(Boolean);
  const records = Array.from(root.querySelectorAll('[data-publication-record]'), (element) => ({
    element,
    year: element.dataset.year,
    types: element.dataset.types.split(' ').filter(Boolean),
    search: normalizeText(element.dataset.search),
  }));
  const groups = Array.from(root.querySelectorAll('[data-publication-year]'));
  const jumps = Array.from(root.querySelectorAll('[data-publication-year-link]'));

  function render() {
    const filters = { query: query.value, type: type.value, year: year.value };
    const visibleYears = new Set();
    let visible = 0;
    for (const record of records) {
      const matches = matchesPublication(record, filters);
      record.element.hidden = !matches;
      if (matches) {
        visible += 1;
        visibleYears.add(record.year);
      }
    }
    for (const group of groups) group.hidden = !visibleYears.has(group.dataset.publicationYear);
    for (const jump of jumps) jump.hidden = !visibleYears.has(jump.dataset.publicationYearLink);
    count.textContent = `Showing ${visible} of ${records.length} records`;
    empty.hidden = visible !== 0;
  }

  function updateTypeHash() {
    const url = new URL(location.href);
    url.hash = type.value ? encodeURIComponent(type.value) : '';
    // Browsing must still work in a restricted preview with unavailable history.
    try {
      history.replaceState(null, '', url);
    } catch {
      // Filtering never depends on writing the address bar.
    }
  }

  function readTypeHash() {
    type.value = typeFromHash(location.hash, allowedTypes);
    render();
  }

  form.addEventListener('submit', (event) => event.preventDefault());
  query.addEventListener('input', render);
  year.addEventListener('change', render);
  type.addEventListener('change', () => {
    updateTypeHash();
    render();
  });
  form.addEventListener('reset', (event) => {
    // Apply immediately, without waiting for the browser's reset default action.
    event.preventDefault();
    query.value = '';
    type.value = '';
    year.value = '';
    updateTypeHash();
    render();
  });
  events.addEventListener('hashchange', () => {
    // A year jump is navigation, not a request to clear the active type filter.
    if (!location.hash || typeFromHash(location.hash, allowedTypes)) readTypeHash();
  });
  events.addEventListener('pageshow', render);
  readTypeHash();
  form.hidden = false;
}

if (typeof document !== 'undefined') {
  const root = document.querySelector('[data-publication-browser]');
  if (root) bindPublicationBrowser(root, window.location, window.history, window);
}
