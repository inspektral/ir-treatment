import os

def rename_files(root_folder):
    for root, dirs, files in os.walk(root_folder):
        for i, file in enumerate(files):
            if file.endswith(".wav"):
                old_file = os.path.join(root, file)
                new_file = os.path.join(root, f"{os.path.basename(root)}{i:06d}.wav")
                os.rename(old_file, new_file)

# Usage
rename_files("D:/datasets/reverbs")