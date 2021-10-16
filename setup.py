import cx_Freeze

executables = [cx_Freeze.Executable('Qr Code Creator - App.py', icon='View/RC/Qr-Code-Creator.ico', base='Win32GUI')]

cx_Freeze.setup(
    name="QrCode Creator",
    options={'build_exe': {'packages': ['PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets', 'os', 'sys', 'shutil','tkinter.filedialog', 'qrcode'],
                           'include_files': ['View/']}},
    executables=executables
)