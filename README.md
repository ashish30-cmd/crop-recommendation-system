# 🌱 Crop Recommendation System

A Machine Learning-based **Crop Recommendation System** that recommends the most suitable crop based on soil and environmental conditions such as **Nitrogen, Phosphorus, Potassium, temperature, humidity, pH, and rainfall**.

The project uses a **Decision Tree Classifier** to classify the input conditions and predict the recommended crop.

---

## 📌 Project Overview

Choosing the right crop is an important decision in agriculture. Crop selection depends on several factors including soil nutrients, temperature, humidity, soil pH, and rainfall.

This project uses Machine Learning to analyze these parameters and recommend an appropriate crop.

### 🎯 Objective

The main objective of this project is to:

* Analyze agricultural and environmental parameters.
* Train a Machine Learning classification model.
* Predict the most suitable crop for given conditions.
* Save the trained model for future predictions.
* Provide a foundation for integrating the model into a web application or other user interface.

---

## 🤖 Machine Learning Model

This project uses a **Decision Tree Classifier**.

### Why Decision Tree?

Decision Trees are suitable for this problem because they:

* Work well with classification problems.
* Are easy to understand and interpret.
* Require relatively little data preprocessing.
* Can capture non-linear relationships between features.
* Provide fast predictions.

### Model Pipeline

```text
Crop Recommendation Dataset
            ↓
      Data Loading
            ↓
   Feature / Target Split
            ↓
      Label Encoding
            ↓
      Train-Test Split
            ↓
    Decision Tree Model
            ↓
        Prediction
            ↓
   Accuracy Evaluation
            ↓
     Save Model + Encoder
```

---

## 📊 Dataset

The project uses:

```text
Crop_recommendation.csv
```

The dataset contains agricultural and environmental parameters used to recommend crops.

### Input Features

| Feature       | Description                |
| ------------- | -------------------------- |
| `N`           | Nitrogen content in soil   |
| `P`           | Phosphorus content in soil |
| `K`           | Potassium content in soil  |
| `temperature` | Temperature in °C          |
| `humidity`    | Relative humidity          |
| `ph`          | Soil pH value              |
| `rainfall`    | Rainfall in mm             |

### Target

```text
label
```

The `label` column contains the crop name that the model learns to predict.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data loading and manipulation
* **Scikit-learn** – Machine Learning model and evaluation
* **Decision Tree Classifier** – Crop classification
* **LabelEncoder** – Encoding crop labels
* **Joblib** – Saving the trained model and encoder
* **Git & GitHub** – Version control and project hosting

---

## 📁 Project Structure

```text
crop-recommendation-system/
│
├── Crop_recommendation.csv
├── train.py
├── model.pkl
├── encoder.pkl
├── README.md
└── requirements.txt
```

> `model.pkl` and `encoder.pkl` are generated after running the training script.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/ashish30-cmd/crop-recommendation-system.git
```

### 2. Navigate to the project directory

```bash
cd crop-recommendation-system
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install pandas scikit-learn joblib
```

Or, if `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

---

## 🚀 Training the Model

Run the training script:

```bash
python train.py
```

The script will:

1. Load the dataset.
2. Separate features and target.
3. Encode crop labels.
4. Split the dataset into training and testing sets.
5. Train a Decision Tree Classifier.
6. Predict crop labels for the test set.
7. Calculate model accuracy.
8. Save the trained model.
9. Save the label encoder.

Example output:

```text
Model Accuracy: 0.XX
Model and encoder saved successfully.
```

---

## 💾 Generated Files

After training, two files are generated:

### `model.pkl`

Contains the trained Decision Tree model.

### `encoder.pkl`

Contains the `LabelEncoder` used to convert crop names into numerical labels.

Both are required for making predictions later.

---

## 🔮 Making Predictions

Once the model has been trained, it can be loaded using Joblib:

```python
import joblib

model = joblib.load("model.pkl")
encoder = joblib.load("encoder.pkl")
```

For example:

```python
sample = [[90, 42, 43, 20.8, 82.0, 6.5, 202.9]]

prediction = model.predict(sample)

crop = encoder.inverse_transform(prediction)

print("Recommended Crop:", crop[0])
```

---

## 📈 Model Evaluation

The model is evaluated using **Accuracy Score**.

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)
```

The dataset is divided into:

```text
80% → Training Data
20% → Testing Data
```

using:

```python
train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42
)
```

---

## 🔄 Future Improvements

This project can be extended in several ways:

* [ ] Build a Streamlit web application.
* [ ] Add user-friendly input forms.
* [ ] Compare Decision Tree with Random Forest, SVM, KNN, and other models.
* [ ] Perform hyperparameter tuning.
* [ ] Add confusion matrix and classification report.
* [ ] Add feature importance visualization.
* [ ] Deploy the application online.
* [ ] Add weather API integration.
* [ ] Provide crop-specific information such as growing season and water requirements.

---

## ⚠️ Disclaimer

This project is developed for **educational and demonstration purposes**. The recommendations generated by the model should not be treated as professional agricultural advice.

Actual crop selection should also consider factors such as local climate, soil characteristics, market conditions, irrigation availability, and expert agricultural guidance.

---

## 👨‍💻 Author

**Ashish Kumar**

GitHub:
`https://github.com/ashish30-cmd`

---

## ⭐ If You Like This Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📜 License

This project is intended for educational purposes. You may modify and extend it for learning and development.
