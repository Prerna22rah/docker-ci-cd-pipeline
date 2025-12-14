from flask import Flask #last time hai ye ab
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from peros ab karde yaar please ab Dockerized Flask App with CI/CD!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)




