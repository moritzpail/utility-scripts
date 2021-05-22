import os
import argparse


parser = argparse.ArgumentParser(description="Batch rename files in directory")

# Define arguments to be parsed 
parser.add_argument("search", type=str, help="To be replaced text")
parser.add_argument("replace", type=str, help="String to replace text")
parser.add_argument(
    "--filetype",
    type=str,
    default=None,
    help="Only files with the given extension will be renamed (e.g. '.txt')."
)
parser.add_argument(
    "--path",
    type=str,
    default=".",
    help="Directory path that contains the to be renamed files."
)

# Parse arguments
arguments = parser.parse_args()
print(arguments)

# Set search string, replace string and file extension
search_string = arguments.search
replace_string = arguments.replace
type_filter = arguments.filetype
path=arguments.path

print(f"Renaming files at path {path}")

# Get all files from current directory
directory_content = os.listdir(path)
path_dir_content = [os.path.join(path, doc) for doc in directory_content]
docs = [doc for doc in path_dir_content if os.path.isfile(doc)]

# Variable to keep track of number of renamed files
renamed_files = 0 

# Log with print statement
print(f"{len(docs)} of {len(directory_content)} are files.")

# Go through all the documents and check if they match the search pattern
for doc in docs:
    
    # Seperate filename from document extension
    full_document_path, filetype = os.path.splitext(doc)
    document_path = os.path.dirname(full_document_path)
    document_name = os.path.basename(full_document_path)
    
    # Filter for files with the right extension
    if filetype == type_filter or type_filter is None:

        # If search string is in doc
        if search_string in document_name:
            
            # Replace the search string with the replace string
            new_document_name = document_name.replace(search_string, replace_string)
            new_document_path = os.path.join(document_path, new_document_name) + filetype
            os.rename(doc, new_document_path)
            renamed_files += 1
            
            print(f"Renamed file {doc} to {new_document_path}")

print(f"Renamed {renamed_files}")
        