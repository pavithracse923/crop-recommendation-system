Crop Recommendation System
The Crop Recommendation System is a web-based application that helps farmers select the best crops for cultivation based on soil, weather, and environmental factors. It uses machine learning to provide accurate recommendations and forecasts.

Features
Crop Suggestions: Recommends suitable crops based on soil and weather conditions.
Weather Forecast: Displays temperature, rainfall, and humidity predictions.
Easy-to-Use Interface: Clean and responsive design for seamless navigation.
Technologies Used
Backend: Flask (Python)
Frontend: HTML, CSS, JavaScript, Bootstrap
Machine Learning: Decision Tree Classifier, LSTM Model
APIs: OpenWeatherMap for weather data
How It Works
Input: Enter soil properties and current weather details.
Processing: Machine learning models analyze the data.
Output: Provides crop recommendations and weather forecasts.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/pavithracse923/crop-recommendation-system.git
cd crop-recommendation-system
Install required packages:

bash
Copy code
pip install -r requirements.txt
Add your API key in .env:

makefile
Copy code
WEATHER_API_KEY=your_api_key
Run the app:

bash
Copy code
python app.py
Open http://127.0.0.1:5000 in your browser.

Future Plans
Add more soil and crop types.
Mobile app version.
Support for local languages.
