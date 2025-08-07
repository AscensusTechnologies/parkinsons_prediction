# -*- mode: python ; coding: utf-8 -*-
import sys
from PyInstaller.utils.hooks import collect_data_files, collect_dynamic_libs

# Collect XGBoost data files and dynamic libraries
xgboost_datas = collect_data_files('xgboost')
xgboost_binaries = collect_dynamic_libs('xgboost')

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=xgboost_binaries,
    datas=xgboost_datas + [('dataset', 'dataset')],  # Include dataset folder
    hiddenimports=[
        'xgboost',
        'xgboost.core',
        'xgboost.compat',
        'xgboost.libpath',
        'sklearn.utils._weight_vector',
        'sklearn.neighbors.typedefs',
        'sklearn.neighbors.quad_tree',
        'sklearn.tree._utils'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Parkinsons_Predictor_macOS',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # GUI version for macOS
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch='universal2',  # Universal Binary for Intel + Apple Silicon
    codesign_identity=None,
    entitlements_file=None,
    icon=None  # Add icon='icon.icns' if you have an icon file
)

# Create .app bundle (macOS specific)
app = BUNDLE(
    exe,
    name='Parkinsons_Predictor.app',
    icon=None,  # Add icon='icon.icns' if you have an icon file
    bundle_identifier='com.ascensus.parkinsons-predictor',
    version='1.0.0',
    info_plist={
        'CFBundleName': 'Parkinsons Predictor',
        'CFBundleDisplayName': 'Parkinsons Disease Prediction',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'NSHighResolutionCapable': 'True',
        'NSRequiresAquaSystemAppearance': 'False'
    },
)
