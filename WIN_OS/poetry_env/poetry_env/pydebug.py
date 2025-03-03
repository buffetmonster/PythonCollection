import sys
import os
import shutil

# Method 1: Using sys.executable (most reliable)
python_exe_path = sys.executable
print(f"Python executable path (sys.executable): {python_exe_path}")

qmake_path = shutil.which("qmake")

if qmake_path:
    print(f"qmake path: {qmake_path}")
else:
    print("qmake not found.")