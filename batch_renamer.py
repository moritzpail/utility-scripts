import os 

# Set search string, replace string and file extension
SEARCH_STRING = "docs"
REPLACE_STRING = "doc"
TYPE_EXTENSION = ".py"


# Get all files from current directory
directory_content = os.listdir('.')
docs = [doc for doc in os.listdir('.') if os.path.isfile(doc)]

# Variable to keep track of number of renamed files
renamed_files = 0 

# Log with print statement
print(f"{len(docs)} of {len(directory_content)} are files.")

# Go through all the documents and check if they match the search pattern
for doc in docs:
    
    # Seperate filename from document extension
    document_name, filetype = os.path.splitext(doc)
    if filetype == TYPE_EXTENSION:

        # If search string is in doc
        if SEARCH_STRING in document_name:
            
            # Replace the search string with the replace string
            new_name = document_name.replace(SEARCH_STRING, REPLACE_STRING) + filetype
            os.rename(doc, new_name)
            renamed_files += 1
            
            print(f"Renamed file {doc} to {new_name}")

print(f"Renamed {renamed_files}")
        