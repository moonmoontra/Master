document.body.addEventListener('htmx:afterRequest', function (event) {
    const hxTitle = event.srcElement.getAttribute('hx-title');
    if (hxTitle) {
        document.title = hxTitle;
    }
});