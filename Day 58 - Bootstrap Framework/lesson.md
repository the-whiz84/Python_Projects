# 1. Introduction to Bootstrap

# Bootstrap is an external CSS framework. It became very popular because it was based on mobile-first CSS elements
# using a 6 column layout that looke great on mobile, tables or PCs

# By importing just some classed from Bootstrap, we can beautify elements without writing a lot of CSS code


# index.html
<ul class="nav nav-pills>
    <li>
        <button class="nav-link active rounded-5">Home</button>
    </li>
</ul>

# bootstrap.css
.nav {
    --bs-nav-link-padding-x: 1rem;
    --bs-nav-link-padding-y: 0.5rem;
    --bs-nav-link-font-weight: ;
    --bs-nav-link-color: var( --bs-link-hover-color);
    --bs-nav-link-disabled-color: var( --bs-secondry-color);
    display: flex;
    flex-wrap: wrap;
    padding-left: 0;
    margin-bottom: 0;
    list-style: none
}
.nav-pills {...}
.nav-link {...}
.active {...}
.rounded-5 {...}


# Bootstrap Framework contains pre-made CSS files that we can include into our project
# Other CSS frameworks are Foundation, MUI, Tailwind etc.


# 2. When to Use Bootstrap
- when building a mobile first, responsive website
- you want to deploy a website quickly
- use predefined sleek components 


# When NOT to use it
- very simple website
- very complex website where you want to customize every aspect of it


# 3.How to use Bootstrap

# 3.1. Via a CDN (Content Delivery Network) link - gets hold of the stylesheet from an external resource

<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

....
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>


# 3.2. Compiled CSS and JS via Download
- this has all the css files and scripts needed and can be included locally inside a project

bootstrap/
├── css/
│   ├── bootstrap-grid.css
│   ├── bootstrap-grid.css.map
│   ├── bootstrap-grid.min.css
│   ├── bootstrap-grid.min.css.map
│   ├── bootstrap-grid.rtl.css
│   ├── bootstrap-grid.rtl.css.map
│   ├── bootstrap-grid.rtl.min.css
│   ├── bootstrap-grid.rtl.min.css.map
│   ├── bootstrap-reboot.css
│   ├── bootstrap-reboot.css.map
│   ├── bootstrap-reboot.min.css
│   ├── bootstrap-reboot.min.css.map
│   ├── bootstrap-reboot.rtl.css
│   ├── bootstrap-reboot.rtl.css.map
│   ├── bootstrap-reboot.rtl.min.css
│   ├── bootstrap-reboot.rtl.min.css.map
│   ├── bootstrap-utilities.css
│   ├── bootstrap-utilities.css.map
│   ├── bootstrap-utilities.min.css
│   ├── bootstrap-utilities.min.css.map
│   ├── bootstrap-utilities.rtl.css
│   ├── bootstrap-utilities.rtl.css.map
│   ├── bootstrap-utilities.rtl.min.css
│   ├── bootstrap-utilities.rtl.min.css.map
│   ├── bootstrap.css
│   ├── bootstrap.css.map
│   ├── bootstrap.min.css
│   ├── bootstrap.min.css.map
│   ├── bootstrap.rtl.css
│   ├── bootstrap.rtl.css.map
│   ├── bootstrap.rtl.min.css
│   └── bootstrap.rtl.min.css.map
└── js/
    ├── bootstrap.bundle.js
    ├── bootstrap.bundle.js.map
    ├── bootstrap.bundle.min.js
    ├── bootstrap.bundle.min.js.map
    ├── bootstrap.esm.js
    ├── bootstrap.esm.js.map
    ├── bootstrap.esm.min.js
    ├── bootstrap.esm.min.js.map
    ├── bootstrap.js
    ├── bootstrap.js.map
    ├── bootstrap.min.js
    └── bootstrap.min.js.map

# 3.3. Via Package Managers
# Pull in Bootstrap’s source files into nearly any project with some of the most popular package managers:

- npm
- yarn
- RubyGems
- Composer
- NuGet


# 4. Bootrap Layout - Undertanding the 12 column Bootstap layout system

# It has 3 components:
- div with class container;
- inside that div we have another div with class row;
- inside the row div we have the items layed with column system

<div class="container">
  <div class="row">
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
  </div>
</div>

# Bootstrap will try to give every column inside the row equal spacing, and space them across the entire width of the container

# We can use the prebuilt layour classes to give each column the desired size

<div class="container">
  <div class="row">
    <div class="col-2">2 x column</div>
    <div class="col-4">4 x column</div>
    <div class="col-6">6 x column</div>
  </div>
</div>

# Bootstrap includes six default breakpoints, sometimes referred to as grid tiers, for building responsively. These breakpoints are based on common screen sizes

# Breakpoint	Class infix	    Dimensions
Extra small	        None	    <576px
Small	            sm	        ≥576px
Medium	            md	        ≥768px
Large	            lg	        ≥992px
Extra large	        xl	        ≥1200px
Extra extra large	xxl	        ≥1400px


# 5. Bootstrap Components - Learn to use pre-built and pre-styled Components

# 5.1 Buttons
https://getbootstrap.com/docs/5.3/components/buttons/#variants

<button type="button" class="btn btn-primary">Primary</button>
<button type="button" class="btn btn-secondary">Secondary</button>
<button type="button" class="btn btn-success">Success</button>
<button type="button" class="btn btn-danger">Danger</button>
<button type="button" class="btn btn-warning">Warning</button>
<button type="button" class="btn btn-info">Info</button>
<button type="button" class="btn btn-light">Light</button>
<button type="button" class="btn btn-dark">Dark</button>

<button type="button" class="btn btn-link">Link</button>


# 5.2 Cards
https://getbootstrap.com/docs/5.3/components/card/#example

<div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>


# 5.3 Navbar
https://getbootstrap.com/docs/5.3/components/navbar/#supported-content

<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" aria-disabled="true">Disabled</a>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>

# 5.4 SVG Icons to embed in NavBar or somewhere else
https://icons.getbootstrap.com

https://icons.getbootstrap.com/#install



# 5.5 Spacing
https://getbootstrap.com/docs/5.3/utilities/spacing/#margin-and-padding

<ul class="navbar-nav me-auto mb-2 mb-lg-0">
# mb-2 stands for margin-bottom size 2


# 5.6 Dark Mode (added in version 5.3)
https://getbootstrap.com/docs/5.3/customize/color-modes/#dark-mode

<!doctype html>
<html lang="en" data-bs-theme="dark">
