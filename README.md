# PowerApps CLI Package

This folder contains your unpacked PowerApps source files in the proper structure for Power Platform CLI.

## Directory Structure
```
project/
├── Src/                    # Screen and control definitions (.pa.yaml, .fx.yaml)
│   ├── App.fx_*.yaml       # App-level PowerFx formulas
│   ├── App.pa_*.yaml       # App properties
│   ├── Screen1.fx.yaml     # Screen1 PowerFx formulas
│   ├── Screen1.pa.yaml     # Screen1 properties
│   └── _EditorState.pa_*.yaml # Editor state metadata
├── DataSources/            # Dataverse connections and data sources
├── Assets/                 # Static assets and resources
├── CanvasManifest.json     # App manifest with screen order
├── Header.json             # App header metadata (required)
├── Entropy.json            # Editor metadata and control IDs
├── checksum.json           # File checksums (required)
├── Resources.json          # Resource definitions (required)
├── Connections.json        # Connection references
├── ComponentReferences.json # Component references
├── ControlTemplates.json   # Control template definitions
└── .gitignore              # Git ignore rules (updated to track required files)
```

## How to Use

### Prerequisites
Install Power Platform CLI:
```bash
# Windows (winget)
winget install Microsoft.PowerPlatformCLI

# Or download from:
# https://aka.ms/PowerAppsCLI
```

### Pack to .msapp
```bash
# Navigate to the project directory
cd /path/to/project

# Pack the source into .msapp
pac canvas pack --sources . --msapp MyApp.msapp
```

### Verified Packaging Command
The following command has been verified to work with this repository structure:
```bash
pac canvas pack --sources . --msapp App.msapp
```

### Unpack .msapp (for reference)
```bash
pac canvas unpack --msapp MyApp.msapp --sources PowerApps_Source_New
```

### Publish to Environment
```bash
# Authenticate
pac auth create --environment YOUR_ENV_URL

# Publish
pac canvas publish --path MyApp.msapp
```

## Next Steps

1. Extract this archive on your local machine
2. Make any edits to YAML files as needed
3. Use `pac canvas pack` to create .msapp
4. Import .msapp to PowerApps or publish via CLI

## Important Notes

- YAML files in `Src/` contain screen definitions and PowerFx formulas
- Editing YAML directly is advanced - use PowerApps Studio when possible
- Always backup your .msapp before making manual edits
- Test thoroughly after packing custom edits

## Required File Structure

This repository now includes all required files for Power Platform CLI packaging:
- `Header.json` - App header metadata (previously ignored by .gitignore)
- `checksum.json` - File integrity checksums (previously ignored by .gitignore)
- `Resources.json` - Resource definitions
- `Screen1.fx.yaml` and `Screen1.pa.yaml` - Screen definitions matching CanvasManifest.json
- `Assets/` and `DataSources/` directories with placeholder files

The `.gitignore` has been updated to allow tracking of required metadata files while still excluding temporary build artifacts.

## Reference

For the web application implementation details, see `POWERAPPS_GUIDE.md` in the project root.
