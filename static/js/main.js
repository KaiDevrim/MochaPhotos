function like(id, img_path) {
  const button = document.getElementsByName("button-" + id);
  button[0].disabled = true;
  fetch(`/like/${img_path}`)
    .then(function (response) {
      return response.text();
    })
    .then(function (text) {});
}
