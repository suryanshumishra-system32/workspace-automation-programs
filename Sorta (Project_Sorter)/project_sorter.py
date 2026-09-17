import os
import shutil

directory = "."

all_files = os.listdir(directory)
choice = 1
while choice == 1:

    project_name = input("enter project name")
    project_name_lower = project_name.lower()

    project_folder= "./"+project_name
    os.makedirs(project_folder, exist_ok=True)


    for filename in all_files:
        filename=filename.lower()
        if os.path.isdir(filename) or filename=="project_sorter.py":
            continue
        elif project_name_lower in filename:
            print("moving", filename,"to", project_name)
            shutil.move(filename, os.path.join(project_folder, filename))
    choice = int(input("Enter '1' to continue sorting"))
    
print("sorting complete!")
