# Sorta (Project_Sorter) 

A command-line automation tool designed to streamline creative and developmental asset management.
The script scans the active folder for specific project keywords and dynamically bundles all matching files into dedicated folders.

## Implementation and logic
1. **Targeting** : reads all files in the directory using `os.listdir()` function.
2. **Inputting** : takes input from the user for the project name. 
3. **Creation** : creates a folder named exactly what the user inputted in the same directory the
   program is present in.
4. **Exclusion** : excludes folders (using `os.path.isdir()`) and the program file itself from the process of moving.
5. **Comparison** : compares a lowered form of the name of the files in the directory and a lowered form of the project name the user inputted (to make the process case insensitive).
6. **Moving** : moves the file to its respective folder using `shutil.move()` and `os.path.join()`.
7. **Choice Input** : asks the user for their choice, whether to continue sorting (running the program once more) or end sorting (exiting the program).


## How to Run and Use

### Prerequisites
This script runs entirely on native Python 3 standard libraries. No external package installations are necessary.

### Step-by-Step Execution
1. Place the `project_sorter.py` file into the main folder where your mixed project assets are located.
2. Run the script any way you like.
3. **Interactive Prompt:** The terminal will ask you to `enter project name`. Type your project keyword (e.g., `sunlight` or `japan`) and press Enter.
4. **Casing Safety:** The script handles input values seamlessly using case-insensitive checks. It will automatically create a folder with that name and safely pull in all files containing that keyword.
5. **Batch Processing:** To sort another project keyword without closing the program, type `1` when prompted. Press any other key to finish and exit the automation loop.
