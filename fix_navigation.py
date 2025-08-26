#!/usr/bin/env python3
"""
Script to fix remaining location references in HTML files
"""

import os
import re
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent

# Location mappings for navigation menus and links
LOCATION_MAPPINGS = {
    'st-george.html': ('Belpre', '45714'),
    'stapleton.html': ('Marietta', '45750'),
    'port-richmond.html': ('Little Hocking', '45742'),
    'tottenville.html': ('Vincent', '45784'),
    'great-kills.html': ('Barlow', '45712'),
    'new-dorp.html': ('Parkersburg, WV', '26101'),
    'west-brighton.html': ('Beverly', '45715'),
    'castleton-corners.html': ('Williamstown, WV', '26187'),
    'new-brighton.html': ('Parkersburg, WV', '26101'),
    'south-beach.html': ('Williamstown, WV', '26187'),
    'willowbrook.html': ('Athens', '45701'),
    'clifton.html': ('Vincent', '45784'),
    'charleston.html': ('Charleston, WV', '25301'),
    'dongan-hills.html': ('Beverly', '45715'),
    'eltingville.html': ('Little Hocking', '45742'),
    'grant-city.html': ('Barlow', '45712'),
    'mariners-harbor.html': ('Marietta', '45750'),
    'oakwood.html': ('Athens', '45701'),
    'pleasant-plains.html': ('Beverly', '45715'),
    'richmond-valley.html': ('Vincent', '45784'),
    'bay-terrace.html': ('Parkersburg, WV', '26101')
}

def update_navigation_menus():
    """Update navigation menus in all HTML files"""
    html_files = []
    
    # Find all HTML files
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    print(f"Updating navigation menus in {len(html_files)} files...")
    
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Update location dropdown menus
            locations_dropdown = '''                    <div class="dropdown-content">
                        <a href="st-george.html">Belpre</a>
                        <a href="stapleton.html">Marietta</a>
                        <a href="port-richmond.html">Little Hocking</a>
                        <a href="tottenville.html">Vincent</a>
                        <a href="great-kills.html">Barlow</a>
                        <a href="new-dorp.html">Parkersburg, WV</a>
                        <a href="west-brighton.html">Beverly</a>
                        <a href="castleton-corners.html">Williamstown, WV</a>
                    </div>'''
            
            # Replace location dropdown content
            content = re.sub(
                r'<div class="dropdown-content">\s*<a href="[^"]*">[^<]*</a>\s*<a href="[^"]*">[^<]*</a>\s*<a href="[^"]*">[^<]*</a>\s*<a href="[^"]*">[^<]*</a>\s*<a href="[^"]*">[^<]*</a>\s*<a href="[^"]*">[^<]*</a>\s*<a href="[^"]*">[^<]*</a>\s*<a href="[^"]*">[^<]*</a>\s*</div>',
                locations_dropdown,
                content,
                flags=re.DOTALL
            )
            
            # Remove old Staten Island location references
            content = re.sub(r'<a href="[^"]*bayonne-nj\.html">[^<]*</a>\s*', '', content)
            content = re.sub(r'<a href="[^"]*jersey-city-nj\.html">[^<]*</a>\s*', '', content)
            content = re.sub(r'<a href="[^"]*hoboken-nj\.html">[^<]*</a>\s*', '', content)
            content = re.sub(r'<a href="[^"]*brooklyn-ny\.html">[^<]*</a>\s*', '', content)
            content = re.sub(r'<a href="[^"]*manhattan-ny\.html">[^<]*</a>\s*', '', content)
            content = re.sub(r'<a href="[^"]*newark-nj\.html">[^<]*</a>\s*', '', content)
            content = re.sub(r'<a href="[^"]*elizabeth-nj\.html">[^<]*</a>\s*', '', content)
            content = re.sub(r'<a href="[^"]*perth-amboy-nj\.html">[^<]*</a>\s*', '', content)
            content = re.sub(r'<a href="[^"]*union-city-nj\.html">[^<]*</a>\s*', '', content)
            content = re.sub(r'<a href="[^"]*weehawken-nj\.html">[^<]*</a>\s*', '', content)
            content = re.sub(r'<a href="[^"]*rosebank\.html">[^<]*</a>\s*', '', content)
            
            # Update specific content sections
            content = content.replace('Mid-Island:', 'Central Ohio:')
            content = content.replace('North Shore:', 'Washington County:')
            content = content.replace('South Shore:', 'Southern Ohio:')
            content = content.replace('East Shore:', 'West Virginia Border:')
            
            # Update zip code references
            for old_zip, new_info in [
                ('10305', '45714'),
                ('10306', '45750'),
                ('10307', '45784'),
                ('10308', '45712'),
                ('10309', '45715'),
                ('10310', '26101'),
                ('10311', '45742'),
                ('10312', '26187'),
                ('10313', '45701'),
                ('10314', '25301')
            ]:
                content = content.replace(f'({old_zip})', f'({new_info})')
            
            # Update hero content for location-specific pages
            if 'locations/' in file_path:
                filename = os.path.basename(file_path)
                if filename in LOCATION_MAPPINGS:
                    city_name, zip_code = LOCATION_MAPPINGS[filename]
                    
                    # Update hero title
                    content = re.sub(
                        r'<h1>Professional <span class="hero-highlight">HVAC Services</span> in [^<]*</h1>',
                        f'<h1>Professional <span class="hero-highlight">HVAC Services</span> in {city_name}, Ohio</h1>',
                        content
                    )
                    
                    # Update hero description
                    content = re.sub(
                        r'<p>Expert ductless mini split installation, HVAC repair, and air conditioning services for [^.]*\. Local technicians with 24/7 emergency service\.</p>',
                        f'<p>Expert ductless mini split installation, HVAC repair, and air conditioning services for {city_name} residents. Local technicians with 24/7 emergency service.</p>',
                        content
                    )
            
            # Only write if content changed
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated navigation in: {file_path}")
            
        except Exception as e:
            print(f"Error updating {file_path}: {e}")

def main():
    """Main function"""
    update_navigation_menus()
    print("Navigation menu updates completed!")

if __name__ == "__main__":
    main()
