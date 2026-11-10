// Preview protection: ask search engines not to index this page when it is
// served from any host other than the production domain (preview/staging URLs,
// localhost). On asemanitrading.com this does nothing, so production stays
// indexable. A hosting-level "X-Robots-Tag: noindex" header on preview
// deployments is the stronger safeguard and should be used as well if available.
(function () {
  var production = ["asemanitrading.com", "www.asemanitrading.com"];
  if (production.indexOf(window.location.hostname) !== -1) return;

  var meta = document.createElement("meta");
  meta.name = "robots";
  meta.content = "noindex";
  document.head.appendChild(meta);
})();
