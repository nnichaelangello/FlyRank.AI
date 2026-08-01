// --- 1. Cursor Follower & Spotlight ---
const cursor = document.getElementById('cursor');
const spotlight = document.getElementById('spotlight');
const interactives = document.querySelectorAll('.interactive, a, button');

let mouseX = window.innerWidth / 2;
let mouseY = window.innerHeight / 2;
let cursorX = mouseX;
let cursorY = mouseY;

window.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    // Update Spotlight
    if (spotlight) {
        spotlight.style.setProperty('--x', `${mouseX}px`);
        spotlight.style.setProperty('--y', `${mouseY}px`);
    }
});

function renderCursor() {
    if (!cursor) return;
    cursorX += (mouseX - cursorX) * 0.15;
    cursorY += (mouseY - cursorY) * 0.15;
    cursor.style.transform = `translate(${cursorX}px, ${cursorY}px)`;
    requestAnimationFrame(renderCursor);
}
renderCursor();

// Cursor hover states
interactives.forEach(el => {
    el.addEventListener('mouseenter', () => { if (cursor) cursor.classList.add('hover'); });
    el.addEventListener('mouseleave', () => { if (cursor) cursor.classList.remove('hover'); });
});

// --- 2. Magnetic Button Logic ---
const magBtns = document.querySelectorAll('.magnetic-btn');
magBtns.forEach(btn => {
    btn.addEventListener('mousemove', (e) => {
        const rect = btn.getBoundingClientRect();
        const h = rect.width / 2;
        const w = rect.height / 2;
        const x = e.clientX - rect.left - h;
        const y = e.clientY - rect.top - w;
        
        gsap.to(btn, {
            x: x * 0.3,
            y: y * 0.3,
            duration: 0.3,
            ease: "power2.out"
        });
    });
    btn.addEventListener('mouseleave', () => {
        gsap.to(btn, { x: 0, y: 0, duration: 0.7, ease: "elastic.out(1, 0.3)" });
    });
});

// --- 3. Page Entrance Animations ---
if (document.querySelector('.reveal-inner')) {
    gsap.fromTo('.reveal-inner', 
        { y: "110%" },
        { y: "0%", duration: 1.2, stagger: 0.15, ease: "power4.out", delay: 0.3 }
    );
}

if (document.querySelector('.glass-card')) {
    gsap.fromTo('.glass-card', 
        { scale: 0.95, opacity: 0, y: 20 },
        { scale: 1, opacity: 1, y: 0, duration: 1.5, ease: "power3.out", delay: 0.1 }
    );
}

// Fade in normal content sections
if (document.querySelector('.fade-in')) {
    gsap.fromTo('.fade-in', 
        { opacity: 0, y: 30 },
        { opacity: 1, y: 0, duration: 1, stagger: 0.2, ease: "power2.out", delay: 0.5 }
    );
}

// --- 4. Interactive Particle Background ---
const canvas = document.getElementById('particles');
if (canvas) {
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    let particlesArray = [];
    const numberOfParticles = 70;

    class Particle {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = Math.random() * 2 + 0.5;
            this.speedX = Math.random() * 1 - 0.5;
            this.speedY = Math.random() * 1 - 0.5;
            this.density = (Math.random() * 30) + 1;
        }
        draw() {
            ctx.fillStyle = 'rgba(100, 255, 218, 0.4)';
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.closePath();
            ctx.fill();
        }
        update() {
            this.x += this.speedX;
            this.y += this.speedY;

            if (this.x < 0 || this.x > canvas.width) this.speedX *= -1;
            if (this.y < 0 || this.y > canvas.height) this.speedY *= -1;

            let dx = mouseX - this.x;
            let dy = mouseY - this.y;
            let distance = Math.sqrt(dx * dx + dy * dy);
            let forceDirectionX = dx / distance;
            let forceDirectionY = dy / distance;
            let maxDistance = 180;
            let force = (maxDistance - distance) / maxDistance;
            let directionX = forceDirectionX * force * this.density;
            let directionY = forceDirectionY * force * this.density;

            if (distance < maxDistance) {
                this.x -= directionX;
                this.y -= directionY;
            }
        }
    }

    function initParticles() {
        particlesArray = [];
        for (let i = 0; i < numberOfParticles; i++) {
            particlesArray.push(new Particle());
        }
    }
    initParticles();

    function animateParticles() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for (let i = 0; i < particlesArray.length; i++) {
            particlesArray[i].update();
            particlesArray[i].draw();
            
            for (let j = i; j < particlesArray.length; j++) {
                let dx = particlesArray[i].x - particlesArray[j].x;
                let dy = particlesArray[i].y - particlesArray[j].y;
                let distance = Math.sqrt(dx * dx + dy * dy);
                if (distance < 120) {
                    ctx.beginPath();
                    ctx.strokeStyle = `rgba(100, 255, 218, ${0.15 - distance/800})`;
                    ctx.lineWidth = 1;
                    ctx.moveTo(particlesArray[i].x, particlesArray[i].y);
                    ctx.lineTo(particlesArray[j].x, particlesArray[j].y);
                    ctx.stroke();
                    ctx.closePath();
                }
            }
        }
        requestAnimationFrame(animateParticles);
    }
    animateParticles();

    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        initParticles();
    });
}
