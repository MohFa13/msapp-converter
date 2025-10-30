# PowerApps Canvas App Structure Validator
# Run this script to verify all required files are present

Write-Host "Validating Power Apps Canvas App Structure..." -ForegroundColor Cyan

$requiredFiles = @(
    "CanvasManifest.json",
    "Header.json",
    "Entropy.json",
    "checksum.json",
    "Resources.json",
    "Connections.json",
    "ComponentReferences.json",
    "ControlTemplates.json"
)

$requiredDirs = @(
    "Src",
    "Assets",
    "DataSources"
)

$missingFiles = @()
$missingDirs = @()

# Check files
foreach ($file in $requiredFiles) {
    if (-not (Test-Path $file)) {
        $missingFiles += $file
        Write-Host "✗ Missing: $file" -ForegroundColor Red
    } else {
        Write-Host "✓ Found: $file" -ForegroundColor Green
    }
}

# Check directories
foreach ($dir in $requiredDirs) {
    if (-not (Test-Path $dir -PathType Container)) {
        $missingDirs += $dir
        Write-Host "✗ Missing directory: $dir" -ForegroundColor Red
    } else {
        Write-Host "✓ Found directory: $dir" -ForegroundColor Green
    }
}

# Validate CanvasManifest.json
if (Test-Path "CanvasManifest.json") {
    try {
        $manifest = Get-Content "CanvasManifest.json" -Raw | ConvertFrom-Json
        Write-Host "✓ CanvasManifest.json is valid JSON" -ForegroundColor Green
        Write-Host "  FormatVersion: $($manifest.FormatVersion)" -ForegroundColor Gray
        Write-Host "  MSAppStructureVersion: $($manifest.Header.MSAppStructureVersion)" -ForegroundColor Gray
        Write-Host "  DocVersion: $($manifest.Header.DocVersion)" -ForegroundColor Gray
    } catch {
        Write-Host "✗ CanvasManifest.json is not valid JSON: $_" -ForegroundColor Red
    }
}

# Check Src files
Write-Host "`nChecking Src directory..." -ForegroundColor Cyan
$srcFiles = @(
    "Src/App.fx_1761820299719.yaml",
    "Src/App.pa_1761820299718.yaml",
    "Src/Screen1.fx.yaml",
    "Src/Screen1.pa.yaml",
    "Src/_EditorState.pa_1761820299719.yaml"
)

foreach ($file in $srcFiles) {
    if (Test-Path $file) {
        Write-Host "✓ Found: $file" -ForegroundColor Green
    } else {
        Write-Host "✗ Missing: $file" -ForegroundColor Red
        $missingFiles += $file
    }
}

# Summary
Write-Host "`n========================================" -ForegroundColor Cyan
if ($missingFiles.Count -eq 0 -and $missingDirs.Count -eq 0) {
    Write-Host "✓ All required files and directories are present!" -ForegroundColor Green
    Write-Host "`nYou can now run:" -ForegroundColor Cyan
    Write-Host "  pac canvas pack --sources . --msapp App.msapp" -ForegroundColor Yellow
} else {
    Write-Host "✗ Structure validation failed!" -ForegroundColor Red
    if ($missingFiles.Count -gt 0) {
        Write-Host "`nMissing files:" -ForegroundColor Red
        $missingFiles | ForEach-Object { Write-Host "  - $_" -ForegroundColor Red }
    }
    if ($missingDirs.Count -gt 0) {
        Write-Host "`nMissing directories:" -ForegroundColor Red
        $missingDirs | ForEach-Object { Write-Host "  - $_" -ForegroundColor Red }
    }
}

Write-Host "========================================`n" -ForegroundColor Cyan
