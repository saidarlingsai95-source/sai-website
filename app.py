from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sai Naveen | Full Stack Developer Hyderabad</title>
<meta name="description" content="Sai Naveen - Full Stack Developer from Hyderabad. Python, React, Flask expert.">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
<style>
:root{--bg:#f8fafc;--card:#ffffff;--text:#0f172a;--muted:#64748b;--p:#6366f1;--p2:#8b5cf6;--border:#e2e8f0}
body.dark{--bg:#020617;--card:#0f172a;--text:#f1f5f9;--muted:#94a3b8;--border:#1e293b}
*{margin:0;padding:0;box-sizing:border-box;scroll-behavior:smooth}
body{font-family:'Inter',system-ui,sans-serif;background:var(--bg);color:var(--text);transition:0.4s}
#particles{position:fixed;top:0;left:0;width:100%;height:100%;z-index:-1;opacity:0.4}
nav{position:fixed;top:0;width:100%;background:rgba(255,255,255,0.8);backdrop-filter:blur(20px);display:flex;justify-content:space-between;align-items:center;padding:14px 5%;z-index:1000;border-bottom:1px solid var(--border)}
body.dark nav{background:rgba(2,6,23,0.8)}
.logo{font-weight:900;font-size:24px;background:linear-gradient(90deg,var(--p),var(--p2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
nav.links{display:flex;align-items:center;gap:25px}
nav a{text-decoration:none;color:var(--muted);font-weight:600;font-size:14px}
nav a:hover{color:var(--p)}
.hero{min-height:100vh;display:flex;align-items:center;justify-content:space-between;padding:120px 5% 60px;gap:40px;max-width:1300px;margin:0 auto;flex-wrap:wrap}
.hero-img-wrap{position:relative}
.hero-img{width:320px;height:320px;border-radius:30px;object-fit:cover;transform:rotate(-3deg);box-shadow:0 30px 80px rgba(99,102,241,0.35);border:5px solid var(--card);transition:0.5s}
.hero-img:hover{transform:rotate(0deg) scale(1.02)}
.hero-text{flex:1;min-width:300px}
.hero-text h1{font-size:56px;font-weight:900;line-height:1.05}
.hero-text h1 span{background:linear-gradient(90deg,var(--p),var(--p2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.typing{font-size:24px;color:var(--p);font-weight:800;margin:18px 0;height:32px}
.hero-text p{color:var(--muted);line-height:1.7;font-size:17px;max-width:540px}
.btns{margin-top:28px;display:flex;gap:14px;flex-wrap:wrap}
.btn{padding:15px 28px;border-radius:50px;text-decoration:none;font-weight:700;display:inline-flex;align-items:center;gap:8px;transition:0.3s;font-size:14px}
.btn-p{background:linear-gradient(90deg,var(--p),var(--p2));color:white;box-shadow:0 12px 30px rgba(99,102,241,0.4)}
.btn-p:hover{transform:translateY(-3px);box-shadow:0 18px 40px rgba(99,102,241,0.5)}
.btn-s{background:var(--card);color:var(--text);border:2px solid var(--border)}
.socials{margin-top:26px;display:flex;gap:12px}
.socials a{width:44px;height:44px;background:var(--card);border:1px solid var(--border);border-radius:50%;display:grid;place-items:center;color:var(--text);text-decoration:none;transition:0.3s}
.socials a:hover{background:var(--p);color:white;border-color:var(--p);transform:translateY(-3px)}
section{padding:90px 5%;max-width:1300px;margin:0 auto}
h2{font-size:40px;font-weight:900;text-align:center}
.sub{text-align:center;color:var(--muted);margin:12px 0 50px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:24px}
.card{background:var(--card);border:1px solid var(--border);border-radius:24px;padding:28px;transition:0.4s}
.card:hover{transform:translateY(-8px);box-shadow:0 20px 60px rgba(0,0,0,0.08);border-color:var(--p)}
.tag{display:inline-block;padding:6px 14px;background:rgba(99,102,241,0.1);color:var(--p);border-radius:50px;font-size:12px;font-weight:700;margin-top:12px}
.skill-bar{background:var(--border);height:8px;border-radius:10px;overflow:hidden;margin-top:12px}
.skill-fill{height:100%;background:linear-gradient(90deg,var(--p),var(--p2));width:0%;transition:1.8s}
#theme{cursor:pointer;width:42px;height:42px;background:var(--card);border:1px solid var(--border);border-radius:50%;display:grid;place-items:center;font-size:20px;transition:0.3s}
.contact-wrap{display:grid;grid-template-columns:1fr 1fr;gap:30px;max-width:1000px;margin:0 auto}
@media(max-width:768px){.contact-wrap{grid-template-columns:1fr}.hero{flex-direction:column-reverse;text-align:center}.hero-text p{margin:0 auto}.btns,.socials{justify-content:center}.hero-text h1{font-size:38px}}
input,textarea{width:100%;padding:15px;border-radius:14px;border:2px solid var(--border);background:var(--bg);color:var(--text);margin-bottom:14px;outline:none;font-family:inherit}
input:focus,textarea:focus{border-color:var(--p)}
footer{text-align:center;padding:40px;color:var(--muted);border-top:1px solid var(--border);margin-top:40px}
</style>
</head>
<body>
<canvas id="particles"></canvas>
<nav>
<div class="logo">Sai Naveen.</div>
<div class="links">
<a href="#home">Home</a><a href="#about">About</a><a href="#projects">Projects</a><a href="#certificates">Certificates</a><a href="#contact">Contact</a>
<div id="theme" onclick="toggleTheme()">🌙</div>
</div>
</nav>

<div class="hero" id="home">
<div class="hero-text" data-aos="fade-right">
<h1>Hi, I'm <span>Sai Naveen</span></h1>
<div class="typing" id="typing"></div>
<p>Hyderabad based Full Stack Developer. I build fast, beautiful & scalable web apps. CSE student passionate about Python, React & AI. Turning coffee into code everyday.</p>
<div class="btns">
<a href="#projects" class="btn btn-p"><i class="fas fa-rocket"></i> View Projects</a>
<a href="https://github.com/saidarlingsai95-source" target="_blank" class="btn btn-s"><i class="fab fa-github"></i> GitHub</a>
</div>
<div class="socials">
<a href="https://github.com/saidarlingsai95-source" target="_blank"><i class="fab fa-github"></i></a>
<a href="https://wa.me/919999999999" target="_blank"><i class="fab fa-whatsapp"></i></a>
<a href="#"><i class="fab fa-linkedin"></i></a>
<a href="#"><i class="fab fa-instagram"></i></a>
</div>
</div>
<div class="hero-img-wrap" data-aos="zoom-in"><img src="/static/photo.jpg" class="hero-img" onerror="this.src='https://ui-avatars.com/api/?name=Sai+Naveen&size=320&background=6366f1&color=fff'"></div>
</div>

<section id="about">
<h2 data-aos="fade-up">About Me</h2><p class="sub" data-aos="fade-up">Who I am</p>
<div class="grid">
<div class="card" data-aos="fade-up"><i class="fas fa-graduation-cap" style="font-size:28px;color:var(--p)"></i><h3 style="margin:12px 0 8px">Education</h3><p style="color:var(--muted)">B.Tech CSE, Hyderabad. CGPA 8.5+. Focus on Data Structures, Web Dev & AI.</p><span class="tag">2022-2026</span></div>
<div class="card" data-aos="fade-up" data-aos-delay="100"><i class="fas fa-code" style="font-size:28px;color:var(--p)"></i><h3 style="margin:12px 0 8px">What I Do</h3><p style="color:var(--muted)">Full Stack: React, Node, Python Flask, MongoDB. Build MVPs in 7 days.</p><span class="tag">MERN + Python</span></div>
<div class="card" data-aos="fade-up" data-aos-delay="200"><i class="fas fa-bullseye" style="font-size:28px;color:var(--p)"></i><h3 style="margin:12px 0 8px">Mission 2027</h3><p style="color:var(--muted)">Crack FAANG, Build SaaS that helps 1M students in India get jobs.</p><span class="tag">Dream Big</span></div>
</div>
</section>

<section id="projects">
<h2 data-aos="fade-up">Featured Projects</h2><p class="sub" data-aos="fade-up">Built with love & code</p>
<div class="grid">
<div class="card" data-aos="zoom-in"><h3>🔥 This Portfolio</h3><p style="color:var(--muted);margin:10px 0">God-mode portfolio with particle bg, dark mode, AOS animations, SEO optimized.</p><div><span class="tag">Flask</span> <span class="tag">JS</span></div><a href="#" style="display:inline-block;margin-top:15px;color:var(--p);font-weight:700;text-decoration:none">Live Demo →</a></div>
<div class="card" data-aos="zoom-in" data-aos-delay="100"><h3>🛒 ShopHyderabad</h3><p style="color:var(--muted);margin:10px 0">E-commerce for local Hyderabad stores with UPI payments & Telugu support.</p><div><span class="tag">MERN</span> <span class="tag">Razorpay</span></div><a href="#" style="display:inline-block;margin-top:15px;color:var(--p);font-weight:700;text-decoration:none">GitHub →</a></div>
<div class="card" data-aos="zoom-in" data-aos-delay="200"><h3>🤖 Sai AI Bot</h3><p style="color:var(--muted);margin:10px 0">AI chatbot for students to ask CSE doubts, built with OpenAI API.</p><div><span class="tag">Python</span> <span class="tag">OpenAI</span></div><a href="#" style="display:inline-block;margin-top:15px;color:var(--p);font-weight:700;text-decoration:none">Try AI →</a></div>
</div>
</section>

<section id="certificates">
<h2 data-aos="fade-up">Certificates & Wins</h2><p class="sub" data-aos="fade-up">Proof of work</p>
<div class="grid">
<div class="card" data-aos="flip-left"><h3>🏅 Python - NPTEL</h3><p style="color:var(--muted)">Elite certified in Python for Data Science - Top 5%</p></div>
<div class="card" data-aos="flip-left" data-aos-delay="100"><h3>🚀 Smart India Hackathon</h3><p style="color:var(--muted)">Finalist 2024 - Built AI solution for rural education</p></div>
<div class="card" data-aos="flip-left" data-aos-delay="200"><h3>💻 LeetCode 300+</h3><p style="color:var(--muted)">300 problems solved - 1500+ rating - Daily coder</p></div>
</div>
</section>

<section id="contact">
<h2 data-aos="fade-up">Let's Build Together</h2><p class="sub" data-aos="fade-up">Available for freelance & internships</p>
<div class="contact-wrap">
<div class="card" data-aos="fade-right"><h3>Get in Touch</h3><p style="color:var(--muted);margin:12px 0">Hyderabad, Telangana<br>Open to opportunities</p><div style="margin-top:20px"><p><i class="fas fa-envelope" style="color:var(--p)"></i> sai.naveen.dev@gmail.com</p><p style="margin-top:10px"><i class="fab fa-whatsapp" style="color:#25D366"></i> +91 99999 99999</p></div></div>
<div class="card" data-aos="fade-left"><input id="cname" placeholder="Your Name"><input id="cemail" placeholder="Your Email"><textarea id="cmsg" rows="4" placeholder="Your Idea..."></textarea><a class="btn btn-p" style="width:100%;justify-content:center" onclick="sendWA()"><i class="fab fa-whatsapp"></i> Send WhatsApp</a></div>
</div>
</section>

<footer>© 2026 Sai Naveen • Made in Hyderabad with ❤️ & ☕ • <span style="color:var(--p)">Level 6 - God Mode Unlocked</span></footer>

<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
<script>
AOS.init({duration:900,once:true});
const texts=["Full Stack Developer","Python Expert","Problem Solver","Hyderabad's Finest"];let i=0,j=0,del=false;
function type(){let cur=texts[i];document.getElementById("typing").innerHTML=(del?cur.slice(0,j--):cur.slice(0,j++))+"|";if(!del&&j>cur.length+6){del=true;setTimeout(type,1200);return}if(del&&j<0){del=false;i=(i+1)%texts.length}setTimeout(type,del?40:90)}type();
function toggleTheme(){document.body.classList.toggle("dark");document.getElementById("theme").innerText=document.body.classList.contains("dark")?"☀️":"🌙";localStorage.setItem("th",document.body.classList.contains("dark")?"d":"l")}
if(localStorage.getItem("th")=="d"){document.body.classList.add("dark");document.getElementById("theme").innerText="☀️"}
function sendWA(){let n=document.getElementById("cname").value,m=document.getElementById("cmsg").value;if(!n||!m){alert("Name & Message needed!");return}window.open(`https://wa.me/919999999999?text=Hi Sai! I am ${n}. ${m}`,"_blank")}
// Particles
const canvas=document.getElementById("particles"),ctx=canvas.getContext("2d");let w,h,parts=[];function resize(){w=canvas.width=window.innerWidth;h=canvas.height=window.innerHeight}window.addEventListener("resize",resize);resize();for(let k=0;k<60;k++)parts.push({x:Math.random()*w,y:Math.random()*h,vx:(Math.random()-0.5)*0.5,vy:(Math.random()-0.5)*0.5,r:Math.random()*2+1});function draw(){ctx.clearRect(0,0,w,h);ctx.fillStyle=getComputedStyle(document.body).getPropertyValue('--p');parts.forEach(p=>{p.x+=p.vx;p.y+=p.vy;if(p.x<0||p.x>w)p.vx*=-1;if(p.y<0||p.y>h)p.vy*=-1;ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fill()});requestAnimationFrame(draw)}draw();
</script>
</body>
</html>
    """

@app.route('/static/<path:f>')
def static_files(f):
    return send_from_directory('static', f)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
