// document.addEventListener('DOMContentLoaded', function () {
//     var savedTheme = localStorage.getItem('theme');
//     var mainNav = document.getElementById('main-nav');
//
//     if (savedTheme === 'dark') {
//         document.body.classList.add('dark-theme');
//         mainNav.setAttribute('data-bs-theme', 'dark');
//     }
// });
//
//
// document.getElementById('theme-toggle').addEventListener('click', function () {
//     console.log('clicked');
//     document.body.classList.toggle('dark-theme');
//     if (document.body.classList.contains('dark-theme')) {
//         localStorage.setItem('theme', 'dark');
//     } else {
//         localStorage.setItem('theme', 'light');
//     }
// });

document.addEventListener('DOMContentLoaded', function () {
    var savedTheme = localStorage.getItem('theme');
    var mainNav = document.getElementById('main-nav');

    if (savedTheme === 'dark') {
        document.body.classList.add('dark-theme');
        mainNav.setAttribute('data-bs-theme', 'dark');
    }
});

document.querySelector('.theme-toggle-dark').addEventListener('click', function () {
    console.log('clicked');
    document.body.classList.add('dark-theme');
    document.body.classList.remove('light-theme');
    localStorage.setItem('theme', 'dark');
});

document.querySelector('.theme-toggle-light').addEventListener('click', function () {
    console.log('clicked');
    document.body.classList.add('light-theme');
    document.body.classList.remove('dark-theme');
    localStorage.setItem('theme', 'light');
});