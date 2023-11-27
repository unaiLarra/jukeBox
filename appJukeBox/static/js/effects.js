$(document).ready(function() {

  var is_up = false;
  $("div.contenido > h2.listado").dbclick(function () {
    if (is_up == false) {
      is_up = true;
      $("div.bandas").slideUp();
    } else {
      is_up = false;
      $("div.bandas").slideDown();
    }
  });

 });