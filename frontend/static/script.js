document.addEventListener('DOMContentLoaded', () => {
  const grlivInput = document.querySelector('input[name="GrLivArea"]');
  const bsmtInput = document.querySelector('input[name="TotalBsmtSF"]');
  const firstflrInput = document.querySelector('input[name="1stFlrSF"]');

  function validateRange(input, min, max) {
    input.addEventListener('input', () => {
      const val = Number(input.value);
      if (val < min || val > max) {
        input.setCustomValidity(`Value must be between ${min} and ${max}`);
      } else {
        input.setCustomValidity('');
      }
    });
  }

  validateRange(grlivInput, 334, 5642);
  validateRange(bsmtInput, 0, 6110);
  validateRange(firstflrInput, 334, 4692);
});
// Custom JS can go here
console.log("Frontend loaded.");
