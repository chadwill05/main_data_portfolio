/*!
* Start Bootstrap - Personal v1.0.1 (https://startbootstrap.com/template-overviews/personal)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-personal/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


function showPage(pageNumber) {
    var page1 = document.getElementById('projectsPage1');
    var page2 = document.getElementById('projectsPage2');

    page1.style.display = (pageNumber === 1) ? 'block' : 'none';
    page2.style.display = (pageNumber === 2) ? 'block' : 'none';
}

