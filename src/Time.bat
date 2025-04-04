@echo off
setlocal

:: Aktuelles Datum und Uhrzeit in Variablen speichern
set "datum=%date%"
set "uhrzeit=%time%"

:: Leerzeichen in der Uhrzeit durch Nullen ersetzen, um ein konsistentes Format zu gewährleisten
set "uhrzeit=%uhrzeit: =0%"

:: Datum und Uhrzeit in die Datei "Edittime.txt" schreiben
echo %datum% %uhrzeit% > Edittime.txt

endlocal
