var loader = function (e) {
  let file = e.target.files;
  let show = "<span> selected : </span>" + file[0].name;

  let output = document.getElementById("selector");
  output.innerHTML = show;
  output.classList.add("acitve");
};

let fileinput = document.getElementById("id_images");
fileinput.addEventListener("change", loader);
