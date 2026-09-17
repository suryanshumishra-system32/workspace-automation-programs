# Sorta (Project_Sorter) 

A command-line automation tool designed to streamline creative and developmental asset management.
The script scans the active folder for specific project keywords and dynamically bundles all matching files into dedicated folders.

## How to Run and Use

### Prerequisites
This script runs entirely on native Python 3 standard libraries. No external package installations are necessary.

### Step-by-Step Execution
1. Place the `_project_sorter.py` file into the main folder where your mixed project assets are located.
2. Run the script any way you like.
3. **Interactive Prompt:** The terminal will ask you to `enter project name`. Type your project keyword (e.g., `sunlight` or `japan`) and press Enter.
4. **Casing Safety:** The script handles input values seamlessly using case-insensitive checks. It will automatically create a folder with that name and safely pull in all files containing that keyword.
5. **Batch Processing:** To sort another project keyword without closing the program, type `1` when prompted. Press any other key to finish and exit the automation loop.
