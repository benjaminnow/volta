$(document).ready(function() {
  var height_arr = [];

  $(".person").each(function() {
    height_arr.push([$(this).offset().top, $(this).attr('id')]);
  });
  height_arr.push([$(document).height(), "bottom"]);
  console.log(height_arr);

  $(window).scroll(function() {
    if ($(".name").offset().top < 15) {
      $(".name").text("Volta Data");
      return;
    }
    for (var i = 0; i < height_arr.length - 1; i++) {
      if ($(".name").offset().top >= height_arr[i][0] && $(".name").offset().top <= height_arr[i + 1][0]) {
        $(".name").text(height_arr[i][1]);
      }
    }

  });
});
