from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load('disease_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            # Get user input
            fever = int(request.form['fever'])
            cough = int(request.form['cough'])
            fatigue = int(request.form['fatigue'])
            headache = int(request.form['headache'])

            # Convert to numpy array for prediction
            features = np.array([[fever, cough, fatigue, headache]])

            # Predict disease
            prediction = model.predict(features)[0]

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
