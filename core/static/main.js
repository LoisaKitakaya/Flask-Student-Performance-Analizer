$(document).ready(() => {
  // destroy notifications
  $(".delete").click(() => {
    $(".notification").remove();
  });

  // dashboard menu
  let vizBtn = $("#visualize-data-btn");
  let vizMenu = $("#visualize-data");

  vizMenu.hide();

  vizBtn.click(() => {
    vizMenu.slideToggle();
    vizBtn.toggleClass("is-active");
  });

  // chart.js
  var myFunc = () => {
    return chartData;
  };

  console.log(chartData);

  // modal
  openStudentModal = () => {
    const el = document.getElementById("add-student-modal");
    el.classList.add("is-active");
  };

  closeStudentModal = () => {
    const el = document.getElementById("add-student-modal");
    el.classList.remove("is-active");
  };

  openEditModal = () => {
    const el = document.getElementById("edit-student-modal");
    el.classList.add("is-active");
  };

  closeEditModal = () => {
    const el = document.getElementById("edit-student-modal");
    el.classList.remove("is-active");
  };

  $(".add-student").click(() => {
    openStudentModal();
  });

  $(".close-student-modal").click(() => {
    closeStudentModal();
  });

  $(".edit-student").click(() => {
    openEditModal();
  });

  $(".close-edit-modal").click(() => {
    closeEditModal();
  });
});
