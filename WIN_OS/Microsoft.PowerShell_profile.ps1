#The windows powershell console has a profile ps1 file, to find location: $profile
#for example this might be: C:\Users\theuser\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
#Using this alias we can easily enable the python virtualenv assuming it is setup
#by editing Microsoft.PowerShell_profile.ps1 we can add some alises related to the powershell
#some weirdo restriction prevents creating the powershell directory using console, use file explorer to create it
#below useful if restriction not present
#mkdir ~\Documents\WindowsPowerShell
#echo "" > ~\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
#cp WindowsProfileSetup.txt ~\WindowsPowerShell\Microsoft.PowerShell_profile.ps1

#Alias doesn't like passing params, can use function or use cmd hack to get the job done
#function go_createenv {
#  python3 -m venv ./venv
#}
New-Alias go_createenv "cmd /c python3 -m venv ./venv"
New-Alias go_virtualenv .\venv\Scripts\activate
function go_pythonrepo {
    cd \GitRepos\PythonCollection\WIN_OS
}
#setup enviromental stuff:
# For User variables (current user):
# Modify the User-level PATH (no admin rights needed):
$newPath = "C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\dotnet\;C:\Program Files\PuTTY\;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\dotnet\;C:\Program Files\PuTTY\;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\dotnet\;C:\Program Files\PuTTY\;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\dotnet\;C:\Program Files\PuTTY\;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\dotnet\;C:\Program Files\PuTTY\;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\dotnet\;C:\Program Files\PuTTY\;C:\Users\Dave.Swan\AppData\Local\Microsoft\WindowsApps;C:\Users\Dave.Swan\AppData\Local\Programs\Microsoft VS Code\bin;C:\Users\Dave.Swan\AppData\Local\Programs\Git\cmd\;C:\Users\Dave.Swan\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\;C:\Users\Dave.Swan\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts\;"

[Environment]::SetEnvironmentVariable("Path", $newPath, "User")

#for poetry:
#C:\Users\Dave.Swan\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts
#C:\Users\Dave.Swan\AppData\Local\Programs\Git\cmd;C:\GitRepos\PythonCollection\WIN_OS\qt6_gui\venv\Scripts\

$env:Path
ECHO "Added Alias: go_virtualenv"
ECHO "Added Alias: go_createenv"
ECHO "Added Alias: go_pythonrepo"

Write-Host "Instead of using go_createenv you can use SetUpEnv.bat which also installs all the required modules.`nThis can be found in the WiFi directory."
ECHO " However you still need to start the virtual env with go_virtualenv macro alias"