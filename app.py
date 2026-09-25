from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <style>
            body {
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                font-family: Arial;
                text-align: center;
                padding-top: 100px;
            }
            h1 {
                font-size: 50px;
            }
            p {
                font-size: 22px;
            }
            button {
                padding: 15px 30px;
                font-size: 18px;
                background: white;
                color: #764ba2;
                border: none;
                border-radius: 30px;
                cursor: pointer;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <h1>Hi Sai Naveen! 👋</h1>
        <p>Welcome to My First Website</p>
        <p>It's Working Perfect! ✅</p>
        <button onclick="alert('You are a Rockstar Developer, Sai! 🚀')">Click Me!</button>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
