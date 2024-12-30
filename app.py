from flask import Flask, request, jsonify

# Create the Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, world! This is my Flask app."

# Define a route that will handle POST requests
@app.route('/receive', methods=['POST'])
def receive_data():
    # Get the JSON data sent to the server
    data = request.get_json()

    # If no data is sent, return an error
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Process the data (e.g., print it to the console)
    print(f"Received data: {data}")

    # Return a JSON response
    return jsonify({"message": "Data received successfully", "received_data": data})

# Run the Flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
