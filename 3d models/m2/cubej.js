// Cube rotation with mouse drag
const cube = document.getElementById('cube');
let rotateX = -27;
let rotateY = -32;
let dragging = false;
let lastX, lastY;

function renderCube() {
    cube.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
}

// Initial render
renderCube();

// Mouse events to drag and rotate cube
cube.parentElement.addEventListener('mousedown', function(e) {
    dragging = true;
    lastX = e.clientX;
    lastY = e.clientY;
});
document.addEventListener('mousemove', function(e) {
    if (!dragging) return;
    rotateY += (e.clientX - lastX) * 0.8;
    rotateX -= (e.clientY - lastY) * 0.8;
    lastX = e.clientX;
    lastY = e.clientY;
    renderCube();
});
document.addEventListener('mouseup', function(e) {
    dragging = false;
});

// Touch events for mobile
cube.parentElement.addEventListener('touchstart', function(e) {
    dragging = true;
    lastX = e.touches[0].clientX;
    lastY = e.touches[0].clientY;
});
document.addEventListener('touchmove', function(e) {
    if (!dragging) return;
    rotateY += (e.touches[0].clientX - lastX) * 0.7;
    rotateX -= (e.touches[0].clientY - lastY) * 0.7;
    lastX = e.touches[0].clientX;
    lastY = e.touches[0].clientY;
    renderCube();
});
document.addEventListener('touchend', function(e) {
    dragging = false;
});
