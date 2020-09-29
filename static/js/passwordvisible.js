function passwordvisible1() {
  var x = document.getElementById("id_password1");
  var im = document.getElementById("pass1");
  if (x.type === "password") {
    x.type = "text";
    im.src = "/static/images/UiIcon/007-eye.png";
  } else {
    x.type = "password";
    im.src = "/static/images/UiIcon/010-hide.png";
  }
}

function passwordvisible2() {
  var x = document.getElementById("id_password2");
  var im = document.getElementById("pass2");
  if (x.type === "password") {
    x.type = "text";
    im.src = "/static/images/UiIcon/007-eye.png";
  } else {
    x.type = "password";
    im.src = "/static/images/UiIcon/010-hide.png";
  }
}

function passwordvisible3() {
  var x = document.getElementById("id_password");
  var im = document.getElementById("pass3");
  if (x.type === "password") {
    x.type = "text";
    im.src = "/static/images/UiIcon/007-eye.png";
  } else {
    x.type = "password";
    im.src = "/static/images/UiIcon/010-hide.png";
  }
}

// function passwordCheck() {
//   var x = document.getElementById("id_password1");
//   var y = document.getElementById("id_password2");
//   var z = document.getElementById("display-alert");
//   if (x.value === y.value) {
//     z.style.display = "none";
//     console.log("same pass");
//   } else {
//     z.style.display = "block";
//     console.log("note same");
//   }
// }
