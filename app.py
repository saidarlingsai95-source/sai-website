from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/')
def home():
    return '''
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{margin:0;font-family:Arial;background:#0f172a;color:white;text-align:center}
.card{max-width:400px;margin:40px auto;background:white;color:#0f172a;border-radius:20px;padding:30px;box-shadow:0 10px 30px rgba(0,0,0,0.3)}
img{width:150px;height:150px;border-radius:50%;object-fit:cover;border:4px solid #3b82f6}
h1{margin:15px 0 5px 0}
p{color:#64748b}
.btn{display:inline-block;margin:10px;padding:12px 25px;background:#3b82f6;color:white;border-radius:30px;text-decoration:none;font-weight:bold}
.skills span{display:inline-block;background:#e0f2fe;color:#0284c7;padding:5px 12px;border-radius:20px;margin:5px;font-size:14px}
</style>
</head>
<body>
<div class="card">
<img src="/photo.jpg">
<h1>Sai Naveen</h1>
<p>Web Developer | Hyderabad</p>
<p>Hi! I built this website myself. I love coding!</p>
<div class="skills">
<span>Python</span><span>Flask</span><span>HTML</span><span>GitHub</span><span>Render</span>
</div>
<br>
<a class="btn" href="https://github.com/saidarlingsai95-source">My GitHub</a>
<a class="btn" style="background:#0f172a" href="#">Contact Me</a>
<p style="margin-top:20px;font-size:12px">Live Website ✅</p>
</div>
</body>
</html>
    '''

@app.route('/photo.jpg')
def photo():
    return send_from_directory('.', 'photo.jpg')

if __name__ == '__main__':
    app.run()
