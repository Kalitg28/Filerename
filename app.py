import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'ᴏɴɢᴏɪɴɢ ᴀɴɪᴍᴇ ꜱᴇʀɪᴇꜱ'

if __name__ == "__main__":
    # Get the port from the environment variable, default to 8080 if not set
    port = int(os.environ.get('PORT', 8080))
    # Bind the Flask app to 0.0.0.0 to make it externally accessible
    app.run(host='0.0.0.0', port=port)
