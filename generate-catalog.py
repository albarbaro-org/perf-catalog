#!/usr/bin/env python3
"""
Generate Backstage catalog from template by string replacement.
"""

import os

SYSTEMS_PER_FILE = 100
TOTAL_FILES = 56  # 56 files × 100 systems × 9 entities = 50,400 entities
OUTPUT_DIR = "/Users/abarbaro/code/perf-catalog"
TEMPLATE_FILE = os.path.join(OUTPUT_DIR, "system-template-test-0.yaml")

def read_template():
    """Read the template file"""
    with open(TEMPLATE_FILE, 'r') as f:
        return f.read()

def replace_indices(template, system_idx):
    """Replace all -0 and group-0 with the new index"""
    group_idx = system_idx % 100
    
    # Simple string replacement
    result = template.replace('-0', f'-{system_idx}')
    result = result.replace(' 0', f' {system_idx}')
    result = result.replace(f'group-{system_idx}', f'group-{group_idx}')
    
    return result

def main():
    print("🚀 Generating Backstage catalog from template...")
    print(f"📋 Template: {TEMPLATE_FILE}")
    print()
    
    # Read template
    template = read_template()
    print(f"✅ Template loaded ({len(template)} bytes)")
    print()
    
    # Generate files
    print(f"📊 Generating {TOTAL_FILES} files × {SYSTEMS_PER_FILE} systems...")
    print()
    
    for file_idx in range(TOTAL_FILES):
        start_system = file_idx * SYSTEMS_PER_FILE
        end_system = start_system + SYSTEMS_PER_FILE - 1

        filename = f"bulk-test-systems-{file_idx:03d}.yaml"
        filepath = os.path.join(OUTPUT_DIR, filename)

        print(f"📝 {filename} (systems {start_system}-{end_system})...", end=" ")

        with open(filepath, 'w') as f:
            f.write(f"# Backstage Catalog - Performance Testing\n")
            f.write(f"# File {file_idx + 1}/{TOTAL_FILES}: Systems {start_system}-{end_system}\n")
            f.write(f"# Generated from template: {TEMPLATE_FILE}\n")

            for system_idx in range(start_system, end_system + 1):
                system_yaml = replace_indices(template, system_idx)
                f.write(system_yaml)

        file_size = os.path.getsize(filepath) / 1024 / 1024
        print(f"✅ {file_size:.2f} MB")

    print()
    print("✨ Generation complete!")
    print(f"📂 Location: {OUTPUT_DIR}")
    print(f"📈 Total: {TOTAL_FILES * SYSTEMS_PER_FILE * 9:,} entities")


if __name__ == "__main__":
    main()
