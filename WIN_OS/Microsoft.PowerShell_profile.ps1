#The windows powershell console has a profile ps1 file, to find location: $profile
#for example this might be: C:\Users\theuser\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
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
ECHO "Added Alias: go_virtualenv"
ECHO "Added Alias: go_createenv"
ECHO "Added Alias: go_pythonrepo"

Write-Host "Instead of using go_createenv you can use SetUpEnv.bat which also installs all the required modules.`nThis can be found in the WiFi directory."
ECHO " However you still need to start the virtual env with go_virtualenv macro alias"