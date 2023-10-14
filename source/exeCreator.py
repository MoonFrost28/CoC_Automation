import PyInstaller.__main__

PyInstaller.__main__.run([
    'source/Launch_IHM.py',
    '--onefile',
    '--noconsole',
    '--noconfirm',
    '--add-data=Images;Images',
    '--icon=Images/CoC_icon.ico',
    '--clean',
    '--distpath=.'
])