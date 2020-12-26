from FileIO import ReadListFromFile
from FileIO import WriteListToFile

def RemoveDuplicateFromFile(filename,catagory):
    # Grab file contents
    contents = ReadListFromFile(filename,catagory)
    size = len(contents)
    # Remove duplicates
    contents = list(set(contents))
    num_duplicate = len(contents) - size
    if num_duplicate > 0:
        # Re-write file witth pruned content
        WriteListToFile(contents,filename,catagory)
        print('Removed ' + str(num_duplicate) + ' ' + 'elements from file!')
    else:
        print('No duplicates!')

# Test
#RemoveDuplicateFromFile('female_old_english','names')
