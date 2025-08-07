import numpy as np
import pandas as pd
import os, sys
import time
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Function to get the correct path for bundled files
def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Set style for better plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")


print("powered by tinybolt")
df=pd.read_csv(get_resource_path('dataset/parkinsons.data'))
df.head()
features=df.loc[:,df.columns!='status'].values[:,1:]
labels=df.loc[:,'status'].values
print(labels[labels==1].shape[0], labels[labels==0].shape[0])
scaler=MinMaxScaler((-1,1))
x=scaler.fit_transform(features)
y=labels
x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.2, random_state=7)
model=XGBClassifier()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")

# Add 5 second delay before showing visualizations

print("Preparing visualizations...")
time.sleep(5)
print("Loading charts...")

# === VISUALIZATIONS ===

# 1. Class Distribution
plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
class_counts = [labels[labels==0].shape[0], labels[labels==1].shape[0]]
plt.pie(class_counts, labels=['Healthy', 'Parkinson\'s'], autopct='%1.1f%%', startangle=90)
plt.title('Dataset Class Distribution')

# 2. Confusion Matrix
plt.subplot(2, 3, 2)
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Healthy', 'Parkinson\'s'], yticklabels=['Healthy', 'Parkinson\'s'])
plt.title('Confusion Matrix')
plt.ylabel('Actual')
plt.xlabel('Predicted')

# 3. Feature Importance (Top 10)
plt.subplot(2, 3, 3)
feature_names = df.columns[df.columns != 'status'][1:]  # Exclude 'name' and 'status'
importances = model.feature_importances_
indices = np.argsort(importances)[::-1][:10]
plt.bar(range(10), importances[indices])
plt.title('Top 10 Feature Importance')
plt.xticks(range(10), [feature_names[i] for i in indices], rotation=45, ha='right')

# 4. Distribution of a key feature (MDVP:Fo(Hz) - fundamental frequency)
plt.subplot(2, 3, 4)
healthy = df[df['status'] == 0]['MDVP:Fo(Hz)']
parkinsons = df[df['status'] == 1]['MDVP:Fo(Hz)']
plt.hist(healthy, alpha=0.7, label='Healthy', bins=20)
plt.hist(parkinsons, alpha=0.7, label='Parkinson\'s', bins=20)
plt.xlabel('MDVP:Fo(Hz)')
plt.ylabel('Frequency')
plt.title('Fundamental Frequency Distribution')
plt.legend()

# 5. Correlation heatmap of top features
plt.subplot(2, 3, 5)
top_features = [feature_names[i] for i in indices[:8]]
correlation_data = df[top_features + ['status']].corr()
sns.heatmap(correlation_data, annot=True, cmap='coolwarm', center=0, fmt='.2f')
plt.title('Feature Correlation Matrix')

# 6. Prediction Confidence
plt.subplot(2, 3, 6)
y_prob = model.predict_proba(x_test)[:, 1]
plt.hist(y_prob[y_test==0], alpha=0.7, label='Healthy', bins=20)
plt.hist(y_prob[y_test==1], alpha=0.7, label='Parkinson\'s', bins=20)
plt.xlabel('Prediction Probability')
plt.ylabel('Count')
plt.title('Model Confidence Distribution')
plt.legend()

plt.tight_layout()
plt.show()

# Print detailed classification report
print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred, target_names=['Healthy', 'Parkinson\'s']))

print('''
📊 What the visualizations display:
Class Distribution - Pie chart showing the imbalance (75% Parkinson's, 25% Healthy)

Confusion Matrix - Shows prediction accuracy:

True Positives/Negatives
False Positives/Negatives
Feature Importance - Top 10 most important voice features for prediction

Feature Distribution - Histogram comparing healthy vs. Parkinson's patients for key features

Correlation Matrix - How features relate to each other and the target

Prediction Confidence - How confident the model is in its predictions

🎯 Key Insights from Results:
94.87% accuracy - Very good performance!
Perfect recall for Parkinson's (100%) - Catches all Parkinson's cases
High precision for Parkinson's (94%) - Few false positives
The model is slightly conservative with healthy predictions (71% recall)
      
''')

print("The dataset is made by Oxford, courtesy of Oxford & UCI ML Team")
print("MIT License. No Rights Reserved")
print("Ascensus's Machine learning capabilities demo")
print("Have a good day! :)")

# Keep the console window open
print("\n" + "="*50)
print("Press Enter to exit...")
input()