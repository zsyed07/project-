import os
from flask import Flask

app = Flask(__name__)

@app.route('/word',methods=['GET'])
def home():
    return "Hello, FRIENDS! The app is live!"

if __name__ == "__main__":
    # Get the port number from the environment (set by the hosting platform)
    port = int(os.environ.get("PORT", 10000))
    # Ensure the app listens on all available network interfaces
    app.run(host="0.0.0.0", port=port)
