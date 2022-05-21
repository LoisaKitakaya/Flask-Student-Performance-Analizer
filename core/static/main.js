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

  // charts
  $(".all-students").click(() => {
    $("#all-unit-average").hide();
  });

  const allUnitAverage = $("#all-unit-average");
  $("#all-unit-average").hide();

  let science = [];
  let scienceAvg;

  let technology = [];
  let technologyAvg;

  let engineering = [];
  let engineeringAvg;

  let math = [];
  let mathAvg;

  let history = [];
  let historyAvg;

  let philosophy = [];
  let philosophyAvg;

  let language = [];
  let languageAvg;

  scienceGrades = (data) => {
    var total = 0;

    for (let i = 0; i < data.length; i++) {
      science.push(data[i]["science"]);
      total += data[i]["science"];
    }

    scienceAvg = Math.round(total / science.length);
  };

  technologyGrades = (data) => {
    var total = 0;

    for (let i = 0; i < data.length; i++) {
      technology.push(data[i]["technology"]);
      total += data[i]["technology"];
    }

    technologyAvg = Math.round(total / technology.length);
  };

  engineeringGrades = (data) => {
    var total = 0;

    for (let i = 0; i < data.length; i++) {
      engineering.push(data[i]["engineering"]);
      total += data[i]["engineering"];
    }

    engineeringAvg = Math.round(total / engineering.length);
  };

  mathGrades = (data) => {
    var total = 0;

    for (let i = 0; i < data.length; i++) {
      math.push(data[i]["math"]);
      total += data[i]["math"];
    }

    mathAvg = Math.round(total / math.length);
  };

  historyGrades = (data) => {
    var total = 0;

    for (let i = 0; i < data.length; i++) {
      history.push(data[i]["history"]);
      total += data[i]["history"];
    }

    historyAvg = Math.round(total / history.length);
  };

  philosophyGrades = (data) => {
    var total = 0;

    for (let i = 0; i < data.length; i++) {
      philosophy.push(data[i]["philosophy"]);
      total += data[i]["philosophy"];
    }

    philosophyAvg = Math.round(total / philosophy.length);
  };

  languageGrades = (data) => {
    var total = 0;

    for (let i = 0; i < data.length; i++) {
      language.push(data[i]["language"]);
      total += data[i]["language"];
    }

    languageAvg = Math.round(total / language.length);
  };

  // fetch data
  $(".avg-all-unts").click(() => {
    $.ajax({
      type: "GET",
      url: "/all_grades",
      dataType: "json",
      beforeSend: () => {
        $("#all-unit-average").hide();
      },
      success: (response) => {
        data = response.data;
        console.log(data);

        scienceGrades(this.data);
        technologyGrades(this.data);
        engineeringGrades(this.data);
        mathGrades(this.data);
        historyGrades(this.data);
        philosophyGrades(this.data);
        languageGrades(this.data);
      },
      complete: () => {
        //
        $("#all-unit-average").show();
        //
        const myChart = new Chart(allUnitAverage, {
          type: "bar",
          data: {
            labels: [
              "science",
              "technology",
              "engineering",
              "math",
              "history",
              "philosophy",
              "language",
            ],
            datasets: [
              {
                label: "Average per unit performance",
                data: [
                  scienceAvg,
                  technologyAvg,
                  engineeringAvg,
                  mathAvg,
                  historyAvg,
                  philosophyAvg,
                  languageAvg,
                ],
                backgroundColor: [
                  "rgba(255, 99, 132, 0.7)",
                  "rgba(54, 162, 235, 0.7)",
                  "rgba(255, 206, 86, 0.7)",
                  "rgba(75, 192, 192, 0.7)",
                  "rgba(153, 102, 255, 0.7)",
                  "rgba(255, 159, 64, 0.7)",
                  "rgba(99, 255, 125, 0.7)",
                ],
                borderColor: [
                  "rgba(255, 99, 132, 1)",
                  "rgba(54, 162, 235, 1)",
                  "rgba(255, 206, 86, 1)",
                  "rgba(75, 192, 192, 1)",
                  "rgba(153, 102, 255, 1)",
                  "rgba(255, 159, 64, 1)",
                  "rgb(102, 255, 148, 1)",
                ],
                borderWidth: 1,
              },
            ],
          },
          options: {
            scales: {
              y: {
                beginAtZero: true,
              },
            },
          },
        });
      },
    });
  });
});
