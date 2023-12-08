document.addEventListener("DOMContentLoaded", () => {

    // mini-nav and breadcrumb fade in animation:

    let mini_nav = document.querySelector('#mini-nav');
    let scroll_top = -1;
    window.addEventListener("scroll", () => {
        if (window.innerWidth > 768) {
            if (window.scrollY >= 200) {
                scroll_top = window.scrollY;
                mini_nav.setAttribute('style', 'display: flex; animation-name: fade-in;');
            }
            else if (window.scrollY < 200 && scroll_top != -1) {
                mini_nav.setAttribute('style', 'display: flex; animation-name: fade-out;');
                mini_nav.addEventListener("animationend", () => {
                    if (mini_nav.style.animationName == "fade-out") {
                        mini_nav.setAttribute('style', 'display: none;');
                    }
                });
                scroll_top = -1;
            }
        }
    });

    
    // mobile navigation menu:
    
    let hamburger_menu_icon = document.querySelector("#hamburger-menu");
    let mobile_menu = document.querySelector("#mobile-menu");
    let close_mobile = mobile_menu.querySelector("#close-mobile")
    hamburger_menu_icon.addEventListener('click', () => {
        mobile_menu.setAttribute('style', 'display: flex;');
    });
    close_mobile.addEventListener('click', () => {
        mobile_menu.removeAttribute('style');
    });

});