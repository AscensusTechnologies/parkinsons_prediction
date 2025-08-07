# Easy macOS Installation for Your Friends

## For Mac Users (No Windows exe needed!)

### Step 1: Install Python
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python
```

### Step 2: Download and Setup Project
```bash
# Clone or download the project
git clone https://github.com/AscensusTechnologies/parkinsons_prediction.git
cd parkinsons_prediction

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python main.py
```

That's it! The Python script will work identically on macOS with the same visualizations and results.

## Alternative: Send as ZIP Package
1. Zip your entire project folder (including dataset)
2. Your Mac friends follow the steps above
3. No exe needed - Python works cross-platform!

## Why This is Better Than EXE:
- ✅ Smaller download size
- ✅ No compatibility issues  
- ✅ Always up-to-date Python libraries
- ✅ Easy to modify/customize
- ✅ Native macOS performance
