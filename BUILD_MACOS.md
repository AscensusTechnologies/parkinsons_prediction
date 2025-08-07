# macOS Build Instructions

## Prerequisites (on macOS):
1. Install Python 3.8+ 
2. Create virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Build Commands:

### Option 1: Create .app bundle
```bash
pyinstaller --onefile --windowed --name "Parkinsons_Predictor" main.py
```

### Option 2: Console version for macOS
```bash
pyinstaller --onefile --console --name "Parkinsons_Predictor_Console" main.py
```

### Option 3: Custom spec file (recommended)
```bash
pyinstaller macos_version.spec
```

## ☁️ Cloud Build Options (for Windows users):

### GitHub Actions (Free)
1. Push code to GitHub repository
2. Set up GitHub Actions workflow with macOS runner
3. Automatically builds .app on every commit
4. Download artifacts from Actions tab

### MacStadium / MacInCloud (Paid)
- Rent macOS cloud instances
- Build directly on remote Mac
- $20-50/month for occasional builds

### AWS EC2 Mac Instances (Paid)
- Official Apple-licensed cloud Macs
- Pay-per-use pricing
- Professional solution for businesses

## Output:
- **dist/Parkinsons_Predictor.app** - GUI version
- **dist/Parkinsons_Predictor_Console** - Terminal version

## Distribution:
- **Direct sharing**: Copy the .app to Applications folder
- **DMG creation**: Use Disk Utility or create-dmg tool
- **Code signing**: Required for distribution (Apple Developer Account needed)

## Universal Binary (Intel + Apple Silicon):
```bash
pyinstaller --target-arch universal2 --onefile main.py
```

## Notes:
- XGBoost works well on macOS
- Matplotlib may need additional configuration
- Consider using conda for easier dependency management on macOS
