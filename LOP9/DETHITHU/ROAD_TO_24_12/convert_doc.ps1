$word = New-Object -ComObject Word.Application
$word.Visible = $false
$docPath = 'd:\GitHub\SOANBAI-main\LOP9\DETHITHU\ROAD_TO_24_12\1. CUỐI KÌ I MÔN TOÁN LỚP 9.docx'
$pdfPath = 'd:\GitHub\SOANBAI-main\LOP9\DETHITHU\ROAD_TO_24_12\de_thi.pdf'
$doc = $word.Documents.Open($docPath)
$doc.SaveAs([ref]$pdfPath, [ref]17)
$doc.Close()
$word.Quit()
Write-Host "Exported to PDF successfully!"
