// app.js - optional: focus input and allow pressing Enter.
document.addEventListener('DOMContentLoaded', function() {
  const cityInput = document.getElementById('city');
  if (cityInput) cityInput.focus();

  const form = document.getElementById('city-form');
  if (form) {
    form.addEventListener('submit', function() {
      // optional: show loading UI or disable button
    });
  }
});
