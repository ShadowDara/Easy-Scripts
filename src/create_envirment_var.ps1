# script written by Shadowdara

# Definiere den Namen und Wert der Umgebungsvariable
$EnvName = "MEINE_VAR"
$EnvValue = "MeinWert"

# Setze die Umgebungsvariable für die aktuelle Sitzung
[System.Environment]::SetEnvironmentVariable($EnvName, $EnvValue, "Process")

# Setze die Umgebungsvariable dauerhaft (Benutzerebene)
[System.Environment]::SetEnvironmentVariable($EnvName, $EnvValue, "User")

# Ausgabe der Umgebungsvariable
Write-Host "Umgebungsvariable $EnvName wurde gesetzt auf: $EnvValue"
