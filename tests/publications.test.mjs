import test from 'node:test';
import assert from 'node:assert/strict';
import { bindPublicationBrowser, matchesPublication, normalizeText, typeFromHash } from '../assets/js/publications.mjs';

const journal = {
  year: '2024', types: ['article-journal'],
  search: normalizeText('Xu Ye X-Ray Techniques Advanced Science 10.1002/advs.202400661'),
};
const filters = (query = '', type = '', year = '') => ({ query, type, year });

test('search is case-insensitive, whitespace-normalized, token-based, and literal', () => {
  assert.equal(normalizeText(' Ｘｕ\n  SCIENCE '), 'xu science');
  assert.ok(matchesPublication(journal, filters('science XU')));
  assert.ok(matchesPublication(journal, filters('10.1002/advs.202400661')));
  assert.ok(matchesPublication(journal, filters('x-ray')));
  for (const query of ['[', '.*', 'Xu|Ye', '(Science', '<script>', 'no-such-record']) {
    assert.equal(matchesPublication(journal, filters(query)), false);
  }
});

test('search, type, and year intersect; records may have multiple types', () => {
  assert.ok(matchesPublication(journal, filters('xu', 'article-journal', '2024')));
  assert.equal(matchesPublication(journal, filters('xu', 'thesis', '2024')), false);
  assert.equal(matchesPublication(journal, filters('', '', '2023')), false);
  assert.ok(matchesPublication({ ...journal, types: ['article-journal', 'working-paper'] }, filters('', 'working-paper')));
});

test('legacy type fragments work and unsafe or unrelated fragments are ignored', () => {
  const types = ['article-journal', 'working-paper'];
  assert.equal(typeFromHash('#article-journal', types), 'article-journal');
  assert.equal(typeFromHash('#Working%20paper', types), 'working-paper');
  assert.equal(typeFromHash('#working-paper', types), 'working-paper');
  for (const hash of ['', '#unknown', '#publication-year-2024', '#%', '#%E0%A4%A', '#%3Cscript%3E']) {
    assert.equal(typeFromHash(hash, types), '');
  }
});

// Minimal DOM contract for state tests, not a substitute for browser/visual QA.
function element(dataset = {}) {
  const handlers = new Map();
  return {
    dataset, hidden: false, value: '', textContent: '',
    addEventListener(name, handler) { handlers.set(name, handler); },
    fire(name) {
      let prevented = false;
      handlers.get(name)?.({ preventDefault() { prevented = true; } });
      return prevented;
    },
  };
}

function fixture(hash = '', failHistory = false, rows = [
  { year: '2024', types: 'article-journal', search: journal.search },
  { year: '2021', types: 'working-paper', search: 'Design Xu 10.26434/chemrxiv' },
  { year: '2019', types: 'thesis', search: 'Molecular Design Ye' },
]) {
  const fields = { q: element(), type: element(), year: element() };
  fields.type.options = ['', ...new Set(rows.flatMap((row) => row.types.split(' ')))].map((value) => ({ value }));
  const form = element();
  form.hidden = true;
  form.elements = { namedItem: (name) => fields[name] };
  const records = rows.map(element);
  const years = [...new Set(rows.map((row) => row.year))];
  const groups = years.map((publicationYear) => element({ publicationYear }));
  const jumps = years.map((publicationYearLink) => element({ publicationYearLink }));
  const count = element();
  const empty = element();
  const root = {
    querySelector: (selector) => ({
      '[data-publication-filters]': form,
      '[data-publication-count]': count,
      '[data-publication-empty]': empty,
    })[selector],
    querySelectorAll: (selector) => ({
      '[data-publication-record]': records,
      '[data-publication-year]': groups,
      '[data-publication-year-link]': jumps,
    })[selector],
  };
  const location = new URL(`https://example.test/publication/?preview=1${hash}`);
  const history = {
    replaceState(_state, _title, url) {
      if (failHistory) throw new Error('History unavailable');
      location.href = url.href;
    },
  };
  const events = element();
  bindPublicationBrowser(root, location, history, events);
  return { fields, form, records, groups, jumps, count, empty, location, events };
}

test('all records initially appear; filters reveal only after initialization', () => {
  const f = fixture();
  assert.equal(f.form.hidden, false);
  assert.equal(f.count.textContent, 'Showing 3 of 3 records');
  assert.ok(f.records.every((record) => !record.hidden));
  assert.ok(f.empty.hidden);
  assert.equal(f.form.fire('submit'), true);
});

test('input/paste, year, empty state, year jumps, and immediate reset stay consistent', () => {
  const f = fixture();
  f.fields.q.value = 'xu';
  f.fields.q.fire('input');
  assert.equal(f.count.textContent, 'Showing 2 of 3 records');
  assert.deepEqual(f.groups.map((group) => group.hidden), [false, false, true]);
  assert.deepEqual(f.jumps.map((jump) => jump.hidden), [false, false, true]);
  f.fields.year.value = '2019';
  f.fields.year.fire('change');
  assert.equal(f.count.textContent, 'Showing 0 of 3 records');
  assert.equal(f.empty.hidden, false);
  assert.ok(f.groups.every((group) => group.hidden));
  assert.equal(f.form.fire('reset'), true);
  assert.deepEqual(Object.values(f.fields).map((field) => field.value), ['', '', '']);
  assert.ok(f.records.every((record) => !record.hidden));
  assert.ok(f.empty.hidden);
  assert.equal(f.location.search, '?preview=1');
});

test('working-paper bookmarks, type changes, and hash navigation preserve matching state', () => {
  const f = fixture('#Working%20paper');
  assert.equal(f.fields.type.value, 'working-paper');
  assert.deepEqual(f.records.map((record) => record.hidden), [true, false, true]);
  f.fields.type.value = 'article-journal';
  f.fields.type.fire('change');
  assert.equal(f.location.hash, '#article-journal');
  f.location.hash = '#publication-year-2024';
  f.events.fire('hashchange');
  assert.equal(f.fields.type.value, 'article-journal');
  f.location.hash = '';
  f.events.fire('hashchange');
  assert.equal(f.fields.type.value, '');
  assert.equal(f.count.textContent, 'Showing 3 of 3 records');
});

test('artwork bookmarks isolate records and intersect with search and year', () => {
  const f = fixture('#frontispiece', false, [
    { year: '2024', types: 'article-journal', search: journal.search },
    { year: '2018', types: 'frontispiece', search: 'Photoacoustic Xu' },
    { year: '2016', types: 'cover-picture', search: 'Cell Tracking Xu' },
  ]);
  assert.equal(f.fields.type.value, 'frontispiece');
  assert.deepEqual(f.records.map((record) => record.hidden), [true, false, true]);
  f.fields.q.value = 'xu';
  f.fields.q.fire('input');
  f.fields.year.value = '2016';
  f.fields.year.fire('change');
  assert.equal(f.count.textContent, 'Showing 0 of 3 records');
  f.location.hash = '#cover-picture';
  f.events.fire('hashchange');
  assert.equal(f.fields.type.value, 'cover-picture');
  assert.deepEqual(f.records.map((record) => record.hidden), [true, true, false]);
  f.form.fire('reset');
  f.fields.type.value = 'article-journal';
  f.fields.type.fire('change');
  assert.deepEqual(f.records.map((record) => record.hidden), [false, true, true]);
});

test('history restrictions do not block filtering and an empty archive is safe', () => {
  const f = fixture('', true);
  f.fields.type.value = 'thesis';
  assert.doesNotThrow(() => f.fields.type.fire('change'));
  assert.equal(f.count.textContent, 'Showing 1 of 3 records');
  assert.doesNotThrow(() => f.form.fire('reset'));
  const empty = fixture('', false, []);
  assert.equal(empty.count.textContent, 'Showing 0 of 0 records');
  assert.equal(empty.empty.hidden, false);
});

test('page restoration re-renders retained controls', () => {
  const f = fixture();
  f.fields.q.value = 'molecular';
  f.events.fire('pageshow');
  assert.equal(f.count.textContent, 'Showing 1 of 3 records');
});
