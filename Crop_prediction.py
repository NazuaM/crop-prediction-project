import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

# Load the dataset
crops = pd.read_csv("soil_measures.csv")

print(crops.isna().sum().sort_values()) #checking for missing values
print(crops['crop'].unique()) #checking if target is binary or multi-classification

y = crops['crop'].values  #target variable

results = {}
names = ['N', 'P', 'K', 'ph'] 

for name in names:
    X = crops[name].values.reshape(-1,1) #features
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)  #split data
    scaled = StandardScaler()
    X_train_scaled = scaled.fit_transform(X_train)
    X_test_scaled = scaled.transform(X_test)
    
    model = LogisticRegression() #instantiate model
    model.fit(X_train_scaled, y_train) #fit training data
    
    y_pred = model.predict(X_test_scaled) #predict test data
    f1_score = metrics.f1_score(y_test, y_pred, average='weighted') #comoute metric for evaluation
    results[name] = f1_score
    
    
max_key = max(results, key=results.get)
best_predictive_feature = {max_key: results[max_key]}
print(best_predictive_feature)
    


