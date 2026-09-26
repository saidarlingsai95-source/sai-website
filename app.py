from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sai Naveen - Web Developer</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
:root { --bg:#f8fafc; --card:#ffffff; --text:#0f172a; --muted:#64748b; --primary:#667eea; --border:#e2e8f0; }
.dark { --bg:#0f172a; --card:#1e293b; --text:#f1f5f9; --muted:#94a3b8; --border:#334155; }
* { margin:0; padding:0; box-sizing:border-box; scroll-behavior:smooth; }
body { font-family:'Segoe UI',sans-serif; background:var(--bg); color:var(--text); transition:0.3s; }
nav { position:fixed; top:0; width:100%; background:rgba(255,255,255,0.9); backdrop-filter:blur(10px); border-bottom:1px solid var(--border); z-index:100; padding:15px 0; }
.dark nav { background:rgba(15,23,42,0.9); }
.nav-wrap { max-width:1100px; margin:0 auto; padding:0 20px; display:flex; justify-content:space-between; align-items:center; }
.logo { font-weight:800; font-size:22px; background:linear-gradient(135deg,#667eea,#764ba2); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.nav-links { display:flex; gap:25px; list-style:none; }
.nav-links a { text-decoration:none; color:var(--muted); font-weight:600; }
.nav-links a:hover { color:var(--primary); }
.actions { display:flex; gap:10px; align-items:center; }
.btn-icon { width:40px; height:40px; border:1px solid var(--border); background:var(--card); border-radius:10px; cursor:pointer; display:grid; place-items:center; }
.hero { min-height:100vh; display:flex; align-items:center; justify-content:center; text-align:center; padding:120px 20px 60px; background:linear-gradient(135deg,#667eea 0%,#764ba2 100%); color:white; }
.profile { width:150px; height:150px; border-radius:50%; border:5px solid white; object-fit:cover; margin:0 auto 20px; display:block; box-shadow:0 20px 40px rgba(0,0,0,0.2); }
.hero h1 { font-size:52px; margin:15px 0; }
.hero p { font-size:20px; opacity:0.9; margin-bottom:30px; }
.btns { display:flex; gap:15px; justify-content:center; flex-wrap:wrap; }
.btn { padding:14px 28px; border-radius:12px; font-weight:700; text-decoration:none; display:inline-flex; align-items:center; gap:8px; cursor:pointer; border:none; }
.btn-white { background:white; color:#667eea; }
.btn-dark { background:rgba(0,0,0,0.2); color:white; border:2px solid white; }
.social { display:flex; gap:15px; justify-content:center; margin-top:30px; }
.social a { width:50px; height:50px; background:rgba(255,255,255,0.2); border-radius:12px; display:grid; place-items:center; color:white; font-size:20px; text-decoration:none; }
.social a:hover { background:white; color:#667eea; transform:translateY(-3px); }
.section { max-width:1100px; margin:0 auto; padding:80px 20px; }
.card { background:var(--card); border:1px solid var(--border); border-radius:20px; padding:30px; box-shadow:0 4px 20px rgba(0,0,0,0.05); }
.grid { display:grid; gap:20px; }
.grid-3 { grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); }
.skill { background:var(--bg); padding:15px; border-radius:12px; border:1px solid var(--border); display:flex; justify-content:space-between; align-items:center; font-weight:600; }
.contact-box { display:grid; grid-template-columns:1fr 1fr; gap:30px; }
@media(max-width:768px){ .contact-box{grid-template-columns:1fr;} .hero h1{font-size:36px;} .nav-links{display:none;} }
input, textarea { width:100%; padding:14px; border:1px solid var(--border); background:var(--bg); color:var(--text); border-radius:10px; margin-bottom:15px; font-family:inherit; }
</style>
</head>
<body id="body">

<nav>
<div class="nav-wrap">
<div class="logo">Sai Naveen</div>
<ul class="nav-links">
<li><a href="#home">Home</a></li>
<li><a href="#about">About</a></li>
<li><a href="#projects">Projects</a></li>
<li><a href="#contact">Contact</a></li>
</ul>
<div class="actions">
<button class="btn-icon" onclick="toggleDark()"><i class="fa-solid fa-moon" id="darkIcon"></i></button>
<a href="#" class="btn-icon" style="text-decoration:none;"><i class="fa-solid fa-download"></i></a>
</div>
</div>
</nav>

<section class="hero" id="home">
<div>
<img src="/static/sai-naveen.jpg" class="profile" onerror="this.src='https://i.pravatar.cc/300?img=12'">
<h1>Sai Naveen</h1>
<p>Web Developer | Python Enthusiast | Hyderabad</p>
<div class="btns">
<a href="#projects" class="btn btn-white"><i class="fa-solid fa-rocket"></i> My Projects</a>
<a href="#contact" class="btn btn-dark"><i class="fa-solid fa-paper-plane"></i> Hire Me</a>
</div>
<div class="social">
<a href="https://instagram.com/sainaveen_8" target="_blank"><i class="fa-brands fa-instagram"></i></a>
<a href="https://wa.me/919494211883" target="_blank"><i class="fa-brands fa-whatsapp"></i></a>
<a href="https://github.com" target="_blank"><i class="fa-brands fa-github"></i></a>
</div>
</div>
</section>

<section class="section" id="about">
<h2 style="font-size:36px; margin-bottom:20px;">About Me 🙋‍♂️</h2>
<div class="card">
<p style="color:var(--muted); line-height:1.7; font-size:17px;">
Hello! I am Sai Naveen from Hyderabad. I love building websites with Python Flask.
Currently learning web development and building real projects. My dream is to become a full-stack developer and work in top tech company!
<br><br>
<strong style="color:var(--text);">Skills:</strong> Python, Flask, HTML, CSS, GitHub, Render Deployment
</p>
<div class="grid grid-3" style="margin-top:25px;">
<div class="skill"><span><i class="fa-brands fa-python"></i> Python</span> <span>90%</span></div>
<div class="skill"><span><i class="fa-brands fa-html5"></i> Flask</span> <span>85%</span></div>
<div class="skill"><span><i class="fa-solid fa-code"></i> HTML/CSS</span> <span>80%</span></div>
</div>
</div>
</section>

<section class="section" id="projects">
<h2 style="font-size:36px; margin-bottom:20px;">My Projects 🚀</h2>
<div class="grid grid-3">
<div class="card"><h3>🌐 Portfolio Website</h3><p style="color:var(--muted); margin:15px 0;">My personal website built with Python Flask and deployed on Render.</p><span style="background:#dbeafe; color:#1e40af; padding:5px 12px; border-radius:20px; font-size:12px; font-weight:700;">Flask</span></div>
<div class="card"><h3>🐍 Python Projects</h3><p style="color:var(--muted); margin:15px 0;">Automation scripts, data analysis and cool Python experiments.</p><span style="background:#dcfce7; color:#166534; padding:5px 12px; border-radius:20px; font-size:12px; font-weight:700;">Python</span></div>
<div class="card"><h3>📱 Coming Soon</h3><p style="color:var(--muted); margin:15px 0;">Next project loading... E-commerce / Chat App / Blog</p><span style="background:#fef3c7; color:#92400e; padding:5px 12px; border-radius:20px; font-size:12px; font-weight:700;">Soon</span></div>
</div>
</section>

<section class="section" id="contact">
<h2 style="font-size:36px; margin-bottom:20px;">Contact Me 📩</h2>
<div class="contact-box">
<div class="card">
<h3>Send Message</h3>
<p style="color:var(--muted); margin:10px 0 20px;">Message will open in WhatsApp directly!</p>
<input type="text" id="name" placeholder="Your Name">
<input type="text" id="msg" placeholder="Your Message">
<button class="btn" style="background:linear-gradient(135deg,#667eea,#764ba2); color:white; width:100%; justify-content:center;" onclick="sendWA()"><i class="fa-brands fa-whatsapp"></i> Send on WhatsApp</button>
</div>
<div class="card" style="background:linear-gradient(135deg,#667eea,#764ba2); color:white; border:none;">
<h3>Let's Connect!</h3>
<p style="margin:15px 0; opacity:0.9;">Available for freelance work and internships!</p>
<div style="margin-top:20px;">
<p><i class="fa-brands fa-instagram"></i> @sainaveen_8</p>
<p style="margin-top:10px;"><i class="fa-brands fa-whatsapp"></i> 9494211883</p>
<p style="margin-top:10px;"><i class="fa-solid fa-location-dot"></i> Hyderabad, India</p>
</div>
<a href="https://wa.me/919494211883" target="_blank" class="btn btn-white" style="margin-top:25px; width:100%; justify-content:center;">Chat on WhatsApp</a>
</div>
</div>
</section>

<footer style="text-align:center; padding:40px; color:var(--muted); border-top:1px solid var(--border);">
<p>© 2026 Sai Naveen - Built with ❤️ using Python Flask</p>
<p style="margin-top:5px;">Level 4 - Pro Plus Edition</p>
</footer>

<script>
function toggleDark(){
  document.body.classList.toggle('dark');
  const icon = document.getElementById('darkIcon');
  if(document.body.classList.contains('dark')){ icon.className='fa-solid fa-sun'; }
  else { icon.className='fa-solid fa-moon'; }
}
function sendWA(){
  const name = document.getElementById('name').value || 'Hi';
  const msg = document.getElementById('msg').value || 'I saw your portfolio!';
  const text = `Hi Sai Naveen! I am ${name}. ${msg} - From your website`;
  window.open(`https://wa.me/919494211883?text=${encodeURIComponent(text)}`,'_blank');
}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/static/<path:filename>')
def static_files(filename):
    return app.send_static_file(filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
</atem:parameter>
</atem:invoke>
</atem:function_calls>
