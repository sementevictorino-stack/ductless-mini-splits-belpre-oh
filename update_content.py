#!/usr/bin/env python3
"""
Script to update all HTML files for Belpre, OH location
"""

import os
import re
from pathlib import Path

# Configuration
CATEGORY = "Ductless Mini Split"
CITY = "Belpre"
STATE = "OH"
FULL_LOCATION = "Belpre, OH"

# Base directory
BASE_DIR = Path(__file__).parent

def update_file_content(file_path):
    """Update content in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Update title tags
        content = re.sub(
            r'<title>([^<]*Staten Island[^<]*)</title>',
            f'<title>{FULL_LOCATION} Ductless Mini Splits | Professional HVAC Services</title>',
            content
        )
        
        # Update meta descriptions
        content = re.sub(
            r'<meta name="description" content="([^"]*Staten Island[^"]*)"',
            f'<meta name="description" content="Professional ductless mini split installation, repair, and maintenance in {FULL_LOCATION}. 24/7 emergency HVAC services. Expert technicians."',
            content
        )
        
        # Update meta keywords
        content = re.sub(
            r'<meta name="keywords" content="([^"]*Staten Island[^"]*)"',
            f'<meta name="keywords" content="ductless mini splits {FULL_LOCATION}, HVAC services, air conditioning repair, heating installation, emergency HVAC"',
            content
        )
        
        # Update business name references
        content = content.replace('Staten Island Ductless Mini Splits', f'{FULL_LOCATION} Ductless Mini Splits')
        content = content.replace('SI Ductless Pro', f'{CITY} Ductless Pro')
        
        # Update addresses
        content = re.sub(
            r'"streetAddress": "123 Victory Blvd"',
            '"streetAddress": "123 Main St"',
            content
        )
        content = re.sub(
            r'"addressLocality": "Staten Island"',
            f'"addressLocality": "{CITY}"',
            content
        )
        content = re.sub(
            r'"addressRegion": "NY"',
            f'"addressRegion": "{STATE}"',
            content
        )
        content = re.sub(
            r'"postalCode": "10301"',
            '"postalCode": "45714"',
            content
        )
        
        # Update coordinates
        content = re.sub(
            r'"latitude": 40\.6282',
            '"latitude": 39.2742',
            content
        )
        content = re.sub(
            r'"longitude": -74\.0776',
            '"longitude": -81.5734',
            content
        )
        
        # Update main headings
        content = re.sub(
            r'Staten Island\'s #1 <span class="hero-highlight">([^<]*)</span> Experts',
            f'{CITY}\'s #1 <span class="hero-highlight">\\1</span> Experts',
            content
        )
        
        # Update service area references
        content = content.replace('Staten Island', FULL_LOCATION)
        content = content.replace('New York Harbor', 'Ohio River')
        content = content.replace('St. George', CITY)
        content = content.replace('Tottenville', 'Marietta')
        content = content.replace('Great Kills', 'Little Hocking')
        content = content.replace('Port Richmond', 'Vincent')
        content = content.replace('New Brighton', 'Parkersburg, WV')
        
        # Update zip codes and locations in footer and content
        content = re.sub(
            r'\(10301\)',
            '(45714)',
            content
        )
        content = re.sub(
            r'\(10304\)',
            '(45750)',
            content
        )
        content = re.sub(
            r'\(10302\)',
            '(45742)',
            content
        )
        
        # Update email addresses
        content = content.replace('info@statenislandductless.com', 'info@belpreductless.com')
        
        # Update social media links
        content = content.replace('facebook.com/statenislandductless', 'facebook.com/belpreductless')
        content = content.replace('instagram.com/statenislandductless', 'instagram.com/belpreductless')
        
        # Update URLs
        content = content.replace('statenislandductless.com', 'belpreductless.com')
        
        # Update address in footer
        content = content.replace('123 Victory Blvd, Staten Island, NY 10301', f'123 Main St, {FULL_LOCATION} 45714')
        
        # Update copyright
        content = content.replace('Staten Island Ductless Mini Splits. All rights reserved.', f'{FULL_LOCATION} Ductless Mini Splits. All rights reserved.')
        
        # Update customer reviews
        content = content.replace('- Maria R., St. George', f'- Maria R., {CITY}')
        content = content.replace('- John D., Tottenville', '- John D., Marietta')
        content = content.replace('- Sarah L., Great Kills', '- Sarah L., Little Hocking')
        
        # Update emergency banner
        content = content.replace('Available in St. George', f'Available in {CITY}')
        
        # Update specific location references in content
        content = re.sub(
            r'serving all Staten Island zip codes',
            f'serving {FULL_LOCATION} and surrounding Washington County areas',
            content
        )
        
        # Update location-specific content
        content = re.sub(
            r'across all Staten Island zip codes including [^.]*\.',
            f'throughout the {FULL_LOCATION} area and surrounding Washington County communities.',
            content
        )
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {file_path}")
            return True
        else:
            print(f"No changes needed: {file_path}")
            return False
            
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False

def main():
    """Main function to update all HTML files"""
    html_files = []
    
    # Find all HTML files
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    print(f"Found {len(html_files)} HTML files to update")
    
    updated_count = 0
    for file_path in html_files:
        if update_file_content(file_path):
            updated_count += 1
    
    print(f"\nCompleted! Updated {updated_count} files out of {len(html_files)} total files.")

if __name__ == "__main__":
    main()
