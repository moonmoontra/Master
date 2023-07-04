document.addEventListener('DOMContentLoaded', function () {
    var savedTheme = localStorage.getItem('theme');
    var mainNav = document.getElementById('main-nav');

    if (savedTheme === 'dark') {
        document.body.classList.add('dark-theme');
        mainNav.setAttribute('data-bs-theme', 'dark');
    }
});


document.getElementById('theme-toggle').addEventListener('click', function () {
    document.body.classList.toggle('dark-theme');
    if (document.body.classList.contains('dark-theme')) {
        localStorage.setItem('theme', 'dark');
    } else {
        localStorage.setItem('theme', 'light');
    }
});