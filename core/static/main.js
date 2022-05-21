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

  openAddGradesModal = () => {
    const el = document.getElementById("add-grades-modal");
    el.classList.add("is-active");
  };

  closeAddGradesModal = () => {
    const el = document.getElementById("add-grades-modal");
    el.classList.remove("is-active");
  };

  openEditGradesModal = () => {
    const el = document.getElementById("edit-grades-modal");
    el.classList.add("is-active");
  };

  closeEditGradesModal = () => {
    const el = document.getElementById("edit-grades-modal");
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

  $(".add-grades").click(() => {
    openAddGradesModal();
  });

  $(".close-grades-modal").click(() => {
    closeAddGradesModal();
  });

  $(".edit-grades").click(() => {
    openEditGradesModal();
  });

  $(".close-gradesedit-modal").click(() => {
    closeEditGradesModal();
  });

  // fetch data
  $(".fetch-student").click(() => {
    $.ajax({
      type: "GET",
      url: "/all_students",
      dataType: "json",
      success: (response) => {
        console.log(response);
      },
    });
  });
});
