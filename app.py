from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/')
def home():
    return '''
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sai Naveen - Web Developer</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:Arial;background:#f8fafc;color:#0f172a;scroll-behavior:smooth}
nav{position:fixed;top:0;width:100%;background:rgba(255,255,255,0.9);backdrop-filter:blur(10px);padding:15px 20px;display:flex;justify-content:space-between;align-items:center;z-index:1000;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
nav b{background:linear-gradient(135deg,#667eea,#764ba2);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-size:20px}
nav a{margin-left:15px;text-decoration:none;color:#0f172a;font-weight:bold;font-size:14px}
.hero{min-height:100vh;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);display:flex;align-items:center;justify-content:center;text-align:center;padding:80px 20px 40px;color:white}
.hero img{width:160px;height:160px;border-radius:50%;border:5px solid white;object-fit:cover;box-shadow:0 10px 30px rgba(0,0,0,0.3)}
.hero h1{font-size:38px;margin:15px 0 5px}
.hero p{opacity:0.9;margin:5px 0}
.btn{display:inline-block;margin:10px 6px;padding:12px 26px;border-radius:30px;text-decoration:none;font-weight:bold;transition:0.3s}
.btn-white{background:white;color:#667eea}
.btn-dark{background:#0f172a;color:white}
.btn:hover{transform:translateY(-3px);box-shadow:0 10px 20px rgba(0,0,0,0.2)}
.section{padding:60px 20px;max-width:1000px;margin:0 auto}
.card{background:white;border-radius:20px;padding:30px;box-shadow:0 5px 20px rgba(0,0,0,0.08);margin:20px 0}
.skills span{display:inline-block;background:linear-gradient(135deg,#667eea15,#764ba215);color:#667eea;border:1px solid #667eea30;padding:8px 16px;border-radius:20px;margin:5px;font-weight:bold;font-size:13px}
.project-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px;margin-top:20px}
.project{background:white;border-radius:15px;padding:20px;box-shadow:0 5px 15px rgba(0,0,0,0.08);border-left:5px solid #667eea}
.social a{display:inline-flex;width:50px;height:50px;align-items:center;justify-content:center;border-radius:50%;margin:0 8px;color:white;font-size:20px;text-decoration:none;transition:0.3s}
.social a:hover{transform:scale(1.15)}
.insta{background:linear-gradient(45deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888)}
.wa{background:#25D366}
.git{background:#333}
footer{background:#0f172a;color:white;text-align:center;padding:30px 20px;margin-top:40px}
h2{font-size:28px;margin-bottom:15px}
h2 i{color:#667eea}
</style>
</head>
<body>

<nav>
<b>Sai Naveen</b>
<div><a href="#about">About</a><a href="#skills">Skills</a><a href="#projects">Projects</a><a href="#contact">Contact</a></div>
</nav>

<div class="hero">
<div>
<img src="/photo.jpg">
<h1>Sai Naveen</h1>
<p style="font-size:18px;font-weight:bold">Web Developer | Python Enthusiast | Hyderabad</p>
<p style="margin-top:10px">I build websites with Python & Flask. Dream is to become Full Stack Developer! 🚀</p>
<div style="margin-top:25px">
<a class="btn btn-white" href="#projects"><i class="fas fa-rocket"></i> My Projects</a>
<a class="btn btn-dark" href="https://wa.me/919494211883" target="_blank"><i class="fab fa-whatsapp"></i> Hire Me</a>
</div>
<div class="social" style="margin-top:30px">
<a class="insta" href="https://instagram.com/sainaveen_8" target="_blank"><i class="fab fa-instagram"></i></a>
<a class="wa" href="https://wa.me/919494211883" target="_blank"><i class="fab fa-whatsapp"></i></a>
<a class="git" href="https://github.com/saidarlingsai95-source" target="_blank"><i class="fab fa-github"></i></a>
</div>
</div>
</div>

<div class="section" id="about">
<div class="card">
<h2><i class="fas fa-user"></i> About Me</h2>
<p style="line-height:1.7;color:#475569;margin-top:10px">Hello! I'm <b>Sai Naveen from Hyderabad</b>. I started my coding journey with Python and fell in love with web development. I built this portfolio myself using Flask, GitHub & Render - all deployed LIVE!</p>
<p style="line-height:1.7;color:#475569;margin-top:10px">My goal is to become a Full Stack Developer and build amazing products that help people. Currently learning HTML, CSS, Python, Flask, and GitHub.</p>
<p style="margin-top:15px"><b>📍 Hyderabad, Telangana</b> | <b>📱 9494211883</b> | <b>📸 @sainaveen_8</b></p>
</div>
</div>

<div class="section" id="skills">
<div class="card">
<h2><i class="fas fa-code"></i> My Skills</h2>
<div class="skills" style="margin-top:15px">
<span><i class="fab fa-python"></i> Python</span>
<span>Flask</span>
<span>HTML5</span>
<span>CSS3</span>
<span>GitHub</span>
<span>Render Deployment</span>
<span>Web Development</span>
<span>Responsive Design</span>
<span>Problem Solving</span>
</div>
</div>
</div>

<div class="section" id="projects">
<h2><i class="fas fa-briefcase"></i> My Projects</h2>
<div class="project-grid">
<div class="project">
<h3>🌐 Personal Portfolio Website</h3>
<p style="color:#64748b;margin:10px 0;line-height:1.5">Live website you are seeing right now! Built with Python Flask, deployed on Render with custom photo and contact.</p>
<p><b>Tech:</b> Python, Flask, HTML, CSS</p>
<a href="https://sai-website-rva7.onrender.com" target="_blank" style="color:#667eea;font-weight:bold;text-decoration:none;margin-top:10px;display:inline-block">View Live <i class="fas fa-external-link-alt"></i></a>
</div>
<div class="project">
<h3>🚀 Coming Soon - Project 2</h3>
<p style="color:#64748b;margin:10px 0">I am building my next project - a cool web app! Stay tuned on my Instagram @sainaveen_8</p>
<p><b>Tech:</b> Python + Creativity</p>
<span style="background:#f1f5f9;padding:5px 10px;border-radius:10px;font-size:12px">In Progress</span>
</div>
<div class="project">
<h3>💡 Your Idea Here?</h3>
<p style="color:#64748b;margin:10px 0">Have an idea for website or app? Let's build it together! WhatsApp me and let's create something amazing.</p>
<a href="https://wa.me/919494211883" target="_blank" style="background:#25D366;color:white;padding:8px 15px;border-radius:20px;text-decoration:none;font-weight:bold;display:inline-block;margin-top:5px"><i class="fab fa-whatsapp"></i> Let's Build</a>
</div>
</div>
</div>

<div class="section" id="contact">
<div class="card" style="text-align:center;background:linear-gradient(135deg,#667eea,#764ba2);color:white">
<h2 style="color:white"><i class="fas fa-paper-plane" style="color:white"></i> Contact Me</h2>
<p style="margin:15px 0;opacity:0.9">Want to work together or just say hi? I'm just a message away!</p>
<div style="margin-top:20px">
<a class="btn btn-white" href="https://wa.me/919494211883" target="_blank"><i class="fab fa-whatsapp"></i> WhatsApp: 9494211883</a>
<a class="btn btn-dark" href="https://instagram.com/sainaveen_8" target="_blank"><i class="fab fa-instagram"></i> Instagram</a>
</div>
<p style="margin-top:20px;font-size:13px;opacity:0.8">📍 Hyderabad | Available for freelance & internships</p>
</div>
</div>

<footer>
<p><b>Sai Naveen</b> - Web Developer from Hyderabad ❤️</p>
<p style="margin-top:8px;font-size:13px;opacity:0.7">Built with Python Flask | Deployed on Render | © 2026</p>
<div class="social" style="margin-top:15px">
<a class="insta" href="https://instagram.com/sainaveen_8" target="_blank"><i class="fab fa-instagram"></i></a>
<a class="wa" href="https://wa.me/919494211883" target="_blank"><i class="fab fa-whatsapp"></i></a>
<a class="git" href="https://github.com/saidarlingsai95-source" target="_blank"><i class="fab fa-github"></i></a>
</div>
</footer>

</body>
</html>
    '''

@app.route('/photo.jpg')
def photo():
    return send_from_directory('.', 'photo.jpg')

if __name__ == '__main__':
    app.run()
