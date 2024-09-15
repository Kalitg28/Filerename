from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Koyeb!'

if __name__ == "__main__":
    # Use the port from the environment variable 'PORT' provided by Koyeb, or default to 8080
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
