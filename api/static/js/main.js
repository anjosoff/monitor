
$("#carouselIndex").carousel();

$(".item").click(function () {
  $("#carouselIndex").carousel(1);
});
$(document).ready(function () {
  $("#carouselIndex").swiperight(function () {
    $(this).carousel('prev');
  });
  $("#carouselIndex").swipeleft(function () {
    $(this).carousel('next');
  });
});

$(document).on("click", '[data-toggle="lightbox"]', function (event) {
  event.preventDefault();
  $(this).ekkoLightbox();
});