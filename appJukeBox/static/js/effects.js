$(document).ready(function() {

  $(".listado").dbclick(function () {
      $("div.card-content").slideUp();
  });

 });

function redirect(link) {
  window.location = link; 
}