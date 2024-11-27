from flask import Flask, request, render_template
import numpy as np
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained model and scalers
try:
    model = pickle.load(open('model.pkl', 'rb'))
    sc = pickle.load(open('standscaler.pkl', 'rb'))
    mx = pickle.load(open('minmaxscaler.pkl', 'rb'))
except FileNotFoundError as e:
    print(f"Error: {e}")
    print("Ensure all required files (model.pkl, standscaler.pkl, minmaxscaler.pkl) are in the same directory.")
    exit(1)  # Exit if files are missing

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to display the prediction form
@app.route("/predict")
def enter_land():
    return render_template("predict.html")

# Route to handle prediction logic
@app.route("/predict", methods=['POST'])
def predict():
    try:
        # Get form data
        N = float(request.form.get('Nitrogen', 0))
        P = float(request.form.get('Phosporus', 0))
        K = float(request.form.get('Potassium', 0))
        temp = float(request.form.get('Temperature', 0))
        humidity = float(request.form.get('Humidity', 0))
        ph = float(request.form.get('pH', 0))
        rainfall = float(request.form.get('Rainfall', 0))

        # Prepare input features for prediction
        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1, -1)

        # Scale the features using MinMaxScaler and StandardScaler
        mx_features = mx.transform(single_pred)
        sc_mx_features = sc.transform(mx_features)

        # Make a prediction
        prediction = model.predict(sc_mx_features)

        # Crop dictionary mapping prediction index to crop names
        crop_dict = {
            1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
            8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
            14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
            19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
        }

        # Determine the best crop based on the prediction
        if prediction[0] in crop_dict:
            crop = crop_dict[prediction[0]]
            result = f"{crop} is the best crop to be cultivated right there"
        else:
            result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
            crop = None

        # Render the result page, passing the result and the predicted crop
        return render_template('result.html', result=result, crop=crop)

    except Exception as e:
        # Handle errors and display a message
        error_message = f"An error occurred during prediction: {e}"
        return render_template('error.html', error_message=error_message)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
