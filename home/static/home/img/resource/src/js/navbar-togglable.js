//
// navbar.js
//

const navbar = document.querySelector('.navbar-togglable');
const navbarCollapse = document.querySelector('.navbar-collapse');
const windowEvents = ['load', 'scroll'];

let isLight = false;
let isCollapsed = false;

function makeNavbarDark(navbar) {
  navbar.classList.add('navbar-dark');
  isLight = false;
}

function makeNavbarLight(navbar) {
  navbar.classList.remove('navbar-dark');
  isLight = true;
}

function toggleNavbar(navbar) {
  const scrollTop = window.pageYOffset;

  if (scrollTop && !isLight) {
    makeNavbarLight(navbar);
  }

  if (!scrollTop && !isCollapsed) {
    makeNavbarDark(navbar);
  }
}

if (navbar) {
  // Toggle navbar on scroll
  windowEvents.forEach(function (event) {
    window.addEventListener(event, function () {
      toggleNavbar(navbar);
    });
  });

  // Toggle navbar on expand
  navbarCollapse.addEventListener('show.bs.collapse', function () {
    isCollapsed = true;

    makeNavbarLight(navbar);
  });

  // Toggle navbar on collapse
  navbarCollapse.addEventListener('hidden.bs.collapse', function () {
    isCollapsed = false;

    if (!window.pageYOffset) {
      makeNavbarDark(navbar);
    }
  });
}
