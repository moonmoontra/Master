function submitForm(event) {
    event.preventDefault();
    var form = event.target;
    var formData = new FormData(form);
    fetch(form.action, {
      method: form.method,
      body: formData
    })
    .then(response => {
    })
    .catch(error => {
    });
  }