//
// jarallax.js
//

import { jarallax, jarallaxElement, jarallaxVideo } from 'jarallax';

const toggles = document.querySelectorAll('[data-jarallax], [data-jarallax-element], [data-jarallax-video]');

// Add Video extension
jarallaxVideo();

// Add Element extension
jarallaxElement();

// Init Jarallax
jarallax(toggles);

// Male available globally
window.jarallax = jarallax;
window.jarallaxElement = jarallaxElement;
window.jarallaxVideo = jarallaxVideo;
