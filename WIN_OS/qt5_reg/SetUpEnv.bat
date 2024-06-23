rem SETUP Python virtual env and install modules, then start python application
rem Unfortuanely env is terminated when env end, hence calling python app with
rem I'm sure this can be adapted but does the job for now.
rem altenativly manually start the env outside the script .\venv\Scripts\activate

@ECHO OFF

:: Check if the 'deactivate' command exists
where deactivate > NUL 2>&1

:: If 'deactivate' is found, deactivate the virtual environment
IF %ERRORLEVEL% EQU 0 (
    ECHO Virtualenv will be deactivated.
    CALL deactivate
) ELSE (
    ECHO Virtualenv is not activated, continue.
)

where python3 > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 (
  ECHO Python 3 is not installed. Please install it from https://www.python.org/downloads/
  EXIT /B 1
) ELSE (
  ECHO Python 3 is installed.
)

ECHO "Creating virtualenv..."
python3 -m venv .\venv

ECHO "Activate the virtual environment"

rem cmd /K ".\venv\Scripts\activate; pip3 install -r requirements.txt"
rem pip3 install -r requirements.txt
CALL .\venv\Scripts\activate
CALL pip3 install -r requirements.txt
CALL python.exe .\hello-qt5-gui.py


