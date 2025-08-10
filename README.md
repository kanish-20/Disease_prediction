# 🩺 Disease Prediction using KNN
This project is a Machine Learning Flask Web App that predicts a disease based on symptoms entered by the user.
It uses the K-Nearest Neighbors (KNN) algorithm for classification.

## 📌 Features
Predicts disease from given symptoms

Interactive web interface using Flask

Styled with HTML & CSS

Uses KNN machine learning model

Supports multiple diseases (extendable with more data)

## 📂 Project Structure

```
Disease_pred/
│-- app.py                  # Flask web app
│-- train_model.py           # Trains the KNN model
│-- disease_data.csv         # Dataset with symptoms & diseases
│-- templates/
│   └── index.html           # Frontend HTML
│-- static/
│   └── style.css            # CSS styling
│-- model.pkl                # Saved trained model
│-- requirements.txt         # Python dependencies
│-- README.md                # Project documentation
```

## ⚙️ Installation & Usage

### 1️⃣ Clone the repository
```
git clone https://github.com/yourusername/disease-prediction-knn.git
cd disease-prediction-knn
```
### 2️⃣ Install dependencies
```
pip install -r requirements.txt
```
### 3️⃣ Train the model
```
python train_model.py
```
### 4️⃣ Run the Flask app
```
python app.py
```
### 5️⃣ Open in browser
```
Go to: http://127.0.0.1:5000/
```

## 📊 Dataset

The dataset contains symptom features and target disease labels.

You can add more diseases and symptoms to improve accuracy.

## Screenshots

![WhatsApp Image 2025-08-10 at 20 08 56](https://github.com/user-attachments/assets/f9bae508-df45-4cf7-9743-d87a8615a607)
![WhatsApp Image 2025-08-10 at 20 08 56 (1)](https://github.com/user-attachments/assets/5af2f1fa-cc79-4e5b-ab18-03416cdfeb7c)
![WhatsApp Image 2025-08-10 at 20 08 56 (2)](https://github.com/user-attachments/assets/d14b5cf4-dd54-4134-a2e4-861bc0c1d69a)



