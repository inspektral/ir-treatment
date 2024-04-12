
# delete all .wav files that don't end in " 1.wav"
Get-ChildItem -Path .\*.wav -File -Recurse | Where-Object { $_.Name -notlike "* 1.wav" } | Remove-Item -Force

# rename all .wav files to remove the " 1" suffix

$wavFiles = Get-ChildItem -Path .\*.wav -File -Recurse
foreach ($file in $wavFiles) {
    $newName = $file.Name -replace " 1.wav", ".wav"
    Rename-Item -Path $file.FullName -NewName $newName
}
