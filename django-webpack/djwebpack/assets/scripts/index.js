'use strict';

import './helper1'
import './helper2'

// import 'htmx.org';
window.htmx = require('htmx.org');


window.addEventListener('load', () => {
    document.getElementById('message').textContent = "YREBUNDLED BY WEBPACK";
});