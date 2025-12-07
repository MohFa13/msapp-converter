#!/usr/bin/env python3
"""
Power Apps YAML Structure Validator
This script validates the basic structure and syntax of Power Apps YAML files.
"""

import yaml
import json
import os
import sys
from pathlib import Path

def load_yaml_file(file_path):
    """Load and parse a YAML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Remove Power Apps warning comments for parsing
            lines = content.split('\n')
            filtered_lines = []
            skip_warning = False
            for line in lines:
                if line.strip().startswith('# ************************************************************************************************'):
                    skip_warning = True
                    continue
                elif skip_warning and line.strip().startswith('# ') and 'Power Apps' in line:
                    continue
                elif skip_warning and line.strip() == '':
                    continue
                elif skip_warning and not line.strip().startswith('#'):
                    skip_warning = False
                    filtered_lines.append(line)
                else:
                    filtered_lines.append(line)
            
            filtered_content = '\n'.join(filtered_lines)
            return yaml.safe_load(filtered_content)
    except yaml.YAMLError as e:
        print(f"❌ YAML Syntax Error in {file_path}: {e}")
        return None
    except Exception as e:
        print(f"❌ Error loading {file_path}: {e}")
        return None

def validate_screen_structure(screen_data, screen_name):
    """Validate the structure of a screen."""
    errors = []
    warnings = []
    
    if not isinstance(screen_data, dict):
        errors.append(f"Screen {screen_name} should be a dictionary")
        return errors, warnings
    
    # Check for required properties
    required_props = ['Fill']
    for prop in required_props:
        if prop not in screen_data:
            # Check if this is the main App.fx file or if Fill is in nested structure
            if screen_name == "App.fx" and 'App' in screen_data:
                app_data = screen_data['App']
                if isinstance(app_data, dict) and 'Fill' in app_data:
                    continue
            errors.append(f"Screen {screen_name} missing required property: {prop}")
    
    # Check for common control types
    controls_found = []
    for key, value in screen_data.items():
        if isinstance(value, dict):
            if 'As' in value:
                control_type = value.get('As', '').split('.')[0] if '.' in str(value.get('As', '')) else str(value.get('As', ''))
                controls_found.append((key, control_type))
                
                # Validate common control properties
                if 'X' not in value and 'Width' not in value and key not in ['App', 'Host']:
                    warnings.append(f"Control {key} in {screen_name} might be missing positioning properties")
            elif key == 'App' and isinstance(value, dict):
                # Check for host control in App structure
                for sub_key, sub_value in value.items():
                    if isinstance(sub_value, dict) and 'As' in sub_value:
                        control_type = sub_value.get('As', '').split('.')[0] if '.' in str(sub_value.get('As', '')) else str(sub_value.get('As', ''))
                        controls_found.append((sub_key, control_type))
    
    print(f"📱 Screen {screen_name}: {len(controls_found)} controls found")
    for control_name, control_type in controls_found:
        print(f"   - {control_name} ({control_type})")
    
    return errors, warnings

def validate_app_structure(app_data):
    """Validate the app structure."""
    errors = []
    warnings = []
    
    if not isinstance(app_data, dict):
        errors.append("App data should be a dictionary")
        return errors, warnings
    
    # Check for app properties
    if 'Properties' in app_data:
        props = app_data['Properties']
        if 'Theme' not in props:
            warnings.append("App missing Theme property")
    
    return errors, warnings

def validate_json_file(file_path):
    """Validate a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"❌ JSON Syntax Error in {file_path}: {e}")
        return None
    except Exception as e:
        print(f"❌ Error loading {file_path}: {e}")
        return None

def main():
    """Main validation function."""
    print("🔍 Power Apps YAML Structure Validator")
    print("=" * 50)
    
    src_dir = Path("Src")
    if not src_dir.exists():
        print("❌ Src directory not found")
        return False
    
    total_errors = 0
    total_warnings = 0
    
    # Validate YAML files
    print("\n📄 Validating YAML files...")
    yaml_files = list(src_dir.glob("*.yaml"))
    
    for yaml_file in yaml_files:
        print(f"\n📋 Validating {yaml_file.name}...")
        data = load_yaml_file(yaml_file)
        
        if data is None:
            total_errors += 1
            continue
        
        # Validate based on file type
        if yaml_file.name.startswith("Screen"):
            errors, warnings = validate_screen_structure(data, yaml_file.stem)
        elif yaml_file.name.startswith("App.fx"):
            errors, warnings = validate_screen_structure(data, "App.fx")
        elif yaml_file.name.startswith("App.pa"):
            errors, warnings = validate_app_structure(data)
        else:
            errors, warnings = [], []
        
        total_errors += len(errors)
        total_warnings += len(warnings)
        
        for error in errors:
            print(f"   ❌ {error}")
        for warning in warnings:
            print(f"   ⚠️  {warning}")
        
        if not errors and not warnings:
            print(f"   ✅ {yaml_file.name} looks good!")
    
    # Validate JSON files
    print("\n📄 Validating JSON files...")
    json_files = ["CanvasManifest.json", "ComponentReferences.json", "Connections.json", "ControlTemplates.json", "Entropy.json"]
    
    for json_file in json_files:
        if Path(json_file).exists():
            print(f"\n📋 Validating {json_file}...")
            data = validate_json_file(json_file)
            if data is not None:
                print(f"   ✅ {json_file} is valid JSON")
            else:
                total_errors += 1
        else:
            print(f"   ⚠️  {json_file} not found (this might be expected)")
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 VALIDATION SUMMARY")
    print("=" * 50)
    print(f"Total Errors: {total_errors}")
    print(f"Total Warnings: {total_warnings}")
    
    if total_errors == 0:
        print("\n🎉 All files passed basic validation!")
        print("✅ The app structure appears to be ready for compilation")
        return True
    else:
        print(f"\n❌ Found {total_errors} errors that need to be fixed")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)