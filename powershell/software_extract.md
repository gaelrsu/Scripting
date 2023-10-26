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

# Récupérer la liste des logiciels
$SoftwareList = Get-WmiObject Win32_Product -ComputerName $ComputerName | Select-Object Name, Vendor, Version

# Écrire les en-têtes dans le tableau Excel
$worksheet.Cells.Item(1, 1) = "Logiciel"
$worksheet.Cells.Item(1, 2) = "Fournisseur"
$worksheet.Cells.Item(1, 3) = "Version"

# Écrire les données des logiciels dans le tableau Excel
$row = 2  # Commencer à la deuxième ligne
foreach ($software in $SoftwareList) {
    $worksheet.Cells.Item($row, 1) = $software.Name
    $worksheet.Cells.Item($row, 2) = $software.Vendor
    $worksheet.Cells.Item($row, 3) = $software.Version
    $row++
}

# Sauvegarder le classeur Excel
$excelFilePath = "C:\($ComputerName)_soft.xlsx"
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

Write-Host "Les informations sur les logiciels ont été exportées vers $excelFilePath."
```
