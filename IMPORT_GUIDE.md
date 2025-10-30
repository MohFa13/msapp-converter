# Import Guide

This guide explains how to import the Canvas App Template into your Power Platform environment.

## Method 1: Import Package (Recommended)

**Best for**: Quick deployment, direct app import with metadata

### Steps:

1. **Download the Package**
   - File: `CanvasAppTemplate_1_0_0_0.zip` (7.1 KB)

2. **Navigate to Power Apps**
   - Go to [https://make.powerapps.com](https://make.powerapps.com)
   - Select your target environment from the environment picker (top right)

3. **Import Package**
   - Click **Apps** in the left navigation menu
   - Click **Import canvas app** at the top
   - OR go to the Home page and click **Import** > **Import package**

4. **Upload Package**
   - Click **Upload** or **Browse**
   - Select `CanvasAppTemplate_1_0_0_0.zip`
   - Click **Upload**

5. **Review and Import**
   - Review the package information:
     - **Name**: App
     - **Package Version**: 1.0.0.0
   - Click **Import**
   - Wait for the import to complete (usually takes 10-30 seconds)

6. **Verify**
   - Once imported, the app should appear in your Apps list
   - Click on it to open and edit in Power Apps Studio

### Benefits:
- ✅ Includes package manifest for proper import
- ✅ Simple and quick deployment
- ✅ Works across environments
- ✅ Preserves app metadata

## Method 2: Import Canvas App Directly

**Best for**: Quick testing, development, proof-of-concept

### Steps:

1. **Download the Package**
   - File: `App.msapp` (7.6 KB)

2. **Navigate to Power Apps**
   - Go to [https://make.powerapps.com](https://make.powerapps.com)
   - Select your target environment

3. **Import Canvas App**
   - Click **Apps** in the left navigation
   - Click **Import canvas app** at the top
   - Click **Upload** and select `App.msapp`

4. **Complete Import**
   - Click **Import**
   - Wait for the upload and import to complete

5. **Verify**
   - The app will appear in your Apps list
   - Click on it to open and edit

### Benefits:
- ✅ Faster import process
- ✅ No solution overhead
- ✅ Good for quick testing
- ✅ Simpler for development scenarios

## What's Included?

This Canvas App Template includes:

- **Single Screen**: Screen1 with header, main content, and footer containers
- **Navigation**: Back button functionality enabled
- **Layout**: Tablet-optimized (1366x768) landscape orientation
- **Theme**: Default Power Apps theme
- **Controls**: Basic container controls (groupContainer.horizontal/vertical)

## Post-Import Steps

After importing, you may want to:

1. **Rename the App**
   - Open the app in Power Apps Studio
   - Click on **Settings** > **General settings**
   - Update the app name and description

2. **Configure Connections** (if needed)
   - Add data sources via **Data** panel
   - Configure connectors via **Data** > **Add data**

3. **Customize**
   - Add more screens
   - Customize the layout and controls
   - Add business logic with Power Fx formulas

4. **Share**
   - Click **Share** to grant access to other users
   - Set appropriate permissions

## Troubleshooting

### Import fails with "Invalid package" or "Manifest file not found"
- Ensure you downloaded the complete file (check file size: 7.1 KB for .zip or 7.6 KB for .msapp)
- Make sure you're using the "Import canvas app" or "Import package" option (not "Import solution")
- Try re-downloading the package
- Check that you have proper permissions in the target environment

### Can't find the app after import
- Check that you're in the correct environment
- Refresh your browser
- Clear browser cache and reload

### App won't open
- Ensure you have appropriate Power Apps license
- Check that canvas apps are enabled in your environment
- Contact your administrator if issues persist

## Need Help?

- **Power Apps Documentation**: [https://docs.microsoft.com/powerapps](https://docs.microsoft.com/powerapps)
- **Power Apps Community**: [https://powerusers.microsoft.com](https://powerusers.microsoft.com)
- **Support**: Contact your organization's Power Platform administrator

## Version Information

- **Solution Version**: 1.0.0.0
- **Solution Name**: CanvasAppTemplate
- **Publisher**: Default Publisher
- **Canvas App**: App (new_canvasapp_6fb7a)
- **Format Version**: 0.24
- **Min Client Version**: 1.331
- **Doc Version**: 1.346
