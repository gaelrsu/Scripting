```powershell
# Créer une instance d'Excel
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $true

# Créer un nouveau classeur Excel
$workbook = $excel.Workbooks.Add()

# Obtenir la première feuille de calcul
$worksheet = $workbook.Worksheets.Item(1)
$worksheet.Name = "Informations système"




# Récupérer le nom de la machine
$ComputerName = [System.Environment]::MachineName

# Récupérer l'adresse IP, le masque et la passerelle

$IPAddress = (Get-NetIPAddress -AddressFamily IPv4).IPAddress -join ", "
$SubnetMask = (Get-NetIPAddress -AddressFamily IPv4).PrefixLength -join ", "
$Gateway = (Get-NetIPConfiguration | Foreach IPv4DefaultGateway).NextHop

# Récupérer la version du système d'exploitation et la licence
$OSInfo = Get-WmiObject -Class Win32_OperatingSystem
$OSVersion = [System.Environment]::OSVersion.Version
$OSLicense = (Get-WmiObject -query ‘select * from SoftwareLicensingService’).OA3xOriginalProductKey
$OSSerial = (Get-WmiObject win32_bios).Serialnumber

# Récupérer les infos du processeur
$Proc = (Get-WmiObject Win32_Processor).Name

# Récupérer les capacités de la ram
$RAM = [math]::Round((Get-WmiObject -Class Win32_ComputerSystem).TotalPhysicalMemory / 1GB)

# Écrire les données dans le tableau Excel
$worksheet.Cells.Item(1, 1) = "Nom de la machine"
$worksheet.Cells.Item(1, 2) = $ComputerName
$worksheet.Cells.Item(2, 1) = "Adresse IP"
$worksheet.Cells.Item(2, 2) = $IPAddress
$worksheet.Cells.Item(3, 1) = "Masque de sous-réseau"
$worksheet.Cells.Item(3, 2) = $SubnetMask
$worksheet.Cells.Item(4, 1) = "Passerelle"
$worksheet.Cells.Item(4, 2) = $Gateway
$worksheet.Cells.Item(5, 1) = "Version du système d'exploitation"
$worksheet.Cells.Item(5, 2) = $OSVersion
$worksheet.Cells.Item(6, 1) = "Licence du système d'exploitation"
$worksheet.Cells.Item(6, 2) = $OSLicense
$worksheet.Cells.Item(7, 1) = "Numero de serie"
$worksheet.Cells.Item(7, 2) = $OSSerial
$worksheet.Cells.Item(8, 1) = "Processeur"
$worksheet.Cells.Item(8, 2) = $Proc
$worksheet.Cells.Item(9, 1) = "RAM"
$worksheet.Cells.Item(9, 2) = $RAM

# Sauvegarder le classeur Excel
$excelFilePath = "C:\$ComputerName.xlsx"
$workbook.SaveAs($excelFilePath)

# Fermer Excel
$excel.Quit()

# Libérer les objets COM
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($worksheet)
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($workbook)
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel)
Remove-Variable excel
Remove-Variable workbook
Remove-Variable worksheet

Write-Host "Les informations ont été exportées vers $excelFilePath."
```
