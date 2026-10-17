(() => {
  const root = document.documentElement;
  const button = document.getElementById('theme-toggle');
  const icon = button?.querySelector('.theme-toggle-icon');
  const label = button?.querySelector('.theme-toggle-label');
  const storageKey = 'portfolio-academico-theme';
  const colorPreference = window.matchMedia?.('(prefers-color-scheme: dark)');

  function readSavedTheme() {
    try {
      const value = window.localStorage.getItem(storageKey);
      return value === 'dark' || value === 'light' ? value : null;
    } catch (_error) {
      return null;
    }
  }

  let savedTheme = readSavedTheme();
  let userSelectedTheme = savedTheme !== null;

  function applyTheme(theme, savePreference = false) {
    const isDark = theme === 'dark';
    root.setAttribute('data-theme', isDark ? 'dark' : 'light');

    if (button) {
      button.setAttribute('aria-pressed', String(isDark));
      button.setAttribute('aria-label', 'Alternar tema claro e modo noturno');
      button.setAttribute('title', 'Alternar tema claro e modo noturno');
    }

    if (icon) icon.textContent = isDark ? '☀' : '☾';
    if (label) label.textContent = isDark ? 'Modo claro' : 'Modo noturno';

    if (savePreference) {
      userSelectedTheme = true;
      try {
        window.localStorage.setItem(storageKey, isDark ? 'dark' : 'light');
      } catch (_error) {
        // O tema continua funcionando mesmo se o navegador bloquear o armazenamento.
      }
    }
  }

  const initialTheme = savedTheme || (colorPreference?.matches ? 'dark' : 'light');
  applyTheme(initialTheme);

  button?.addEventListener('click', () => {
    const currentlyDark = root.getAttribute('data-theme') === 'dark';
    applyTheme(currentlyDark ? 'light' : 'dark', true);
  });

  colorPreference?.addEventListener?.('change', (event) => {
    if (!userSelectedTheme) applyTheme(event.matches ? 'dark' : 'light');
  });
})();
