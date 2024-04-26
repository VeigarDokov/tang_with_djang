// Navbar collapse on scroll
var navbarCollapse = document.querySelector('.navbar-collapse');
var navbarToggler = document.querySelector('.navbar-toggler');

window.addEventListener('scroll', function () {
    if (window.scrollY > 0) {
        navbarCollapse.classList.remove('show');
        navbarToggler.classList.add('collapsed');
    }
});
