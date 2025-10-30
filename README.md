# PowerApps CLI Package

This folder contains your unpacked PowerApps source files in the proper structure for Power Platform CLI.

## Directory Structure
```
PowerApps_CLI_Ready/
├── Src/                    # Screen and control definitions (.pa.yaml, .fx.yaml)
├── DataSources/            # Dataverse connections and data sources
├── CanvasManifest.json     # App manifest
├── Entropy.json            # Editor metadata
├── checksum.json           # File checksums
├── Connections.json        # Connection references
└── Other metadata files
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
# Navigate to parent directory
cd /path/to/

# Pack the source into .msapp
pac canvas pack --sources PowerApps_CLI_Ready --msapp MyApp.msapp
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

## Reference

For the web application implementation details, see `POWERAPPS_GUIDE.md` in the project root.
