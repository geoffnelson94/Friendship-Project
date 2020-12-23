import random
from ReadListFromFile import ReadListFromFile

def TraitGen(**kwargs):
    if 'race' in kwargs and kwargs['race'] == 'elvish':
        print('\n\nIt would be nice if we had elf features! ... Generic for now: \n')## TODO: Add specific elvish traits
        traits = ReadListFromFile('generic_traits','traits')
    else:
        traits = ReadListFromFile('generic_traits','traits')

    return random.choice(traits)
