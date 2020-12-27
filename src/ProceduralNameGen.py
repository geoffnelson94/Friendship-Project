from BreakToSyllables import BreakToSyllables
from FileIO import ReadListFromFile
import random

def ProceduralNameGen(name_list):
    # Grab a list of names
    names = ReadListFromFile(name_list,'names')

    # Break list into syllable components
    syllable_tool = BreakToSyllables()
    components = syllable_tool.ListToSyllables(names)

    # Randomly decide number of syllables in the name (Limit to 3 for now)
    num_syllables = random.choice([1,2,3])

    # Piece together randomly syllables in the sequence
    # first : (middle*num_syllables-2) : last
    new_name = ''

    # Pick a 'first syllable' component
    new_name+=random.choice(components[0])

    # Pick 'middle syllable' components
    num_middle_syllables = num_syllables-2
    if num_middle_syllables > 0:
        for i in range(0,num_middle_syllables):
            new_name+=random.choice(components[1])

    # Pick 'end syllable' componentBB
    new_name+=random.choice(components[2])

    return new_name
