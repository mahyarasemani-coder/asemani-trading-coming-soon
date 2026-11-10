// Keep the footer year current. The page is fully usable without JavaScript.
(function () {
  var el = document.getElementById("year");
  if (el) el.textContent = String(new Date().getFullYear());
})();
