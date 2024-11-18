from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the calorie prediction function
def predict_calories(age, gender, weight, height, activity_level):
    # Base calculation using the Harris-Benedict equation
    if gender.lower() == 'male':
        base_calories = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        base_calories = 10 * weight + 6.25 * height - 5 * age - 161

    # Adjust for activity level
    predicted_calories = base_calories * activity_level
    return round(predicted_calories, 2)

# Define a route for the prediction API
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.json

        # Extract values
        age = data.get('age')
        gender = data.get('gender')
        weight = data.get('weight')
        height = data.get('height')
        activity_level = data.get('activity_level')

        # Validate input
        if not all([age, gender, weight, height, activity_level]):
            return jsonify({"error": "Missing required fields"}), 400

        # Perform prediction
        calories = predict_calories(age, gender, weight, height, activity_level)

        # Return the result
        return jsonify({"predicted_calories": calories})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
