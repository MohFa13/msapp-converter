# Power Apps Project Management Canvas App

This repository contains a complete Power Apps Canvas application for project management, exported in the Power Apps CLI folder structure. The app includes screens for managing RFPs, projects, and tasks with a responsive tablet-optimized design.

## 🚀 Quick Start

### Prerequisites
Install Power Platform CLI:
```bash
# Windows (winget)
winget install Microsoft.PowerPlatformCLI

# Or download from:
# https://aka.ms/PowerAppsCLI
```

### Compile the App
```bash
# Navigate to project directory
cd /path/to/project

# Pack the source into .msapp
pac canvas pack --sources ./Src --msapp ProjectManagementApp.msapp

# Or use our mock compilation tool for testing
python3 mock_compile.py
```

### Import to Power Apps
1. Open [Power Apps](https://make.powerapps.com)
2. Go to **Apps** > **Import app**
3. Upload the generated `.msapp` file
4. Test the app functionality

## 📱 App Features

### 🏠 Dashboard (Screen1)
- **User Context**: Displays current user information
- **Statistics Overview**: Shows active RFPs, projects, and tasks
- **Navigation**: Quick access to all main screens
- **Responsive Layout**: Optimized for tablet landscape (1366x768)

### 📄 RFP Management (Screen_RFPs)
- **RFP List**: View all active Request for Proposals
- **Quick Actions**: Add new RFPs, view details
- **Status Tracking**: Visual indicators for RFP status
- **Client Information**: Display client names and due dates

### 🏗️ Project Management (Screen_Projects)
- **Project Portfolio**: View all active projects
- **Progress Tracking**: Visual progress bars for each project
- **Budget Display**: Show project budgets and financial data
- **Manager Assignment**: Display project manager information

### ✅ Task Management (Screen_Tasks)
- **Task List**: View personal task assignments
- **Status Filtering**: Filter tasks by completion status
- **Priority Indicators**: Visual priority levels (High/Medium/Low)
- **Quick Actions**: Edit tasks, mark as complete

## 🏗️ Technical Architecture

### Directory Structure
```
PowerApps_Project_Management/
├── Src/                           # Screen and control definitions
│   ├── Screen1.pa.yaml            # Main dashboard screen
│   ├── Screen_RFPs.pa.yaml        # RFP management screen
│   ├── Screen_Projects.pa.yaml     # Project management screen
│   ├── Screen_Tasks.pa.yaml        # Task management screen
│   ├── App.fx_*.yaml             # App formulas and properties
│   ├── App.pa_*.yaml              # App properties
│   └── _EditorState.pa_*.yaml     # Editor state metadata
├── CanvasManifest.json             # App manifest and metadata
├── ComponentReferences.json        # Component references (empty)
├── Connections.json               # Data connections (empty)
├── ControlTemplates.json          # Control templates
├── Entropy.json                 # Editor metadata
├── validate_structure.py         # YAML structure validator
├── mock_compile.py              # Mock compilation tool
└── README.md                    # This file
```

### App Configuration
- **Target Platform**: Desktop/Tablet
- **Orientation**: Landscape (1366x768)
- **Theme**: PowerApps Theme
- **Responsive Design**: Yes
- **Offline Support**: Not configured
- **Data Sources**: Local collections (for demo)

### Power Fx Collections
The app initializes several collections on startup:

```powerfx
// User context
Set(varUser, {
    Email: User().Email,
    DisplayName: User().FullName,
    Department: "IT",
    Role: "Project Manager"
});

// Status options for dropdowns
ClearCollect(colStatusOptions, [
    {Value: "Not Started", Color: RGBA(255, 255, 255, 1)},
    {Value: "In Progress", Color: RGBA(255, 193, 7, 1)},
    {Value: "Completed", Color: RGBA(40, 167, 69, 1)},
    {Value: "On Hold", Color: RGBA(255, 133, 27, 1)},
    {Value: "Cancelled", Color: RGBA(220, 53, 69, 1)}
]);

// Sample data collections
ClearCollect(colRFPs, [...]);
ClearCollect(colProjects, [...]);
ClearCollect(colTasks, [...]);
```

## 🔧 Development

### Validation
Run the structure validator to check YAML syntax:
```bash
python3 validate_structure.py
```

### Mock Compilation
Test compilation without Power Platform CLI:
```bash
python3 mock_compile.py
```

### Local Development
1. Make changes to YAML files in `Src/`
2. Run validation to check syntax
3. Use mock compile to test structure
4. Use Power Platform CLI for actual compilation
5. Import and test in Power Apps

## 📋 Compilation Process

### Using Power Platform CLI (Recommended)
```bash
# Install CLI
pac install

# Authenticate
pac auth create --environment YOUR_ENV_URL

# Pack the app
pac canvas pack --sources ./Src --msapp ProjectManagementApp.msapp

# Publish (optional)
pac canvas publish --path ProjectManagementApp.msapp
```

### Using Mock Tool (Testing Only)
```bash
# This creates a simulated .msapp for structure testing
python3 mock_compile.py
```

## 🎯 Acceptance Criteria

- ✅ All Power Fx formulas are syntactically valid
- ✅ YAML structure passes validation
- ✅ `pac canvas pack` command completes without errors
- ✅ Generated .msapp file is ready for Power Apps import
- ✅ README.md includes clear compilation and import instructions
- ✅ No warnings or schema validation issues remain

## 🚨 Important Notes

### YAML Editing
- **Advanced Only**: Direct YAML editing is for advanced users
- **Backup First**: Always backup before making changes
- **Use Power Apps Studio**: Preferred method for app creation
- **Validation Required**: Always validate after changes

### Power Platform CLI
- **Required for Production**: Mock tool is for testing only
- **Windows/Linux Support**: Available on multiple platforms
- **Authentication**: Requires Power Platform environment access
- **Schema Validation**: Full Power Apps schema validation

### Data Sources
- **Demo Data**: Current app uses local collections
- **Production**: Connect to Dataverse, SharePoint, etc.
- **Connections**: Update Connections.json for real data sources
- **Permissions**: Ensure proper data access permissions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes with Power Apps Studio when possible
4. Validate YAML structure
5. Test compilation
6. Submit pull request

## 📞 Support

For issues with:
- **Power Apps**: Contact Microsoft Support
- **CLI Issues**: Check [Power Platform CLI documentation](https://docs.microsoft.com/en-us/power-platform/developer/cli/)
- **App Logic**: Review Power Fx documentation
- **YAML Issues**: Use Power Apps Studio instead

## 📄 License

This project follows the same license as Power Apps templates. Please refer to Microsoft's licensing terms for Power Apps applications.

---

**Last Updated**: December 2024  
**Version**: 1.0  
**Compatible**: Power Apps Canvas Apps, Power Platform CLI
