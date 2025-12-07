# RFP Management System - PowerApps Canvas App

This folder contains the unpacked PowerApps source files for the RFP Management System in the proper structure for Power Platform CLI.

## Overview

A Canvas app for managing RFPs (Requests for Proposals), Projects, and Tasks with a responsive navigation interface and seeded in-memory data collections.

## Directory Structure
```
PowerApps_CLI_Ready/
├── Src/                    # Screen and control definitions (.pa.yaml, .fx.yaml)
│   ├── App.fx.yaml         # App initialization and OnStart logic
│   ├── Screen1.fx.yaml     # RFPs screen
│   ├── ProjectsScreen.fx.yaml  # Projects screen
│   └── MyTasksScreen.fx.yaml   # My Tasks screen
├── CanvasManifest.json     # App manifest
├── Entropy.json            # Editor metadata
├── Connections.json        # Connection references
├── ComponentReferences.json # Component references
└── ControlTemplates.json   # Control templates
```

## Data Model

The app uses in-memory collections seeded on app startup via `App.OnStart`:

### Collections

#### colStatusOptions
Status lookup table for all entities:
- **ID** (Number): Unique identifier (1-5)
- **Status** (Text): Status label ("Not Started", "In Progress", "On Hold", "Completed", "Cancelled")
- **Color** (Color): RGBA color for visual representation

#### colRFPs
RFP (Request for Proposal) records:
- **ID** (Number): Unique identifier
- **Title** (Text): RFP title
- **Client** (Text): Client name
- **DueDate** (Date): Proposal due date
- **Budget** (Number): Estimated budget amount
- **StatusID** (Number): Foreign key to colStatusOptions
- **Priority** (Text): "High", "Medium", or "Low"
- **Description** (Text): Detailed RFP description

#### colProjects
Active project records:
- **ID** (Number): Unique identifier
- **Name** (Text): Project name
- **Client** (Text): Client name
- **StartDate** (Date): Project start date
- **EndDate** (Date): Project end date
- **StatusID** (Number): Foreign key to colStatusOptions
- **Budget** (Number): Project budget
- **Progress** (Number): Completion percentage (0-100)
- **Manager** (Text): Project manager name

#### colTasks
User task records:
- **ID** (Number): Unique identifier
- **Title** (Text): Task title
- **ProjectID** (Number): Foreign key to colProjects
- **AssignedTo** (Text): User email (defaults to current user)
- **DueDate** (Date): Task due date
- **StatusID** (Number): Foreign key to colStatusOptions
- **Priority** (Text): "High", "Medium", or "Low"
- **EstimatedHours** (Number): Estimated effort in hours

## Theme Tokens

The app defines consistent design tokens in `App.OnStart` for maintainable styling:

### Color Variables
- **varColorPrimary**: RGBA(0, 120, 212, 1) - Primary blue
- **varColorSecondary**: RGBA(0, 176, 240, 1) - Light blue
- **varColorAccent**: RGBA(16, 110, 190, 1) - Dark blue
- **varColorSuccess**: RGBA(16, 124, 16, 1) - Green
- **varColorWarning**: RGBA(255, 185, 0, 1) - Amber
- **varColorDanger**: RGBA(196, 49, 75, 1) - Red
- **varColorBackground**: RGBA(243, 242, 241, 1) - Light gray background
- **varColorSurface**: RGBA(255, 255, 255, 1) - White surface
- **varColorText**: RGBA(50, 49, 48, 1) - Primary text
- **varColorTextLight**: RGBA(96, 94, 92, 1) - Secondary text
- **varColorBorder**: RGBA(225, 223, 221, 1) - Border gray

### Typography Variables
- **varFontSizeSmall**: 12pt
- **varFontSizeMedium**: 14pt
- **varFontSizeLarge**: 18pt
- **varFontSizeXLarge**: 24pt
- **varFontFamily**: "Segoe UI"

### Spacing Variables
- **varSpacingSmall**: 8px
- **varSpacingMedium**: 16px
- **varSpacingLarge**: 24px

### Navigation Variables
- **varUser**: Current user object from `User()` function
- **varActiveSection**: Current active navigation section ("RFPs", "Projects", or "Tasks")

## App Architecture

### Screens
1. **Screen1 (RFPs)**: Default landing screen displaying RFP summary
2. **ProjectsScreen**: Projects overview and management
3. **MyTasksScreen**: User's assigned tasks filtered by email

### Navigation Pattern
Each screen includes:
- **HeaderContainer**: Horizontal auto-layout container with:
  - App title label
  - Three navigation buttons (RFPs, Projects, My Tasks)
  - User welcome label
- **BodyContainer**: Vertical auto-layout container for screen content

Navigation buttons:
- Update `varActiveSection` on click
- Call `Navigate()` to switch screens
- Highlight active section with primary color fill
- Show hover states for better UX

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
To package the source files into an importable .msapp file:

```bash
# Navigate to parent directory of the project folder
cd /path/to/parent

# Pack the source into .msapp
pac canvas pack --sources project-folder-name --msapp RFPManagementSystem.msapp
```

**Example:**
```bash
cd /home/engine
pac canvas pack --sources project --msapp RFPManagementSystem.msapp
```

### Unpack .msapp (for reference)
To unpack an existing .msapp back to source format:

```bash
pac canvas unpack --msapp RFPManagementSystem.msapp --sources RFPManagementSystem_Source
```

### Publish to Environment
To publish the app to a Power Platform environment:

```bash
# Authenticate to your environment
pac auth create --environment YOUR_ENV_URL

# Import the .msapp file
pac canvas import --environment YOUR_ENV_URL --path RFPManagementSystem.msapp

# Or publish an existing app
pac canvas publish --path RFPManagementSystem.msapp
```

## Development Workflow

### Making Changes
1. Edit the YAML files in `Src/` directory
2. Update collection schemas in `App.fx.yaml` if adding new data fields
3. Maintain consistent theme variable usage across all screens
4. Test navigation flows between screens

### Packing and Testing
1. Pack to .msapp: `pac canvas pack --sources . --msapp test.msapp`
2. Import to Power Apps Studio for visual testing
3. Verify OnStart executes and collections are populated
4. Test navigation between all three screens
5. Confirm theme variables are applied consistently

## Important Notes

- **Data Persistence**: Collections are in-memory only and reset on app restart
- **User Context**: `varUser` captures current user info on startup
- **Navigation**: Screens use `varActiveSection` to highlight active tab
- **Theme Consistency**: Always use theme variables (varColor*, varFontSize*, varSpacing*) for styling
- **YAML Editing**: Manual YAML editing is advanced - validate syntax carefully
- **Backup**: Always keep a working .msapp backup before making manual edits
- **Testing**: Thoroughly test after packing custom edits, especially formulas

## Extending the App

### Adding New Screens
1. Create new `.fx.yaml` file in `Src/` directory
2. Copy navigation structure from existing screen
3. Update `CanvasManifest.json` ScreenOrder array
4. Update `Entropy.json` with new control IDs
5. Update `_EditorState.pa_1761820299719.yaml` ScreensOrder
6. Add navigation button in HeaderContainer of all screens

### Adding Collection Fields
1. Update `ClearCollect()` in `App.OnStart` with new fields
2. Update README.md data model documentation
3. Use new fields in screen formulas and galleries

### Modifying Theme
1. Edit color/font/spacing variables in `App.OnStart`
2. Variables automatically apply across all screens
3. Document any new variables in README.md
