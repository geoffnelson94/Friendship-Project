import random
from FileIO import ReadListFromFile

def OldEnglishName(gender):
    # Check the gender so you don't have to read all the name files
    if gender == 'male':
        names = ReadListFromFile('male_old_english','names')
    elif gender == 'female':
        names = ReadListFromFile('female_old_english','names')
    else:
        print("Bro, that is not a gender. option: male/female")

    # Return a random name in the list
    return random.choice(names)
