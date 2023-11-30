$(document).ready(function() {

  $("#titulo").dbclick(function () {
      $("div.card-content").slideUp();
  });

 });

function redirect(link) {
  window.location = link; 
}