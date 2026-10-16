// Opens the accordion a link or URL hash points to (e.g. #slides), then scrolls to it.
(function () {
  function openTarget(hash, scroll) {
    if (!hash || hash.length < 2) return;
    var el = document.getElementById(decodeURIComponent(hash.slice(1)));
    if (!el) return;
    var d = el.tagName === 'DETAILS' ? el : el.closest('details');
    if (d) d.open = true;
    if (scroll) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href^="#"]');
    if (!a) return;
    var h = a.getAttribute('href');
    if (h === location.hash) { e.preventDefault(); openTarget(h, true); } else { openTarget(h, false); }
  });
  window.addEventListener('hashchange', function () { openTarget(location.hash, true); });
  openTarget(location.hash, false);
  window.addEventListener('load', function () { setTimeout(function () { openTarget(location.hash, true); }, 60); });
})();
