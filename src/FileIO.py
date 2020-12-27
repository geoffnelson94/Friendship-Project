from pathlib import Path
import os, os.path

# Handles contructing path from catagory
def PathContructor(filename=None,catagory=None):
    # Step back from src directory
    path = Path(__file__).parent / ".."

    # If catagory, step path into that catagory
    if catagory != None:
        if catagory == 'names' or catagory == 'name':
            path = Path(__file__).parent / "../names/"
        elif catagory == 'trait' or catagory == 'traits':
            path = Path(__file__).parent / "../traits/"
        elif catagory == 'jobs' or catagory == 'job':
            path = Path(__file__).parent / "../jobs/"

    # Add filename if provided
    if filename != None:
        path = path / str(filename)

    return path

# Handles reading list from file
def ReadListFromFile(filename,catagory):
    # Construct a relative path structure
    path = PathContructor(filename,catagory)

    # Read each name in file into a list
    with open(path, 'r') as f:
        file_list = f.read().splitlines()
    return file_list

def ReadAllFromDirectory(catagory):
    path = PathContructor()
    all_elem = []
    for name in os.listdir(path):
        if os.path.isfile(name):
            with open(os.path.join(DIR, name),'r') as filehandle:
                all_elem.append(filehandle.read().splitlines())

    return all_elem

# Handles writing contents of a list to file
def WriteListToFile(my_list,filename,catagory):
    # Construct a relative path structure
    path = PathContructor(filename,catagory)

    # Write contents to file
    with open(path, 'w') as filehandle:
        filehandle.writelines("%s\n" % elem for elem in my_list)

def AppendListToFile(my_list, filename, catagory):
    # Construct a relative path structure
    path = PathFromCatagory(filename,catagory)

    # Append contents to end of existing file
    with open(path, 'a') as filehandle:
        filehandle.writelines("%s\n" % elem for elem in my_list)

def DeleteListFromFile(my_list, filename, catagory):
    # Grab all contents currently in file
    old_contents = ReadListFromFile(filename,catagory)

    # Determine overlap in content to be deleted vs. current contents
    new_contents = [elem for elem in old_contents if elem not in my_list]

    # Write the new contents back to file
    WriteListToFile(new_contents, filename, catagory)
