# Package Summary

This repository provides a Power Apps Canvas App Template in multiple formats for easy import and development.

## Available Packages

### 1. Import Package (App-level, production-ready)
**File**: `CanvasAppTemplate_1_0_0_0.zip` (7.1 KB)

This is a Power Platform import package that includes:
- Package manifest with app metadata
- Canvas app ready for deployment
- Simple import process

**Import via**: Power Apps Portal → Apps → Import canvas app OR Import → Import package

### 2. Unmanaged Solution Package (Experimental)
**File**: `CanvasAppTemplateSolution_1_0_0_0.zip` (8.8 KB)

⚠️ **Note**: May not work in all environments. Use Package #1 or #3 if import fails.

Standard unmanaged solution containing the canvas app as a root component.

**Import via**: Power Apps Portal → Solutions → Import solution

**Known Limitation**: Some Power Platform environments do not support importing standalone canvas apps via unmanaged solutions. If you see "Cannot add a Root Component" errors, use Package #1 or #3 instead.

### 3. Canvas App Package (Quick Import)
**File**: `App.msapp` (7.6 KB)

Standalone canvas app package for quick testing and development.

**Import via**: Power Apps Portal → Apps → Import canvas app

### 4. Source Files (Development)
The complete unpacked source structure including:
- YAML screen definitions (`Src/`)
- Metadata files (`CanvasManifest.json`, `Header.json`, etc.)
- Assets and DataSources folders
- Validation scripts

**Use with**: `pac canvas pack` command

## Package Comparison

| Feature | Import Package (.zip) | Unmanaged Solution (.zip) | Canvas App (.msapp) | Source Files |
|---------|----------------------|---------------------------|---------------------|--------------|
| File Size | 7.1 KB | 8.8 KB | 7.6 KB | ~15 KB |
| Import Method | Apps → Import canvas app | Solutions → Import solution | Apps → Import canvas app | `pac canvas pack` |
| Includes Manifest/Metadata | ✅ Yes (`manifest.xml`) | ✅ Yes (`solution.xml`, `customizations.xml`) | ⚠️ Basic | ✅ Full |
| Canvas App Root Component | ✅ App-level | ✅ Solution component (type 300) | ✅ Standalone | ✅ Generated when packed |
| ALM / Pipelines | ⚠️ Limited | ✅ Full | ❌ Manual | ✅ Full |
| Dependencies Included | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes |
| Best For | Production deployments | Enterprise ALM | Quick tests | Development customization |

## What's Included in the App?

### App Configuration
- **Name**: App
- **Type**: Canvas App
- **Form Factor**: Tablet (1366x768)
- **Orientation**: Landscape
- **Theme**: Power Apps Default Theme

### Screens
- **Screen1**: Main screen with container layout
  - HeaderContainer1: Top navigation area with back button
  - MainContainer1: Main content area
  - FooterContainer1: Bottom section

### Controls
- Back button with navigation functionality
- Responsive container controls (horizontal/vertical)
- White background with standard layout

### Features Enabled
- Back button navigation
- OnStart event support
- Power Fx formulas
- Component support (framework ready)

## File Structure

```
Repository Root
├── App.msapp                           # Standalone canvas app package
├── CanvasAppTemplate_1_0_0_0.zip       # Import package
├── IMPORT_GUIDE.md                     # Detailed import instructions
├── README.md                           # Main documentation
├── PACKAGE_SUMMARY.md                  # This file
├── validate-structure.ps1              # Windows validation script
├── validate-structure.sh               # Linux/Mac validation script
│
├── Source Files (for pac canvas pack)
│   ├── CanvasManifest.json             # App manifest
│   ├── Header.json                     # App metadata
│   ├── Entropy.json                    # Editor state
│   ├── checksum.json                   # File checksums
│   ├── Resources.json                  # Resource definitions
│   ├── Connections.json                # Connection references
│   ├── ComponentReferences.json        # Component references
│   ├── ControlTemplates.json           # Control templates
│   ├── Src/                            # Screen YAML files
│   │   ├── App.fx_*.yaml
│   │   ├── App.pa_*.yaml
│   │   ├── Screen1.fx.yaml
│   │   ├── Screen1.pa.yaml
│   │   └── _EditorState.pa_*.yaml
│   ├── Assets/                         # Static assets
│   └── DataSources/                    # Data source definitions
│
├── solution-package/                   # Unmanaged solution source
│   ├── [Content_Types].xml
│   ├── customizations.xml
│   ├── solution.xml
│   └── CanvasApps/
│       ├── new_canvasapp_6fb7a.msapp
│       └── new_canvasapp_6fb7a.meta.xml
└── package/                            # Import package source
    ├── manifest.xml                    # Package manifest
    └── App.msapp                       # Canvas app
```

## Quick Start

### For End Users (Just want to use the app)
1. Decide which package you need:
   - `CanvasAppTemplateSolution_1_0_0_0.zip` for solution-aware import (recommended for ALM)
   - `CanvasAppTemplate_1_0_0_0.zip` for direct app import
2. Import the package in Power Apps using the appropriate menu (Solutions → Import solution or Apps → Import canvas app)
3. Open and customize the app once the import completes

### For Developers (Want to modify and rebuild)
1. Clone the repository
2. Modify the YAML files in `Src/`
3. Run validation: `./validate-structure.sh` or `.\validate-structure.ps1`
4. Pack: `pac canvas pack --sources . --msapp MyApp.msapp`
5. Import the generated .msapp file

## Technical Details

### Versions
- **Solution Version**: 1.0.0.0
- **Format Version**: 0.24
- **Doc Version**: 1.346
- **Min Version to Load**: 1.331
- **MSApp Structure Version**: 2.4.0

### Compatibility
- Power Apps Studio: 3.24052.0 or later
- Power Platform CLI: 1.50.1 or later
- Minimum Client Version: 1.331

## Support & Resources

- **Import Guide**: See [IMPORT_GUIDE.md](IMPORT_GUIDE.md)
- **Development Guide**: See [README.md](README.md)
- **Power Apps Docs**: https://docs.microsoft.com/powerapps
- **CLI Reference**: https://aka.ms/PowerAppsCLI

## License

This template is provided as-is for use in Power Apps development.
