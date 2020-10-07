function openNav() {
  x = document.getElementById("side-m");
  x.style.display = "block";
  x.style.width = "300px";
  // document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
  x = document.getElementById("side-m");
  if (x.style.display === "block") {
    x.style.display = "none";
    x.style.width = "0px";
  }
}
