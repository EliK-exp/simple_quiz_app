
var count = 0;

var navLinks = document.getElementById("navLinks");
var toggleNavLinks = document.getElementById("toggleNavLinks");
var navLinksAreHidden = false;
document.addEventListener("scroll", function (e) {
  //   console.log(window.pageYOffset);
  if (window.pageYOffset > 99 && navLinksAreHidden === false) {
    navLinks.style.opacity = 0;
    navLinksAreHidden = true;
    setTimeout(() => {
      if (window.pageYOffset > 99) {
        navLinks.style.display = "none";
        toggleNavLinks.style.display = "flex";
        toggleNavLinks.style.opacity = 1;
        toggleNavLinks.style.background = "rgba(255, 128, 0, 0.1)";
        count = 0;
      }
    }, 300);
  } else if (window.pageYOffset < 99 && navLinksAreHidden === true) {
    navLinks.style.display = "flex";
    toggleNavLinks.style.opacity = 0;
    navLinksAreHidden = false;
    setTimeout(() => {
      navLinks.style.opacity = 1;
      toggleNavLinks.style.display = "none";
    }, 300);
  }
});

toggleNavLinks.addEventListener("click", () => {
  console.log(count);
  count += 1;
  if (count % 2 === 0) {
    navLinks.style.display = "none";
    navLinks.style.opacity = 0;
    toggleNavLinks.style.background = "rgba(255, 128, 0, 0.1)";
  } else {
    navLinks.style.display = "flex";
    navLinks.style.opacity = 1;
    toggleNavLinks.style.background = "rgba(255, 128, 0, 0.439)";
  }
});
