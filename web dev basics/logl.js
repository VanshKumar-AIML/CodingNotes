function generateCode(elementId) {
  const code = Math.random().toString(36).substring(2, 8).toUpperCase();
  document.getElementById(elementId).textContent = code;
}

function flipCard() {
  const card = document.getElementById("card");
  card.classList.toggle("flipped");
}

// Generate codes on page load
window.onload = () => {
  generateCode("loginCode");
  generateCode("registerCode");
};
