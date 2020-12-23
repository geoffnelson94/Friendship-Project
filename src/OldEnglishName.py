import random
from ReadNames import ReadNames

def OldEnglishName(gender):
    # Check the gender so you don't have to read all the name files
    if gender == 'male':
        names = ReadNames('male_old_english')
    elif gender == 'female':
        names = ReadNames('female_old_english')
    else:
        print("Bro, that is not a gender. option: male/female")

    # Return a random name in the list
    return random.choice(names)
