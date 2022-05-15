$(document).ready(() => {
  // destroy notifications
  $(".delete").click(() => {
    $(".notification").remove();
  });
});
