const canvas = document.getElementById('background');
const ctx = canvas.getContext('2d');
let circles = [];

function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();

function createCircles() {
    circles = [];
    for (let i = 0; i < 30; i++) {
        circles.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            r: 20 + Math.random() * 40,
            dx: (Math.random() - 0.5) * 1.5,
            dy: (Math.random() - 0.5) * 1.5,
            color: `rgba(${100 + Math.random() * 155}, ${100 + Math.random() * 155}, 255, 0.2)`
        });
    }
}
createCircles();

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let c of circles) {
        ctx.beginPath();
        ctx.arc(c.x, c.y, c.r, 0, Math.PI * 2);
        ctx.fillStyle = c.color;
        ctx.fill();
        c.x += c.dx;
        c.y += c.dy;
        if (c.x < -c.r || c.x > canvas.width + c.r) c.dx *= -1;
        if (c.y < -c.r || c.y > canvas.height + c.r) c.dy *= -1;
    }
    requestAnimationFrame(animate);
}
animate();
