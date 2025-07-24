import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Python311\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Python311\tcl\tk8.6"

executables = [cx_Freeze.Executable("Face Recognition Software.py", base=base, icon="icon3.ico")]


cx_Freeze.setup(
    name = "Face Recognition Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon3.ico",'tcl86t.dll','tk86t.dll', 'Images','data','database','attendance_report']}},
    version = "1.0",
    description = "Face Recognition Attendace System | Developed By CO4I Students",
    executables = executables
    )