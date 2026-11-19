/* Linewise landing page interactions. Vanilla JS, no build step. */
(function () {
  'use strict';

  var root = document.documentElement;
  root.classList.add('js');
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Theme toggle ---------- */
  var themeBtn = document.querySelector('[data-theme-toggle]');
  var themeLabel = document.querySelector('[data-theme-label]');

  function syncThemeLabel() {
    var current = root.getAttribute('data-theme');
    // The button names the theme you would switch TO.
    themeLabel.textContent = current === 'dark' ? 'Light' : 'Dark';
    themeBtn.setAttribute('aria-label', 'Switch to ' + (current === 'dark' ? 'light' : 'dark') + ' theme');
  }
  syncThemeLabel();

  themeBtn.addEventListener('click', function () {
    var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('linewise-theme', next); } catch (e) {}
    syncThemeLabel();
  });

  /* ---------- Nav: solid after 40px, mobile menu ---------- */
  var nav = document.querySelector('[data-nav]');
  function onScroll() { nav.classList.toggle('is-solid', window.scrollY > 40); }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  var burger = document.querySelector('[data-menu-toggle]');
  var menu = document.getElementById('mobile-menu');
  function setMenu(open) {
    burger.setAttribute('aria-expanded', String(open));
    burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    menu.hidden = !open;
    nav.classList.toggle('is-solid', open || window.scrollY > 40);
  }
  burger.addEventListener('click', function () {
    setMenu(burger.getAttribute('aria-expanded') !== 'true');
  });
  menu.addEventListener('click', function (e) {
    if (e.target.closest('a')) setMenu(false);
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && !menu.hidden) { setMenu(false); burger.focus(); }
  });

  /* ---------- Scroll reveal (blur to focus) ---------- */
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-visible'); });
  }

  /* ---------- Example heatmap (illustration only) ---------- */
  var heat = document.querySelector('[data-heatmap]');
  if (heat) {
    // Fixed pattern so it looks the same on every load.
    var pattern = '0120321303212301230123310232123302132132';
    for (var i = 0; i < 48; i++) {
      var cell = document.createElement('i');
      var v = pattern.charAt(i % pattern.length);
      if (v === '1') cell.className = 'l1';
      else if (v === '2') cell.className = 'l2';
      else if (v === '3') cell.className = 'l3';
      if (i === 17 || i === 30) cell.className = 'lp';
      heat.appendChild(cell);
    }
  }

  /* ---------- Live demo: "Try today's snippet" ---------- */
  var BUG_LINE = 8;
  var lines = [
    [['k', 'def'], ['', ' '], ['f', 'dedupe_emails'], ['', '(emails):']],
    [['', '    '], ['c', '"""Remove duplicate emails, ignoring case."""']],
    [['', '    seen = '], ['f', 'set'], ['', '()']],
    [['', '    result = []']],
    [['', '    '], ['k', 'for'], ['', ' email '], ['k', 'in'], ['', ' emails:']],
    [['', '        key = email.'], ['f', 'strip'], ['', '().'], ['f', 'lower'], ['', '()']],
    [['', '        '], ['k', 'if'], ['', ' key '], ['k', 'not in'], ['', ' seen:']],
    [['', '            seen.'], ['f', 'add'], ['', '(email)']],
    [['', '            result.'], ['f', 'append'], ['', '(email)']],
    [['', '    '], ['k', 'return'], ['', ' result']]
  ];

  var codeBox = document.querySelector('[data-demo-lines]');
  var checkBtn = document.querySelector('[data-demo-check]');
  var resetBtn = document.querySelector('[data-demo-reset]');
  var countEl = document.querySelector('[data-demo-count]');
  var resultEl = document.querySelector('[data-demo-result]');
  var hint = document.querySelector('[data-hint]');
  var selected = new Set();
  var locked = false;
  var buttons = [];

  function plainText(tokens) {
    return tokens.map(function (t) { return t[1]; }).join('');
  }

  lines.forEach(function (tokens, idx) {
    var n = idx + 1;
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'demo-line';
    btn.setAttribute('aria-pressed', 'false');
    btn.setAttribute('aria-label', 'Line ' + n + ': ' + plainText(tokens).trim());
    btn.dataset.line = String(n);
    btn.tabIndex = idx === 0 ? 0 : -1; // roving tabindex: one tab stop for the group

    var num = document.createElement('span');
    num.className = 'demo-line__n';
    num.setAttribute('aria-hidden', 'true');
    num.textContent = n;
    btn.appendChild(num);

    var code = document.createElement('span');
    code.setAttribute('aria-hidden', 'true');
    tokens.forEach(function (t) {
      var s = document.createElement('span');
      if (t[0]) s.className = 'tok-' + t[0];
      s.textContent = t[1];
      code.appendChild(s);
    });
    btn.appendChild(code);

    var mark = document.createElement('span');
    mark.className = 'demo-line__mark';
    mark.setAttribute('aria-hidden', 'true');
    btn.appendChild(mark);

    btn.addEventListener('click', function () { toggle(n); });
    btn.addEventListener('keydown', onLineKey);
    codeBox.appendChild(btn);
    buttons.push(btn);
  });

  function focusLine(i) {
    i = Math.max(0, Math.min(buttons.length - 1, i));
    buttons.forEach(function (b, j) { b.tabIndex = j === i ? 0 : -1; });
    buttons[i].focus();
  }

  function onLineKey(e) {
    var i = buttons.indexOf(e.currentTarget);
    if (e.key === 'ArrowDown') { e.preventDefault(); focusLine(i + 1); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); focusLine(i - 1); }
    else if (e.key === 'Home') { e.preventDefault(); focusLine(0); }
    else if (e.key === 'End') { e.preventDefault(); focusLine(buttons.length - 1); }
    else if (e.key === 'Enter') {
      // Enter submits; Space (native button behavior) toggles.
      e.preventDefault();
      if (!locked && selected.size) check();
    }
  }

  function toggle(n) {
    if (locked) return;
    if (selected.has(n)) selected.delete(n); else selected.add(n);
    render();
  }

  function render() {
    buttons.forEach(function (b) {
      var n = Number(b.dataset.line);
      var on = selected.has(n);
      b.setAttribute('aria-pressed', String(on));
      if (!locked) b.querySelector('.demo-line__mark').textContent = on ? '✓' : '';
    });
    checkBtn.disabled = locked || selected.size === 0;
    if (locked) return;
    if (selected.size === 0) countEl.textContent = 'No lines flagged yet';
    else {
      var list = Array.from(selected).sort(function (a, b) { return a - b; });
      countEl.textContent = 'Flagged: line' + (list.length > 1 ? 's ' : ' ') + list.join(', ');
    }
  }

  var explanation =
    '<p class="result__body">Line 7 checks <code>key</code>, the lowercased email. Line 8 stores <code>email</code>, the original. ' +
    'The set never contains what you look up, so <code>Maya@x.com</code> and <code>maya@x.com</code> both survive.</p>' +
    '<div class="result__fix" aria-label="Fix: change seen.add(email) to seen.add(key)">' +
    '<span class="del">8   seen.add(email)</span>\n<span class="add">8   seen.add(key)</span></div>' +
    '<p class="result__body"><strong>Bug pattern:</strong> normalization mismatch. AI code often normalizes a value for the check and forgets to use it everywhere else.</p>';

  function saveCta(extra) {
    return '<div class="result__cta"><button type="button" class="btn btn--primary" data-demo-save>Save your streak — it\'s free</button>' + extra + '</div>';
  }

  function check() {
    if (!selected.size) return;
    locked = true;
    codeBox.classList.add('is-locked');

    var gotBug = selected.has(BUG_LINE);
    var extras = Array.from(selected).filter(function (n) { return n !== BUG_LINE; });
    var outcome = gotBug && extras.length === 0 ? 'correct' : 'partial';

    buttons.forEach(function (b) {
      var n = Number(b.dataset.line);
      var mark = b.querySelector('.demo-line__mark');
      if (n === BUG_LINE) {
        b.classList.add('is-bug');
        if (outcome === 'correct' && !reduceMotion) b.classList.add('is-pulse');
        mark.textContent = gotBug ? '✓ bug' : '← bug';
      } else if (selected.has(n)) {
        b.classList.add('is-wrong');
        mark.textContent = '✕';
      }
    });

    var html;
    if (outcome === 'correct') {
      html =
        '<p class="result__tag">✓ Found it on the first try</p>' +
        '<h3 class="result__title">That\'s the bug. Line 8.</h3>' + explanation +
        saveCta('<p>Email or GitHub. Nothing else.</p>');
      confetti();
    } else if (gotBug) {
      html =
        '<p class="result__tag">◐ Almost. You found it, plus ' + extras.length + ' extra line' + (extras.length > 1 ? 's' : '') + '.</p>' +
        '<h3 class="result__title">The bug is line 8. Here\'s what was hiding.</h3>' + explanation +
        '<p class="result__body">Partial credit. Next time, try narrowing it to one line: what actually changes the result?</p>' +
        saveCta('');
    } else {
      html =
        '<p class="result__tag">◐ Almost. Here\'s what was hiding.</p>' +
        '<h3 class="result__title">The bug is on line 8.</h3>' + explanation +
        '<p class="result__body">This one fools almost everyone the first time. That\'s exactly why it\'s practice.</p>' +
        '<div class="result__cta"><button type="button" class="btn btn--ghost" data-demo-retry>Try again</button></div>';
    }
    resultEl.className = 'result result--' + (outcome === 'correct' ? 'correct' : 'partial');
    resultEl.innerHTML = html;
    countEl.textContent = outcome === 'correct' ? 'Nice reading.' : 'Answer revealed.';
    checkBtn.disabled = true;
    if (hint) hint.open = false;

    var save = resultEl.querySelector('[data-demo-save]');
    if (save) save.addEventListener('click', function () {
      var note = document.createElement('p');
      note.textContent = 'Sign-up isn\'t live yet: Linewise is a class-project concept. Thanks for trying the snippet!';
      save.replaceWith(note);
    });

    var retry = resultEl.querySelector('[data-demo-retry]');
    if (retry) retry.addEventListener('click', reset);
  }

  function reset() {
    locked = false;
    selected.clear();
    codeBox.classList.remove('is-locked');
    buttons.forEach(function (b) {
      b.classList.remove('is-bug', 'is-wrong', 'is-pulse');
      b.querySelector('.demo-line__mark').textContent = '';
    });
    resultEl.className = 'result';
    resultEl.innerHTML = '';
    render();
    focusLine(0);
  }

  checkBtn.addEventListener('click', check);
  resetBtn.addEventListener('click', reset);
  render();

  /* ---------- Confetti (skipped under reduced motion) ---------- */
  function confetti() {
    if (reduceMotion) return;
    var colors = ['#2563EB', '#06B6D4', '#10B981', '#F59E0B', '#F97316'];
    var layer = document.createElement('div');
    layer.className = 'confetti';
    layer.setAttribute('aria-hidden', 'true');
    for (var i = 0; i < 70; i++) {
      var p = document.createElement('i');
      p.style.left = Math.random() * 100 + 'vw';
      p.style.background = colors[i % colors.length];
      p.style.animationDelay = Math.random() * 0.4 + 's';
      p.style.setProperty('--dx', (Math.random() * 160 - 80) + 'px');
      p.style.setProperty('--rot', (Math.random() * 720 - 360) + 'deg');
      layer.appendChild(p);
    }
    document.body.appendChild(layer);
    setTimeout(function () { layer.remove(); }, 2400);
  }
})();
