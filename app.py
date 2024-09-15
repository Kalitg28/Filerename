from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '@JishuDeveloper'

if __name__ == "__main__":
    # Bind to 0.0.0.0 and port 8080 to work with Koyeb
    app.run(host='0.0.0.0', port=8080)
