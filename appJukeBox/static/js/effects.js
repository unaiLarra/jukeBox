$(document).ready(function() {

  var is_up = false;
  $("h2.listado").dbclick(function () {
      is_up = true;
      $("div.bandas").slideUp();
  });

 });