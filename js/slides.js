// Chart Academy · slide deck controls
// Arrow keys, space, or click the buttons to move. N shows presenter notes. F goes full screen.
(function () {
  var stage = document.querySelector(".stage");
  var slides = Array.prototype.slice.call(document.querySelectorAll(".slide"));
  var progress = document.querySelector(".progress");
  var counter = document.querySelector(".count");
  var i = 0;

  var start = parseInt((location.hash || "").replace("#", ""), 10);
  if (start >= 1 && start <= slides.length) i = start - 1;

  function fit() {
    var s = Math.min(window.innerWidth / 1280, window.innerHeight / 720);
    stage.style.transform = "scale(" + s + ")";
  }

  function show(n) {
    i = Math.max(0, Math.min(slides.length - 1, n));
    slides.forEach(function (el, k) { el.classList.toggle("active", k === i); });
    if (progress) progress.style.width = ((i + 1) / slides.length * 100) + "%";
    if (counter) counter.textContent = (i + 1) + " / " + slides.length;
    history.replaceState(null, "", "#" + (i + 1));
  }

  document.addEventListener("keydown", function (e) {
    if (["ArrowRight", "PageDown", " "].indexOf(e.key) > -1) { e.preventDefault(); show(i + 1); }
    else if (["ArrowLeft", "PageUp"].indexOf(e.key) > -1) { e.preventDefault(); show(i - 1); }
    else if (e.key === "Home") show(0);
    else if (e.key === "End") show(slides.length - 1);
    else if (e.key === "n" || e.key === "N") document.body.classList.toggle("show-notes");
    else if (e.key === "f" || e.key === "F") {
      if (document.fullscreenElement) document.exitFullscreen();
      else document.documentElement.requestFullscreen();
    }
  });

  document.querySelector(".prev").addEventListener("click", function () { show(i - 1); });
  document.querySelector(".next").addEventListener("click", function () { show(i + 1); });
  document.querySelector(".toggle-notes").addEventListener("click", function () {
    document.body.classList.toggle("show-notes");
  });

  window.addEventListener("hashchange", function () {
    var n = parseInt(location.hash.replace("#", ""), 10);
    if (n >= 1 && n <= slides.length && n - 1 !== i) show(n - 1);
  });
  window.addEventListener("resize", fit);
  fit();
  show(i);
})();
