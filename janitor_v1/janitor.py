import os
import shutil

directory = "."

images = "./images"
documents = "./documents"
audio = "./audio"
text = "./text"
misc = "./miscellaneous"
exe = "./executables"
comp = "./compressed"
video = "./videos"

os.makedirs(images, exist_ok=True)
os.makedirs(documents, exist_ok=True)
os.makedirs(audio, exist_ok=True)
os.makedirs(text, exist_ok=True)
os.makedirs(misc, exist_ok=True)
os.makedirs(exe, exist_ok=True)
os.makedirs(comp, exist_ok=True)
os.makedirs(video, exist_ok=True)

all_files = os.listdir(directory)

for filename in  all_files:
    if os.path.isdir(filename) or filename == "janitor.py":
        continue
    _,file_ext=os.path.splitext(filename)
    file_ext=file_ext.lower()
    if file_ext==".png" or file_ext== ".jpg" or file_ext==".jpeg" or file_ext==".webp" or file_ext==".svg":
        print("moving", filename,"to images")
        shutil.move(filename, os.path.join(images, filename))
    elif file_ext==".pdf" or file_ext== ".docx" or file_ext==".xlsx":
        print("moving", filename, "to documents")
        shutil.move(filename, os.path.join(documents, filename))
    elif file_ext==".mp3" or file_ext== ".wav" or file_ext== ".flac":
        print("moving", filename,"to audio")
        shutil.move(filename, os.path.join(audio, filename))
    elif file_ext==".txt":
        print("moving", filename,"to text")
        shutil.move(filename, os.path.join(text, filename))
    elif file_ext==".exe":
        print("moving", filename,"to executables")
        shutil.move(filename, os.path.join(exe, filename))
    elif file_ext==".zip" or file_ext==".7z" or file_ext==".rar":
        print("moving", filename,"to compressed")
        shutil.move(filename, os.path.join(comp, filename))
    elif file_ext==".mp4" or file_ext==".mov" or file_ext==".mkv" or file_ext==".webm" or file_ext==".avi" or file_ext==".wmv":
        print("moving", filename,"to videos")
        shutil.move(filename, os.path.join(video, filename)) 
    else:
        print("moving", filename, "to miscellaneous")
        shutil.move(filename, os.path.join(misc, filename))

print("Cleanup complete!")

'''notes : _, splits the tuple we get from os.path.splitext() and makes the name of the file be ignored
because of the underscore and the extension be saved

os.listdir() lists all files in the directory to python
os.makedir() makes a directory (folder) in the folder being used, the exist_ok argument is used in order to prevent a crash 
if the folder we are trying to make already exists
os.path.join() joins two paths using the correct format for the os currently in use
it is used here so that our files stay safe and are made a directory instead of relying
on the shutil.move() function to do it
shutil.move() moves a file to a given directory
os.path.isdir() checks whether the argument inserted (such as filename here) is a directory (folder) itself
it is used here to prevent a directory itself from being moved which also inherently means that this program
will not be able to sort folders into other folders
while assigning directory variables values for the directory, a "." is used to indicate "this folder" (the one the program
file exists in) and forward slashes "/" after the dot can be used to indicate "inside this folder"'''