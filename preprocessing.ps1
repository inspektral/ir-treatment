python ./wir2wav.py

Get all WAV files in subfolders
$wavFiles = Get-ChildItem -Path .\*.wav -File -Recurse
Write-Host "Found $($wavFiles.Count) WAV files in subfolders."

# Move WAV files to current folder
foreach ($file in $wavFiles) {
    Move-Item -Path $file.FullName -Destination .\
}

#delete .wir and .xps files in subfolders
Get-ChildItem -Path .\*\*.wir -File -Recurse | Remove-Item -Force
Get-ChildItem -Path .\*\*.xps -File -Recurse | Remove-Item -Force

# Delete empty subfolders
Get-ChildItem -Path .\* -Directory -Recurse | Where-Object { $_.GetFiles().Count -eq 0 } | Remove-Item -Force

python ./renamer.py

# delete all .wav files that don't end in " 1.wav"
# Get-ChildItem -Path .\*.wav -File -Recurse | Where-Object { $_.Name -notlike "* 1.wav" } | Remove-Item -Force