from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/')
def home():
    return '''
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
body{margin:0;font-family:Arial;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);min-height:100vh;display:flex;align-items:center;justify-content:center}
.card{max-width:420px;width:90%;margin:20px auto;background:white;color:#0f172a;border-radius:25px;padding:35px;box-shadow:0 20px 60px rgba(0,0,0,0.3);text-align:center;animation:slideUp 0.8s ease}
@keyframes slideUp{from{transform:translateY(50px);opacity:0}to{transform:translateY(0);opacity:1}}
img{width:160px;height:160px;border-radius:50%;object-fit:cover;border:5px solid #667eea;box-shadow:0 5px 15px rgba(102,126,234,0.4)}
h1{margin:20px 0 5px 0;font-size:28px;background:linear-gradient(135deg,#667eea,#764ba2);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.role{color:#667eea;font-weight:bold;margin:5px 0}
.desc{color:#64748b;margin:15px 0;line-height:1.5}
.skills{margin:20px 0}
.skills span{display:inline-block;background:linear-gradient(135deg,#667eea15,#764ba215);color:#667eea;border:1px solid #667eea30;padding:6px 14px;border-radius:20px;margin:4px;font-size:13px;font-weight:bold}
.btn{display:inline-block;margin:8px;padding:13px 28px;border-radius:30px;text-decoration:none;font-weight:bold;transition:all 0.3s}
.btn:hover{transform:translateY(-3px);box-shadow:0 10px 20px rgba(0,0,0,0.2)}
.btn-primary{background:linear-gradient(135deg,#667eea,#764ba2);color:white}
.btn-dark{background:#25D366;color:white}
.social{margin:20px 0}
.social a{display:inline-block;width:45px;height:45px;line-height:45px;border-radius:50%;margin:0 8px;color:white;font-size:18px;transition:all 0.3s}
.social a:hover{transform:scale(1.2)}
.insta{background:linear-gradient(45deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888)}
.whatsapp{background:#25D366}
.github{background:#333}
.live{margin-top:20px;font-size:11px;color:#10b981;font-weight:bold;letter-spacing:1px}
</style>
</head>
<body>
<div class="card">
<img src="/photo.jpg">
<h1>Sai Naveen</h1>
<p class="role">Web Developer | Hyderabad</p>
<p class="desc">Hi! I built this website myself using Python & Flask. I love coding and creating cool things! 🚀<br>DM me on Instagram or WhatsApp!</p>
<div class="skills">
<span>Python</span><span>Flask</span><span>HTML</span><span>GitHub</span><span>Render</span><span>Developer</span>
</div>
<div class="social">
<a class="insta" href="https://instagram.com/sainaveen_8" target="_blank"><i class="fab fa-instagram"></i></a>
<a class="whatsapp" href="https://wa.me/919494211883" target="_blank"><i class="fab fa-whatsapp"></i></a>
<a class="github" href="https://github.com/saidarlingsai95-source" target="_blank"><i class="fab fa-github"></i></a>
</div>
<a class="btn btn-primary" href="https://instagram.com/sainaveen_8" target="_blank"><i class="fab fa-instagram"></i> Follow Me</a>
<a class="btn btn-dark" href="https://wa.me/919494211883" target="_blank"><i class="fab fa-whatsapp"></i> WhatsApp Me</a>
<p class="live">● LIVE WEBSITE - BUILT BY SAI NAVEEN</p>
</div>
</body>
</html>
    '''

@app.route('/photo.jpg')
def photo():
    return send_from_directory('.', 'photo.jpg')

if __name__ == '__main__':
    app.run()
