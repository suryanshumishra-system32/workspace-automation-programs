# File Janitor V1 (Baseline Implementation) 

This project is a desktop/ downloads folder cleanup utility, developed during my first semester of BSc (Hons.) Computer Science. 
It was built by independently translating logical pointers and architectural steps provided by Gemini AI into functional Python code.

It works by reading file extensions and sorting them into the following categories (folders):
1. **Images** : (.png, .jpg, .jpeg, .webp, .svg)
2. **Documents** : (.pdf, .docx, .xlsx)
3. **Audio** : (.mp3, .wav, .flac)
4. **Text** : (.txt)
5. **Executables** : (.exe)
6. **Compressed** : (.zip, .7z)
7. **Videos** : (.mp4, .mov, .mkv, .webm, .avi, .wmv)
8. **Miscellaneous** : (all other file extensions)

##  Implementation & Logic
The script operates sequentially using core Python programming structures:
1. **Targeting:** Scans the active directory using the legacy `os.listdir()` module.
2. **Exclusion:** Explicitly ignores directories and its own executable file to avoid logical loops.
3. **Parsing:** Extracts file extensions using `os.path.splitext()`.
4. **Conditional Routing:** Employs a linear chain of `if/elif/else` statements to map extensions to their designated target paths.
5. **Execution:** Dispatches files to their destination using `shutil.move()`.

# How to Run and Use

### Prerequisites
Make sure you have **Python 3** installed on your system.
No external packages are required, as this script only uses Python's built-in libraries (`os` and `shutil`).

### Step-by-Step Execution
1. Place the `janitor.py` script directly into the messy folder that you want to cleaned (e.g. your Downloads folder or Desktop).
2. Run the .py file placed in the messy folder in any way that you prefer.
3. The script will instantly scan the folder and create the necessary subdirectories (`/images`, `/documents`, etc.), and move your files into them.

I intend to add more extensions and features to this!! Happy organizing!!
