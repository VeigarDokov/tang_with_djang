//
// Scripts
// 

document.addEventListener('DOMContentLoaded', function () {
    var swiper = new Swiper('.swiper-container', {
        slidesPerView: 1,
        spaceBetween: 30,
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
    });

    // Navbar collapse on scroll
    var navbarCollapse = document.querySelector('.navbar-collapse');
    var navbarToggler = document.querySelector('.navbar-toggler');

    window.addEventListener('scroll', function () {
        if (window.scrollY > 0) {
            navbarCollapse.classList.remove('show');
            navbarToggler.classList.add('collapsed');
        }
    });
});
