# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [
    ( 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\screen_recorder_sdk\\lib\\ScreenRecorder.dll', '.' ),
    ( 'config.ini', '.' ),
    ( 'icons\\own.ico', 'icons' )
]

a = Analysis(['gui.py'],
             pathex=['C:\\Users\\User\\Desktop\\OWNotify'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='OWNotify',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='icons\\own.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=['vcruntime140.dll'],
               name='OWNotify')
