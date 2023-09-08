from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy user data
user_data = {
    "full_name": "John Doe",
    "dob": "17091999",
    "email": "john@xyz.com",
    "roll_number": "ABCD123",
}

# POST method endpoint
@app.route('/bfhl', methods=['POST'])
def post_bfhl():
    try:
        data = request.get_json()
        input_data = data.get("data")

        # Extract numbers and alphabets
        numbers = [x for x in input_data if x.isdigit()]
        alphabets = [x for x in input_data if x.isalpha()]

        # Find the highest alphabet
        highest_alphabet = max(alphabets, key=lambda x: x.lower())

        response_data = {
            "is_success": True,
            "user_id": f"{user_data['full_name'].replace(' ', '_')}_{user_data['dob']}",
            "email": user_data["email"],
            "roll_number": user_data["roll_number"],
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": [highest_alphabet],
        }

        return jsonify(response_data), 200
    except Exception as e:
        return jsonify({"is_success": False, "error_message": str(e)}), 400

# GET method endpoint
@app.route('/bfhl', methods=['GET'])
def get_bfhl():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
