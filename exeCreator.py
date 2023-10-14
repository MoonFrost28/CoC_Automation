import PyInstaller.__main__

PyInstaller.__main__.run([
    'Launch_IHM.py',
    '--noconsole',
    '--add-data=images;images',
    '--icon=Images/CoC_icon.ico'
])