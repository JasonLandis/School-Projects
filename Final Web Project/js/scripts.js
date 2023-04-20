var imageContainer = document.querySelector("#top-image");
var range = document.querySelector("#range-input");

range.oninput = function() {
  imageContainer.style.width = this.value + "%";
}
