# GitHub Actions macOS Build Guide

## 🚀 Steps to Build macOS App using GitHub Actions:

### Step 1: Push to GitHub
```bash
# Add all files to git
git add .

# Commit changes
git commit -m "Add macOS build workflow and specs"

# Push to GitHub (make sure repository is public for free Actions)
git push origin main
```

### Step 2: Trigger the Build
1. **Automatic**: Build runs automatically when you push to main branch
2. **Manual**: Go to "Actions" tab → "Build macOS App" → "Run workflow"

### Step 3: Monitor the Build
1. Go to your repository on GitHub
2. Click "Actions" tab
3. Click on the latest workflow run
4. Watch the progress (takes ~10-15 minutes)

### Step 4: Download Your macOS App
Once the build completes successfully:
1. Scroll down to "Artifacts" section
2. Download **both**:
   - `parkinsons-predictor-macos-app` (the .app file)
   - `parkinsons-predictor-macos-dmg` (installer disk image)

### Step 5: Share with Mac Friends
**Option A - Send .app file:**
```bash
# Your Mac friends can:
1. Download and extract the .app
2. Right-click → "Open" (to bypass Gatekeeper)
3. Move to Applications folder
```

**Option B - Send DMG file:**
```bash
# Your Mac friends can:
1. Download the .dmg file
2. Double-click to mount
3. Drag app to Applications folder
4. Eject the disk image
```

## 🔧 Troubleshooting:

### If Build Fails:
1. Check "Actions" tab for error details
2. Common issues:
   - **Deprecated actions**: We've updated to latest versions (v4/v5)
   - **Missing dataset files**: Ensure dataset folder is committed
   - **Python dependency conflicts**: Check requirements.txt
   - **PyInstaller spec file errors**: Verify macos_version.spec syntax

### If Actions Are Deprecated:
- ✅ **Fixed**: Updated to `actions/upload-artifact@v4` and `actions/setup-python@v5`
- If you see deprecation warnings, the workflow will auto-update

### If App Won't Run on Mac:
1. **Gatekeeper Issue**: Right-click → "Open" instead of double-click
2. **Missing Dependencies**: Check that all libraries were bundled
3. **Architecture Issue**: Build Universal Binary for both Intel/Apple Silicon

## 📋 What Gets Built:
- ✅ **Parkinsons_Predictor.app** - Standalone macOS application
- ✅ **Parkinsons-Predictor-macOS.dmg** - Professional installer
- ✅ **Universal Binary** - Works on both Intel and Apple Silicon Macs
- ✅ **Dataset Included** - No additional files needed

## 💰 Cost:
- **FREE** for public repositories (2000 minutes/month)
- **Paid** for private repositories (~$0.08/minute)

## ⏱️ Build Time:
- Typical build: 10-15 minutes
- Includes Python setup, dependency installation, and PyInstaller packaging
