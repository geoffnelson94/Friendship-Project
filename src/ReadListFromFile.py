from pathlib import Path

# This function handles file i/o for reading lists of names
def ReadListFromFile(filename,catagory):
    # Construct a relative path structure
    if catagory == 'names':
        path = Path(__file__).parent / "../names/" / str(filename)

    if catagory == 'traits':
            path = Path(__file__).parent / "../traits/" / str(filename)

    # Read each name in file into a list
    with open(path) as f:
        file_list = f.read().splitlines()
    return file_list
