import random
from FileIO import ReadListFromFile
from FileIO import ReadAllFromDirectory
from ProceduralNameGen import ProceduralNameGen

def NameGen(**kwargs):
    # Check the gender so you don't have to read all the name files
    if 'gender' in kwargs and kwargs['gender'] == 'male':
        print('man time!')
        names = ReadListFromFile('male_old_english','names')
    elif 'gender' in kwargs and kwargs['gender'] == 'female':
        names = ReadListFromFile('female_old_english','names')
    else:
        # If no criteria given for name, just grab all available names and
        # select one.
        names = ReadAllFromDirectory('names')

    # If procedural option given, use procedural methods
    if 'procedural' in kwargs and kwargs['procedural'] == 'yes':
        return ProceduralNameGen(names)
    else:
        # Return a random name in the list
        return random.choice(names)
