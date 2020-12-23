from pathlib import Path

# This function handles file i/o for reading lists of names
def ReadNames(filename):
    # Construct a relative path structure
    path = Path(__file__).parent / "../names/" / str(filename   )

    # Read each name in file into a list
    with open(path) as f:
        names = f.read().splitlines()
    return names
