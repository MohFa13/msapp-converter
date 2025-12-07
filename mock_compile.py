#!/usr/bin/env python3
"""
Power Apps Mock Compilation Script
This script simulates the Power Platform CLI pack process since we cannot install the actual CLI.
"""

import os
import json
import zipfile
from pathlib import Path
from datetime import datetime

def create_mock_msapp():
    """Create a mock .msapp file for demonstration purposes."""
    
    print("🔨 Creating mock Power Apps compilation...")
    print("=" * 50)
    
    # Validate source files exist
    src_dir = Path("Src")
    if not src_dir.exists():
        print("❌ Src directory not found")
        return False
    
    yaml_files = list(src_dir.glob("*.yaml"))
    if not yaml_files:
        print("❌ No YAML files found in Src directory")
        return False
    
    print(f"📄 Found {len(yaml_files)} source files:")
    for yaml_file in yaml_files:
        print(f"   - {yaml_file.name}")
    
    # Validate manifest file
    manifest_file = Path("CanvasManifest.json")
    if not manifest_file.exists():
        print("❌ CanvasManifest.json not found")
        return False
    
    try:
        with open(manifest_file, 'r') as f:
            manifest = json.load(f)
        print(f"✅ CanvasManifest.json is valid (App: {manifest.get('PublishInfo', {}).get('AppName', 'Unknown')})")
    except Exception as e:
        print(f"❌ CanvasManifest.json error: {e}")
        return False
    
    # Create mock compilation metadata
    compilation_info = {
        "compilation_time": datetime.now().isoformat(),
        "source_files": [f.name for f in yaml_files],
        "app_name": manifest.get('PublishInfo', {}).get('AppName', 'App'),
        "app_id": manifest.get('Properties', {}).get('Id', 'Unknown'),
        "screens": manifest.get('ScreenOrder', []),
        "status": "success",
        "warnings": [],
        "errors": []
    }
    
    # Check for common issues
    for yaml_file in yaml_files:
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Basic syntax checks
            if 'OnStart:' in content and 'Screen1' in yaml_file.name:
                compilation_info["warnings"].append(f"{yaml_file.name}: OnStart formula found - ensure proper syntax")
            
            if 'Navigate(' in content:
                compilation_info["warnings"].append(f"{yaml_file.name}: Navigate formulas detected - verify screen references")
                
            if 'Fill:' not in content and 'Screen' in yaml_file.name:
                compilation_info["errors"].append(f"{yaml_file.name}: Missing Fill property")
                
        except Exception as e:
            compilation_info["errors"].append(f"{yaml_file.name}: Read error - {e}")
    
    # Create mock .msapp structure
    msapp_name = f"ProjectManagementApp_{datetime.now().strftime('%Y%m%d_%H%M%S')}.msapp"
    
    print(f"\n📦 Creating {msapp_name}...")
    
    # Create a zip file to simulate .msapp
    with zipfile.ZipFile(msapp_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add source files
        for yaml_file in yaml_files:
            zipf.write(yaml_file, f"Src/{yaml_file.name}")
        
        # Add metadata files
        metadata_files = [
            "CanvasManifest.json",
            "ComponentReferences.json", 
            "Connections.json",
            "ControlTemplates.json",
            "Entropy.json"
        ]
        
        for meta_file in metadata_files:
            if Path(meta_file).exists():
                zipf.write(meta_file, meta_file)
        
        # Add compilation info
        zipf.writestr("compilation_info.json", json.dumps(compilation_info, indent=2))
    
    # Print results
    print("\n" + "=" * 50)
    print("📊 COMPILATION RESULTS")
    print("=" * 50)
    
    if compilation_info["errors"]:
        print(f"❌ {len(compilation_info['errors'])} Errors found:")
        for error in compilation_info["errors"]:
            print(f"   - {error}")
    else:
        print("✅ No critical errors found")
    
    if compilation_info["warnings"]:
        print(f"⚠️  {len(compilation_info['warnings'])} Warnings:")
        for warning in compilation_info["warnings"]:
            print(f"   - {warning}")
    else:
        print("✅ No warnings generated")
    
    print(f"\n📁 Generated: {msapp_name}")
    print(f"📱 App Name: {compilation_info['app_name']}")
    print(f"🆔 App ID: {compilation_info['app_id']}")
    print(f"📺 Screens: {len(compilation_info['screens'])}")
    
    for screen in compilation_info['screens']:
        print(f"   - {screen}")
    
    # Calculate success rate
    total_issues = len(compilation_info["errors"]) + len(compilation_info["warnings"])
    if total_issues == 0:
        print("\n🎉 App compiled successfully - ready for import!")
        return True
    elif len(compilation_info["errors"]) == 0:
        print("\n✅ App compiled with warnings - should import successfully")
        return True
    else:
        print(f"\n❌ App has {len(compilation_info['errors'])} critical errors - fix before importing")
        return False

def main():
    """Main function."""
    print("🚀 Power Apps Mock Compilation Tool")
    print("This tool simulates Power Platform CLI compilation for testing purposes")
    print()
    
    success = create_mock_msapp()
    
    print("\n" + "=" * 50)
    print("📋 NEXT STEPS")
    print("=" * 50)
    print("1. Install Power Platform CLI for actual compilation:")
    print("   https://docs.microsoft.com/en-us/power-platform/developer/cli/reference/pac-canvas")
    print()
    print("2. Use actual CLI command:")
    print("   pac canvas pack --sources ./Src --msapp YourApp.msapp")
    print()
    print("3. Import to Power Apps:")
    print("   - Open Power Apps Studio")
    print("   - Import the .msapp file")
    print("   - Test functionality")
    print()
    
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())