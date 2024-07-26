//
// isotope.js
//

import imagesLoaded from 'imagesloaded';
import Isotope from 'isotope-layout';

const toggles = document.querySelectorAll('[data-isotope]');

toggles.forEach(function (toggle) {
  imagesLoaded(toggle, function () {
    const options = toggle.dataset.isotope ? JSON.parse(toggle.dataset.isotope) : {};

    new Isotope(toggle, options);
  });
});

// Make available globally
window.Isotope = Isotope;
window.imagesLoaded = imagesLoaded;
