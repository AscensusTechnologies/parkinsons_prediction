# Parkinsons Disease Prediction using Machine Learning

This project uses XGBoost to predict Parkinson's disease from voice recordings with 94.87% accuracy.

## 🚀 Features

- **Machine Learning Model**: XGBoost classifier trained on voice features
- **Comprehensive Visualizations**: 6 different charts showing model performance
- **Cross-Platform Executables**: Windows (.exe) and macOS (.app) versions available
- **High Accuracy**: 94.87% prediction accuracy with detailed classification metrics

## 📊 What the visualizations display:

- **Class Distribution**: Pie chart showing the imbalance (75% Parkinson's, 25% Healthy)
- **Confusion Matrix**: Shows prediction accuracy with True/False Positives/Negatives
- **Feature Importance**: Top 10 most important voice features for prediction
- **Feature Distribution**: Histogram comparing healthy vs. Parkinson's patients for key features
- **Correlation Matrix**: How features relate to each other and the target
- **Prediction Confidence**: How confident the model is in its predictions

## 🎯 Key Results:
- **94.87% accuracy** - Very good performance!
- **Perfect recall for Parkinson's (100%)** - Catches all Parkinson's cases
- **High precision for Parkinson's (94%)** - Few false positives
- **Conservative with healthy predictions (71% recall)**

## 🔧 Installation & Usage

### Requirements
```bash
pip install -r requirements.txt
```

### Run Python Script
```bash
python main.py
```

### Windows Executable
- **GUI Version**: `dist/parkinsons_predictor.exe`
- **Console Version**: `dist/parkinsons_predictor_console.exe`

### macOS Build
See [BUILD_MACOS.md](BUILD_MACOS.md) for detailed instructions.

## 📈 Dataset
- **Source**: Oxford Parkinson's Disease Detection Dataset (UCI ML Repository)
- **Features**: 22 voice measurement attributes
- **Samples**: 195 voice recordings (147 Parkinson's, 48 Healthy)

## 🏗️ Building Executables

### Windows
```bash
pyinstaller console_version.spec  # Console version
pyinstaller main_fixed.spec       # GUI version
```

### macOS (requires macOS machine)
```bash
pyinstaller macos_version.spec
```

## 📜 License
MIT License - No Rights Reserved

**Powered by tinybolt by Ascensus**
remix of data-flair.training's version (the code was depriciated, it is now fixed and the algo was made better i think?)
High precision for Parkinson's (94%) - Few false positives

The model is slightly conservative with healthy predictions (71% recall)

