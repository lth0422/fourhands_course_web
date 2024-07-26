# TOUCHE

Touche Theme by Simpleqode.

### Getting Started

To get started, you need to do the following:

1. Make sure you have Node installed since Touche uses npm to manage dependencies. If you don't, installing is quite easy, just visit the [Node Downloads page](https://nodejs.org/en/download/) and install it.
2. Unzip your theme and open your command line, making sure your command line prompt is at the root of the unzipped theme directory.
3. `npm install`: Open your command line to the root directory of your unzipped theme and run to install all of Touche's dependencies.

It's that simple! If you're not used to using terminal, don't worry, this is as advanced as it gets. If you want to kill the server and stop Webpack, just hit `Control + C`.

## Compiling

Webpack is used to manage Touche development. Open your command line to the root directory of the theme to use the following commands:

- `npm start`: Compile and watch the SCSS/JS/HTML, use Live Reload to update browsers instantly, start a server, and pop a tab in your default browser. Any changes made to the source files will be compiled as soon as you save the file.
- `npm run build`: Generates a `/dist` directory with all the production files.

## Handlebars Webpack Plugin

The [handlebars-webpack-plugin](https://www.npmjs.com/package/handlebars-webpack-plugin) package is used to make partials easier to use for initial development. For Touche, we only use it for a handful of components that are found on most pages. You can easily create new `.html` partials inside the `/src/partials` folder and point to them from any file by specifying the path to the partial file inside `{{> }}` curly brackets. Please read the [official package documentation](https://www.npmjs.com/package/handlebars-webpack-plugin) for more info.

## Customizing SCSS

There are 2 basic ways to customize your theme...

1. Customizing SCSS. This is more versatile and sustainable way to customize Touche, but requires the webpack compilation steps outlined above. The 2 major benefits of this strategy are using variable overrides to easily customize theme styles, plus you never have to touch Bootstrap or Touche's source, meaning future updates will be much, much, simpler. There are 2 provided files that make this strategy simple to implement:

- `user-variables.scss`: This file can be used to override Bootstrap core and Touche variables for customizing elements that have been tied to variables.
- `user.scss`: This file can be used for writing custom SCSS that will be compiled alongside Bootstrap and Touche's core files.

2. Compiled CSS. If you plan on using Touche "as is", or only need limited customization, feel free to simply attach the compiled `theme.bundle.css` file in the `dist/assets/css` directory.

## Plugins

### BigPicture

Vanilla JavaScript image / video viewer. Doesn't sit on the DOM when inactive.

```
<a data-bigpicture='{"imgSrc": "IMAGE_SOURCE"}' href="#">
  <img class="img-fluid" src="IMAGE_SOURCE" alt="..." />
</a>
```

[Plugin documentation](https://github.com/henrygd/bigpicture)

### Flickity

Touch, responsive, flickable carousels.

```
<div data-flickity='{FLICKITY_OPTIONS}'>
  ...
</div>
```

[Plugin documentation](https://flickity.metafizzy.co/)

### Isotope

Filter & sort magical layouts.

```
<div data-isotope='{ISOTOPE_OPTIONS}'>
  ...
</div>
```

[Plugin documentation](https://isotope.metafizzy.co/)

### Jarallax

Smooth parallax scrolling effect for background images, videos and inline elements.

```
<header data-jarallax data-speed=".8" style="background-image: url(IMAGE_SOURCE);">
  ...
</header>
```

[Plugin documentation](https://github.com/nk-o/jarallax)

### Map

Adds an interactive map powered by Mapbox. To enable the Mapbox map on your website, you'll need a Mapbox access token. Mapbox uses access tokens to associate API requests with your account. You can create a new access token on your Access Tokens page or programmatically using the Mapbox Tokens API. Once a new access token is created, please replace the original access token at `src/js/map.js` with the new one.

```
<div data-map='{"center": [LAT, LNG], "zoom": ZOOM_LEVEL}' style="height: 30rem;"></div>
```

[Plugin documentation](https://www.mapbox.com/)

### Newsletter form

The newsletter form is powered by [Mailchimp](https://mailchimp.com/). In order to hook up the form to your Mailchimp newsletter campaign, you need to replace the form's `action` attribute and the corresponding input's `name` attribute values with those provided by Mailchimp.

```
<form action="MAILCHIMP_FORM_ACTION" ...>
  ...
  <div style="position: absolute; left: -5000px;" aria-hidden="true">
    <input type="text" name="MAILCHIMP_INPUT_NAME" tabindex="-1" value="">
  </div>
  ...
</form>
```

1. Go to your Mailchimp dashboard, then click Create.
2. Choose Signup Form -> Embedded form, then click Begin.
3. Choose Unstyled tab. The information you need should be available in the form code below.

## Dark mode

Enabled by adding the `data-bs-theme="dark"` attribute to the `body` element. If you do not have the possibility to store user preferences on the backend, I highly recommend switching to a media query implementation: [Bootstrap documentation](https://getbootstrap.com/docs/5.3/customize/color-modes/#building-with-sass).

## Changelog

Version 3.1.0 - 17/02/2024

- Updated to Bootstrap v5.3.2
- Updated other dependencies
- Added dark mode
- Removed contact and reservation functionality. I recommend using custom backend solutions for better performance.
- Other small changes

Version 3.0.0 - 23/06/2021

- Updated to Bootstrap v5.0.2
- Replaced Gulp with Webpack & npm-scripts
- Replaced PHP scripts with EmailJS for email dispatching
- Added Handlebars Webpack Plugin for HTML partials
- Improved folder structure
- Improved HTML markup and SCSS styles
- Moved all JavaScript to ES6 modules
- Removed jQuery dependency
- Overall design overhaul
- Other small changes

Version 2.0.4 – 18/04/2019

- Updated to Bootstrap v4.3.1
- Updated to Flickity v2.2.0
- Updated to Isotope v3.0.6
- Updated to Imagesloaded v4.1.4
- Updated to Lightbox v2.10.0
- Updated to Parallax v1.5.0
- Updated dev dependencies

Version 2.0.3 – 20/08/2018

- Updated to Bootstrap v4.1.3

Version 2.0.2 – 28/01/2018

- Updated to Bootstrap 4
- Removed empty SASS files
- Removed empty index.html files
- Improved documentation

Version 2.0.1 – 17/09/2017

- Menu, events, map, and newsletter sections can now be used multiple times on a single page
- Added a marker to the Google maps
- Added a new navbar option and made it default (the old one can be found in the /snippets folder)
- Other small changes

Version 2.0.0 – 03/09/2017

- Rewrote code from scratch
- Updated to Bootstrap v4 Beta
- Replaced parallax plugin
- Added 7 new pages
- Added multiple new sections
- Enabled reservation and contact forms
- Enabled newsletter form
- Disabled preloader
- Disabled smooth scroll
- Other small changes

Version 1.0.0 – 23/05/2016

- Initial release

## Support

Simpleqode is happy to provide support for issues. Shoot me an email at yevgenysim+simpleqode@gmail.com and I'll get you squared away.
