# Crop Prediction Model

## Overview
This project aims to predict the type of crop that can be grown based on soil nutrient levels (Nitrogen, Phosphorus, Potassium) and pH. The model uses logistic regression to classify crops based on these features and is evaluated using the F1 score.

## Dataset
The dataset used in this project contains the following columns:
- **N**: Nitrogen level in the soil (numeric)
- **P**: Phosphorus level in the soil (numeric)
- **K**: Potassium level in the soil (numeric)
- **ph**: pH level of the soil (numeric)
- **crop**: Type of crop (target variable; could be multi-class)

### Data Exploration
Before training the model, the dataset was explored to:
- Check for missing values.
- Determine if the target variable (`crop`) is binary or multi-class.
- Examine the unique crop types to understand the classification problem.

## Methodology
1. **Data Preprocessing**:
   - Handled missing values (if any).
   - Standardized features (N, P, K, and pH) using `StandardScaler`.
   - Split the data into training and testing sets (70% training, 30% testing).
   
2. **Model Training**:
   - Trained a **Logistic Regression** model on each feature independently and evaluated performance using F1 score.
   - Also trained the model using all features together to improve accuracy.

3. **Model Evaluation**:
   - The model was evaluated using **F1 score** (weighted average).
   - Additional metrics like **accuracy**, **confusion matrix**, and **classification report** were also used to evaluate the performance.

4. **Best Feature Selection**:
   - The feature with the highest F1 score was identified as the best predictive feature for crop prediction.

## Requirements
This project requires the following Python libraries:
- `pandas`
- `scikit-learn`
- `matplotlib` (for visualizations, if any)

Install the required dependencies using:
```bash
pip install -r requirements.txt
