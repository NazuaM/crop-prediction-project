## Crop Prediction Model

A machine learning model to predict the best crop to grow based on soil nutrient levels (Nitrogen, Phosphorus, Potassium) and pH. The model uses **Logistic Regression** and is evaluated using the **F1 score**.

## 📁 Dataset
The dataset contains the following columns:

- **N**: Nitrogen level in the soil (numeric)  
- **P**: Phosphorus level in the soil (numeric)  
- **K**: Potassium level in the soil (numeric)  
- **ph**: pH level of the soil (numeric)  
- **crop**: Target variable (type of crop; multi-class)

## 📊 Data Exploration
- Checked for missing values  
- Determined target variable type (multi-class)  
- Examined unique crop types to understand the classification problem  

## 🛠 Methodology
**Data Preprocessing:**
- Handled missing values  
- Standardized features using `StandardScaler`  
- Split data into 70% training and 30% testing  

**Model Training:**
- Trained Logistic Regression on each feature independently  
- Trained using all features together for better accuracy  

**Model Evaluation:**
- Evaluated using **F1 score**, accuracy, confusion matrix, and classification report  
- Selected the feature with the highest predictive power for crop prediction  

## 🧰 Tech Stack
- Python  
- pandas  
- scikit-learn  
- matplotlib (optional, for visualizations)

## 📁 Project Structure

crop-prediction-project/
├── Crop_prediction.py
├── soil_measures.csv
├── README.md
└── farmer-8294716_1280.webp (thumbnail)
