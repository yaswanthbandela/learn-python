import os #importing a library into your code

print(os.system('powershell -Command "Get-PSDrive -PSProvider FileSystem | Select-Object Name, @{Name=\\"FreeSpace(GB)\\";Expression={[math]::round($_.Free/1GB,2)}}, @{Name=\\"TotalSize(GB)\\";Expression={[math]::round($_.Used/1GB + $_.Free/1GB,2)}}'))
print(os.system(' systeminfo | findstr /C:"Total Physical Memory"'))

print(os.system('systeminfo'))