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
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='parkinsons_predictor_console',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Show console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None
)
