import os 
import argparse


# Set up argument parser
parser = argparse.ArgumentParser(
    description="Clean up directory by putting files into respective folders."
)

parser.add_argument(
    "--path",
    type=str,
    default=".",
    help="Directory path to the to be cleaned up directory."
)

# Parse arguments
args = parser.parse_args()
path = args.path

print(f"Cleaning up directory {path}")

# Get all the files of a given directort
dir_content = os.listdir(path)
path_dir_content = [os.path.join(path, doc) for doc in dir_content]
docs = [doc for doc in path_dir_content if os.path.isfile(doc)]
folders = [folder for folder in path_dir_content if os.path.isdir(folder)]

moved = 0
created_folders = []

print(f"There are {len(docs)} {'doc' if len(docs) == 1 else 'docs'} and {len(folders)} {'folder' if len(folders) == 1 else 'folders'} in the directory.")
print()
print(f"Cleaning up {len(docs)} of {len(dir_content)} elements.")

# Go through all files and move them to into according folder
for doc in docs:
    # Seperate name from file extension
    full_doc_path, filetype = os.path.splitext(doc)
    doc_path = os.path.dirname(full_doc_path)
    doc_name = os.path.basename(full_doc_path)
    
    # Skip this python file
    if doc_name == "directory_clean.py" or doc_name.startswith("."):
        continue
    
    # Get the subfolder and create the folder if not existing
    subfolder_path = os.path.join(path, filetype[1:].lower())
    
    if subfolder_path not in folders and subfolder_path not in created_folders:
        try: 
            os.mkdir(subfolder_path)
            created_folders.append(subfolder_path)
            print(f"Folder {subfolder_path} created.")
        except FileExistsError as err:
            print(f"Folder already exists at {subfolder_path} .. {err}")
            print(created_folders)
            
    # Get new folder path and move the file
    new_doc_path = os.path.join(subfolder_path, doc_name) + filetype
    os.rename(doc, new_doc_path)
    moved += 1
    print(f"Moved file {doc} to {new_doc_path}.")

print(f"Renamed {moved} of {len(docs)} files.")
    


