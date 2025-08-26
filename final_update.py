#!/usr/bin/env python3
"""
Final comprehensive update script for all HTML files
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Service-specific information
SERVICE_INFO = {
    'ductless-mini-split-installation.html': {
        'title': 'Ductless Mini Split Installation Belpre OH | Professional HVAC Installation',
        'description': 'Expert ductless mini split installation in Belpre, Ohio. Energy-efficient systems, professional technicians, same-day installation. Free estimates.',
        'keywords': 'ductless mini split installation Belpre OH, HVAC installation, mini split systems, energy efficient cooling heating'
    },
    'hvac-repair.html': {
        'title': 'HVAC Repair Services Belpre OH | 24/7 Emergency Heating & Cooling Repair',
        'description': 'Expert HVAC repair services in Belpre, Ohio. 24/7 emergency heating and cooling repair. Licensed technicians. Same-day service.',
        'keywords': 'HVAC repair Belpre OH, heating repair, air conditioning repair, furnace repair, emergency HVAC'
    },
    'air-conditioning-installation.html': {
        'title': 'Air Conditioning Installation Belpre OH | AC Installation Services',
        'description': 'Professional air conditioning installation in Belpre, Ohio. Energy-efficient AC systems, expert installation, free estimates.',
        'keywords': 'air conditioning installation Belpre OH, AC installation, cooling systems, central air'
    },
    'heating-installation.html': {
        'title': 'Heating Installation Belpre OH | Furnace & Heat Pump Installation',
        'description': 'Professional heating system installation in Belpre, Ohio. Furnaces, heat pumps, boilers. Expert installation, energy-efficient systems.',
        'keywords': 'heating installation Belpre OH, furnace installation, heat pump installation, boiler installation'
    },
    'emergency-hvac.html': {
        'title': '24/7 Emergency HVAC Services Belpre OH | Emergency Heating & Cooling Repair',
        'description': '24/7 emergency HVAC services in Belpre, Ohio. Emergency heating and cooling repair, same-day service, licensed technicians.',
        'keywords': 'emergency HVAC Belpre OH, 24/7 HVAC repair, emergency heating, emergency cooling'
    },
    'hvac-maintenance.html': {
        'title': 'HVAC Maintenance Services Belpre OH | Heating & Cooling Maintenance',
        'description': 'Professional HVAC maintenance services in Belpre, Ohio. Preventive maintenance, tune-ups, service contracts.',
        'keywords': 'HVAC maintenance Belpre OH, heating maintenance, cooling maintenance, HVAC tune-up'
    },
    'commercial-hvac.html': {
        'title': 'Commercial HVAC Services Belpre OH | Business Heating & Cooling',
        'description': 'Commercial HVAC services in Belpre, Ohio. Business heating and cooling installation, repair, maintenance.',
        'keywords': 'commercial HVAC Belpre OH, business HVAC, commercial heating cooling'
    },
    'ductwork-services.html': {
        'title': 'Ductwork Services Belpre OH | Duct Installation, Cleaning & Repair',
        'description': 'Professional ductwork services in Belpre, Ohio. Duct installation, cleaning, repair, and replacement.',
        'keywords': 'ductwork services Belpre OH, duct installation, duct cleaning, duct repair'
    },
    'indoor-air-quality.html': {
        'title': 'Indoor Air Quality Services Belpre OH | Air Purification & Filtration',
        'description': 'Indoor air quality services in Belpre, Ohio. Air purification, filtration systems, humidity control.',
        'keywords': 'indoor air quality Belpre OH, air purification, air filtration, humidity control'
    },
    'heat-pump-services.html': {
        'title': 'Heat Pump Services Belpre OH | Heat Pump Installation & Repair',
        'description': 'Heat pump services in Belpre, Ohio. Installation, repair, maintenance of heat pump systems.',
        'keywords': 'heat pump services Belpre OH, heat pump installation, heat pump repair'
    }
}

# Location-specific information
LOCATION_INFO = {
    'st-george.html': {
        'city': 'Belpre',
        'title': 'Belpre Ohio Ductless Mini Split Installation & HVAC Services',
        'description': 'Expert ductless mini split installation, HVAC repair, and air conditioning services in Belpre, Ohio. 24/7 emergency service.',
        'zip': '45714'
    },
    'stapleton.html': {
        'city': 'Marietta',
        'title': 'Marietta Ohio Ductless Mini Split Installation & HVAC Services',
        'description': 'Expert ductless mini split installation, HVAC repair, and air conditioning services in Marietta, Ohio. 24/7 emergency service.',
        'zip': '45750'
    },
    'port-richmond.html': {
        'city': 'Little Hocking',
        'title': 'Little Hocking Ohio HVAC Services | Ductless Mini Split Installation',
        'description': 'Expert HVAC services in Little Hocking, Ohio. Ductless mini split installation, heating and cooling repair.',
        'zip': '45742'
    },
    'tottenville.html': {
        'city': 'Vincent',
        'title': 'Vincent Ohio HVAC Services | Ductless Mini Split Installation',
        'description': 'Expert HVAC services in Vincent, Ohio. Ductless mini split installation, heating and cooling repair.',
        'zip': '45784'
    },
    'great-kills.html': {
        'city': 'Barlow',
        'title': 'Barlow Ohio HVAC Services | Ductless Mini Split Installation',
        'description': 'Expert HVAC services in Barlow, Ohio. Ductless mini split installation, heating and cooling repair.',
        'zip': '45712'
    },
    'new-dorp.html': {
        'city': 'Parkersburg, WV',
        'title': 'Parkersburg WV HVAC Services | Ductless Mini Split Installation',
        'description': 'Expert HVAC services in Parkersburg, West Virginia. Ductless mini split installation, heating and cooling repair.',
        'zip': '26101'
    },
    'west-brighton.html': {
        'city': 'Beverly',
        'title': 'Beverly Ohio HVAC Services | Ductless Mini Split Installation',
        'description': 'Expert HVAC services in Beverly, Ohio. Ductless mini split installation, heating and cooling repair.',
        'zip': '45715'
    },
    'castleton-corners.html': {
        'city': 'Williamstown, WV',
        'title': 'Williamstown WV HVAC Services | Ductless Mini Split Installation',
        'description': 'Expert HVAC services in Williamstown, West Virginia. Ductless mini split installation, heating and cooling repair.',
        'zip': '26187'
    }
}

def update_service_files():
    """Update service files with specific titles and descriptions"""
    services_dir = BASE_DIR / 'services'
    
    for filename, info in SERVICE_INFO.items():
        file_path = services_dir / filename
        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Update title
                content = re.sub(
                    r'<title>[^<]*</title>',
                    f'<title>{info["title"]}</title>',
                    content
                )
                
                # Update meta description
                content = re.sub(
                    r'<meta name="description" content="[^"]*"',
                    f'<meta name="description" content="{info["description"]}"',
                    content
                )
                
                # Update meta keywords
                content = re.sub(
                    r'<meta name="keywords" content="[^"]*"',
                    f'<meta name="keywords" content="{info["keywords"]}"',
                    content
                )
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"Updated service file: {filename}")
                
            except Exception as e:
                print(f"Error updating {filename}: {e}")

def update_location_files():
    """Update location files with specific city information"""
    locations_dir = BASE_DIR / 'locations'
    
    for filename, info in LOCATION_INFO.items():
        file_path = locations_dir / filename
        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Update title
                content = re.sub(
                    r'<title>[^<]*</title>',
                    f'<title>{info["title"]}</title>',
                    content
                )
                
                # Update meta description
                content = re.sub(
                    r'<meta name="description" content="[^"]*"',
                    f'<meta name="description" content="{info["description"]}"',
                    content
                )
                
                # Update emergency banner
                content = re.sub(
                    r'🚨 24/7 Emergency HVAC Services Available in [^-]* - Call Now!',
                    f'🚨 24/7 Emergency HVAC Services Available in {info["city"]} - Call Now!',
                    content
                )
                
                # Update hero title
                content = re.sub(
                    r'<h1>Professional <span class="hero-highlight">HVAC Services</span> in [^<]*</h1>',
                    f'<h1>Professional <span class="hero-highlight">HVAC Services</span> in {info["city"]}</h1>',
                    content
                )
                
                # Update hero description
                content = re.sub(
                    r'<p>Expert ductless mini split installation, HVAC repair, and air conditioning services for [^.]*\.',
                    f'<p>Expert ductless mini split installation, HVAC repair, and air conditioning services for {info["city"]} residents.',
                    content
                )
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"Updated location file: {filename} for {info['city']}")
                
            except Exception as e:
                print(f"Error updating {filename}: {e}")

def clean_up_remaining_references():
    """Clean up any remaining Staten Island references"""
    html_files = []
    
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Final cleanup of any remaining references
            content = content.replace('NY', 'OH')
            content = content.replace('New York', 'Ohio')
            content = content.replace('Harbor', 'River')
            content = content.replace(', OH, OH', ', OH')
            content = content.replace('Belpre, OH, NY', 'Belpre, OH')
            content = content.replace('Staten Island', 'Belpre')
            
            # Clean up any double references
            content = content.replace('Belpre, OH Ductless Mini Splits', 'Belpre OH Ductless Mini Splits')
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Cleaned up: {file_path}")
                
        except Exception as e:
            print(f"Error cleaning {file_path}: {e}")

def main():
    """Main function"""
    print("Starting final comprehensive updates...")
    update_service_files()
    update_location_files()
    clean_up_remaining_references()
    print("All updates completed!")

if __name__ == "__main__":
    main()
