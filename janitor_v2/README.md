# Janitor V2

This is the upgraded, highly optimized version of the first Janitor script (janitor_v1).
After completing the baseline version (V1), I analyzed its structural weak points and remade the entire codebase to meet modern, industry-standard Python practices.

## 📈 The Engineering Retrospective (V1 vs. V2)

When reviewing my **[V1 Code](../janitor_v1/)**, I identified three major constraints that needed fixing:

1. **Code Repetition (The DRY Principle):** V1 relied heavily on a long, repetitive chain of `if/elif` blocks.
    If I wanted to add a new file category, I had to write an entirely new branch of conditional logic.
3. **Scattered Variables:** Every folder and extension list lived as a loose, independent string variable, making the codebase noisy and hard to scale.
4. **The System-Lookup Bug:** V1 permanently overwrote the main `filename` string variable to lowercase before moving it.
    On case-sensitive operating systems (like Linux), this caused severe file-system lookups to fail, resulting in crashes.

## V2 Optimizations
In this version, I completely overhauled the code architecture:
* **Dictionary Mappings:** I mapped target destination folders directly to tuples of extensions (`{folder: extensions}`).
  This cleanly separates program configuration from execution logic.
* **Dynamic Loop Generation:** Folders are now automatically verified and created using a clean, compact loop over the dictionary, completely eliminating lines of repetitive boilerplate code.
* **Inline Normalization:** String casing (`.lower()`) is now applied *inline* exclusively during comparison checks.
   The original filename variable remains unchanged, ensuring the code safely executes across Windows, macOS, and Linux without losing source information.
* **Safety Tracking Flag:** Implemented a boolean tracking flag (`moved`) to cleanly handle unrecognized file formats and route them to a fallback
   `miscellaneous` folder without interrupting core logic.

---

## How to Run and Use

### Prerequisites
Make sure you have **Python 3** installed on your system. No external packages are required, as this script uses Python's built-in libraries (`os` and `shutil`).

### Step-by-Step Execution
1. Place the `janitor.py` script directly into the messy folder you want to clean up (e.g., your Downloads folder or Desktop).
2. Run the script any way you like.
4. The script will instantly scan the folder, dynamically create the necessary subdirectories (`/images`, `/documents`, etc.), and route your files into them.
