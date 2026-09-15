import os
import shutil

foldandext = {"./Images" : (".png", ".jpg", ".jpeg", ".webp", ".svg") , "./Documents" : (".pdf", ".docx", ".xlsx"), "./Audio" : (".mp3", ".wav", ".flac"),
               "./Text" : (".txt", ".rtf", ".md"), "./Executables" : (".exe"),
                 "./Compressed" : (".zip", ".7z", ".rar"), "./Videos" : (".mp4", ".mov", ".mkv", ".webm", ".avi", ".wmv")}

for keys in foldandext:
    os.makedirs(keys, exist_ok=True)

misc = "./Miscellaneous"
os.makedirs(misc, exist_ok=True)


directory = "."
all_files = os.listdir(directory)

for filename in  all_files:
    all_files = os.listdir(directory)
    if os.path.isdir(filename) or filename == "janitor.py":
        continue
    _,file_extog=os.path.splitext(filename)
    file_ext=file_extog.lower()
    for keys, ext in foldandext.items():
        if file_ext in ext:
            print("Moving", filename, "to", keys.strip("."))
            shutil.move(filename, os.path.join(keys, filename))
            moved = True
            break
    
if not moved:
    shutil.move(filename, os.path.join(misc, filename))
    
print("Cleanup complete!")