#!/bin/bash
# PowerApps Canvas App Structure Validator
# Run this script to verify all required files are present

echo -e "\033[36mValidating Power Apps Canvas App Structure...\033[0m"

REQUIRED_FILES=(
    "CanvasManifest.json"
    "Header.json"
    "Entropy.json"
    "checksum.json"
    "Resources.json"
    "Connections.json"
    "ComponentReferences.json"
    "ControlTemplates.json"
)

REQUIRED_DIRS=(
    "Src"
    "Assets"
    "DataSources"
)

MISSING_FILES=()
MISSING_DIRS=()

# Check files
for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo -e "\033[32m✓ Found: $file\033[0m"
    else
        echo -e "\033[31m✗ Missing: $file\033[0m"
        MISSING_FILES+=("$file")
    fi
done

# Check directories
for dir in "${REQUIRED_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        echo -e "\033[32m✓ Found directory: $dir\033[0m"
    else
        echo -e "\033[31m✗ Missing directory: $dir\033[0m"
        MISSING_DIRS+=("$dir")
    fi
done

# Validate CanvasManifest.json
if [ -f "CanvasManifest.json" ]; then
    if python3 -m json.tool CanvasManifest.json > /dev/null 2>&1; then
        echo -e "\033[32m✓ CanvasManifest.json is valid JSON\033[0m"
        FORMAT_VERSION=$(python3 -c "import json; print(json.load(open('CanvasManifest.json'))['FormatVersion'])" 2>/dev/null)
        echo -e "\033[90m  FormatVersion: $FORMAT_VERSION\033[0m"
    else
        echo -e "\033[31m✗ CanvasManifest.json is not valid JSON\033[0m"
    fi
fi

# Check Src files
echo -e "\n\033[36mChecking Src directory...\033[0m"
SRC_FILES=(
    "Src/App.fx_1761820299719.yaml"
    "Src/App.pa_1761820299718.yaml"
    "Src/Screen1.fx.yaml"
    "Src/Screen1.pa.yaml"
    "Src/_EditorState.pa_1761820299719.yaml"
)

for file in "${SRC_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo -e "\033[32m✓ Found: $file\033[0m"
    else
        echo -e "\033[31m✗ Missing: $file\033[0m"
        MISSING_FILES+=("$file")
    fi
done

# Summary
echo -e "\n\033[36m========================================\033[0m"
if [ ${#MISSING_FILES[@]} -eq 0 ] && [ ${#MISSING_DIRS[@]} -eq 0 ]; then
    echo -e "\033[32m✓ All required files and directories are present!\033[0m"
    echo -e "\n\033[36mYou can now run:\033[0m"
    echo -e "\033[33m  pac canvas pack --sources . --msapp App.msapp\033[0m"
else
    echo -e "\033[31m✗ Structure validation failed!\033[0m"
    if [ ${#MISSING_FILES[@]} -gt 0 ]; then
        echo -e "\n\033[31mMissing files:\033[0m"
        for file in "${MISSING_FILES[@]}"; do
            echo -e "\033[31m  - $file\033[0m"
        done
    fi
    if [ ${#MISSING_DIRS[@]} -gt 0 ]; then
        echo -e "\n\033[31mMissing directories:\033[0m"
        for dir in "${MISSING_DIRS[@]}"; do
            echo -e "\033[31m  - $dir\033[0m"
        done
    fi
fi
echo -e "\033[36m========================================\033[0m\n"
