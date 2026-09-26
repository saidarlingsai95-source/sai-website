from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sai Naveen | Legend Portfolio</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
<style>
:root{--bg:#f8fafc;--card:#fff;--text:#0f172a;--muted:#64748b;--primary:#6366f1;--primary2:#8b5cf6}
body.dark{--bg:#020617;--card:#0f172a;--text:#f1f5f9;--muted:#94a3b8}
*{margin:0;padding:0;box-sizing:border-box;scroll-behavior:smooth}
body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:var(--text);transition:0.4s;overflow-x:hidden}
nav{position:fixed;top:0;width:100%;background:rgba(255,255,255,0.8);backdrop-filter:blur(20px);display:flex;justify-content:space-between;align-items:center;padding:15px 5%;z-index:1000;box-shadow:0 1px 20px rgba(0,0,0,0.05)}
body.dark nav{background:rgba(2,6,23,0.8)}
.logo{font-weight:900;font-size:22px;background:linear-gradient(90deg,var(--primary),var(--primary2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
nav a{margin-left:20px;text-decoration:none;color:var(--muted);font-weight:600}
nav a:hover{color:var(--primary)}
.hero{min-height:100vh;display:flex;align-items:center;justify-content:center;padding:120px 5% 50px;gap:50px;flex-wrap:wrap}
.hero-img{width:280px;height:280px;border-radius:50%;object-fit:cover;border:6px solid var(--card);box-shadow:0 20px 60px rgba(99,102,241,0.3);animation:float 3s ease-in-out infinite}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-15px)}}
.hero-text h1{font-size:50px;font-weight:900;line-height:1.1}
.hero-text h1 span{background:linear-gradient(90deg,var(--primary),var(--primary2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.typing{font-size:22px;color:var(--primary);font-weight:700;margin:15px 0;height:30px}
.btns{margin-top:25px;display:flex;gap:15px;flex-wrap:wrap}
.btn{padding:14px 28px;border-radius:50px;text-decoration:none;font-weight:700;transition:0.3s;display:inline-flex;align-items:center;gap:8px}
.btn-p{background:linear-gradient(90deg,var(--primary),var(--primary2));color:white;box-shadow:0 10px 30px rgba(99,102,241,0.4)}
.btn-p:hover{transform:translateY(-3px);box-shadow:0 15px 40px rgba(99,102,241,0.5)}
.btn-s{background:var(--card);color:var(--text);border:2px solid #e2e8f0}
.socials{margin-top:25px;display:flex;gap:15px}
.socials a{width:45px;height:45px;background:var(--card);border-radius:50%;display:grid;place-items:center;color:var(--text);box-shadow:0 5px 20px rgba(0,0,0,0.08);transition:0.3s;text-decoration:none}
.socials a:hover{background:var(--primary);color:white;transform:translateY(-3px)}
section{padding:80px 5%}
.card{background:var(--card);border-radius:20px;padding:30px;box-shadow:0 10px 40px rgba(0,0,0,0.06);transition:0.3s}
.card:hover{transform:translateY(-5px)}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:25px;margin-top:30px}
h2{font-size:36px;font-weight:900;text-align:center;margin-bottom:10px}
.subtitle{text-align:center;color:var(--muted);margin-bottom:40px}
.skill-bar{background:#e2e8f0;height:8px;border-radius:10px;overflow:hidden;margin-top:10px}
.skill-fill{height:100%;background:linear-gradient(90deg,var(--primary),var(--primary2));width:0%;transition:1.5s}
#theme{cursor:pointer;font-size:22px;margin-left:20px;background:var(--card);width:40px;height:40px;border-radius:50%;display:grid;place-items:center;box-shadow:0 5px 15px rgba(0,0,0,0.1)}
.contact-form input,.contact-form textarea{width:100%;padding:15px;border-radius:12px;border:2px solid #e2e8f0;background:var(--bg);color:var(--text);margin-bottom:15px;outline:none}
.contact-form input:focus,.contact-form textarea:focus{border-color:var(--primary)}
</style>
</head>
<body>

<nav>
<div class="logo">Sai Naveen.</div>
<div style="display:flex;align-items:center">
<a href="#home">Home</a><a href="#about">About</a><a href="#projects">Projects</a>
<div id="theme" onclick="toggleTheme()">🌙</div>
</div>
</nav>

<div class="hero" id="home">
<img src="/static/photo.jpg" class="hero-img" data-aos="zoom-in">
<div class="hero-text" data-aos="fade-left">
<h1>Hi, I'm <span>Sai Naveen</span></h1>
<div class="typing" id="typing"></div>
<p style="color:var(--muted);max-width:500px;line-height:1.6">I build exceptional digital experiences. Passionate CSE student from Hyderabad, turning ideas into powerful websites.</p>
<div class="btns">
<a href="#projects" class="btn btn-p"><i class="fas fa-rocket"></i> My Projects</a>
<a href="/static/resume.pdf" class="btn btn-s" download><i class="fas fa-download"></i> Resume</a>
</div>
<div class="socials">
<a href="https://github.com/saidarlingsai95-source" target="_blank"><i class="fab fa-github"></i></a>
<a href="https://wa.me/919999999999" target="_blank"><i class="fab fa-whatsapp"></i></a>
<a href="https://instagram.com" target="_blank"><i class="fab fa-instagram"></i></a>
<a href="https://linkedin.com" target="_blank"><i class="fab fa-linkedin"></i></a>
</div>
</div>
</div>

<section id="about">
<h2 data-aos="fade-up">About Me</h2><p class="subtitle" data-aos="fade-up">Know me better</p>
<div class="grid">
<div class="card" data-aos="fade-up"><h3>🎓 Student</h3><p style="color:var(--muted);margin-top:10px">B.Tech CSE - Passionate about Full Stack Development and AI. Hyderabad based developer.</p></div>
<div class="card" data-aos="fade-up" data-aos-delay="100"><h3>💻 Developer</h3><p style="color:var(--muted);margin-top:10px">MERN Stack, Python, Flask. Built 10+ projects with modern tech stack.</p></div>
<div class="card" data-aos="fade-up" data-aos-delay="200"><h3>🚀 Goal</h3><p style="color:var(--muted);margin-top:10px">To become a top 1% developer and work at FAANG company. Building in public.</p></div>
</div>
</section>

<section id="skills">
<h2 data-aos="fade-up">My Skills</h2>
<div class="grid" style="max-width:900px;margin:30px auto">
<div class="card" data-aos="flip-left"><h4>Python <span style="float:right">90%</span></h4><div class="skill-bar"><div class="skill-fill" data-width="90%"></div></div></div>
<div class="card" data-aos="flip-left" data-aos-delay="100"><h4>JavaScript <span style="float:right">85%</span></h4><div class="skill-bar"><div class="skill-fill" data-width="85%"></div></div></div>
<div class="card" data-aos="flip-left" data-aos-delay="200"><h4>React <span style="float:right">80%</span></h4><div class="skill-bar"><div class="skill-fill" data-width="80%"></div></div></div>
<div class="card" data-aos="flip-left" data-aos-delay="300"><h4>Flask <span style="float:right">88%</span></h4><div class="skill-bar"><div class="skill-fill" data-width="88%"></div></div></div>
</div>
</section>

<section id="projects">
<h2 data-aos="fade-up">Projects</h2><p class="subtitle" data-aos="fade-up">What I built</p>
<div class="grid">
<div class="card" data-aos="zoom-in"><h3>🔥 Portfolio Website</h3><p style="color:var(--muted);margin:10px 0">This legend portfolio with dark mode, animations & WhatsApp integration.</p><span style="color:var(--primary);font-weight:700">Flask • Python</span></div>
<div class="card" data-aos="zoom-in" data-aos-delay="100"><h3>🛒 E-Commerce</h3><p style="color:var(--muted);margin:10px 0">Full stack shopping app with cart, payment & admin panel.</p><span style="color:var(--primary);font-weight:700">MERN Stack</span></div>
<div class="card" data-aos="zoom-in" data-aos-delay="200"><h3>🤖 AI Chatbot</h3><p style="color:var(--muted);margin:10px 0">Intelligent chatbot using OpenAI API for college queries.</p><span style="color:var(--primary);font-weight:700">Python • AI</span></div>
</div>
</section>

<section id="contact">
<h2 data-aos="fade-up">Contact Me</h2>
<div style="max-width:600px;margin:0 auto" data-aos="fade-up">
<div class="card">
<div class="contact-form">
<input type="text" id="cname" placeholder="Your Name">
<textarea id="cmsg" rows="4" placeholder="Your Message"></textarea>
<a href="#" class="btn btn-p" style="width:100%;justify-content:center" onclick="sendWA()"><i class="fab fa-whatsapp"></i> Send on WhatsApp</a>
</div>
</div>
</div>
</section>

<footer style="text-align:center;padding:30px;color:var(--muted)">© 2026 Sai Naveen • Built with ❤️ in Hyderabad</footer>

<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
<script>
AOS.init({duration:1000,once:true});
const texts=["Full Stack Developer","Python Developer","CSE Student","Problem Solver"];let i=0,j=0,cur="",del=false;
function type(){cur=texts[i];let t=del?cur.substring(0,j--):cur.substring(0,j++);document.getElementById("typing").innerHTML=t+"|";
if(!del&&j==cur.length+8){del=true} else if(del&&j==0){del=false;i=(i+1)%texts.length} setTimeout(type,del?50:100)} type();
function toggleTheme(){document.body.classList.toggle("dark");document.getElementById("theme").innerText=document.body.classList.contains("dark")?"☀️":"🌙";localStorage.setItem("theme",document.body.classList.contains("dark")?"dark":"light")}
if(localStorage.getItem("theme")=="dark"){document.body.classList.add("dark");document.getElementById("theme").innerText="☀️"}
window.addEventListener("scroll",()=>{document.querySelectorAll(".skill-fill").forEach(e=>{if(e.getBoundingClientRect().top<window.innerHeight){e.style.width=e.dataset.width}})});
function sendWA(){let n=document.getElementById("cname").value,m=document.getElementById("cmsg").value;if(!n||!m){alert("Fill name & message!");return}window.open(`https://wa.me/919999999999?text=Hi Sai! I'm ${n}. ${m}`,"_blank")}
</script>
</body>
</html>
    """

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
