import random
from FileIO import ReadListFromFile

def TraitGen(**kwargs):
    valid_elf_terms = ['elf', 'elvish', 'elfs', 'Elf', 'Elvish', 'Elfs']
    if 'race' in kwargs and kwargs['race'] in valid_elf_terms:
        print('\nIt would be nice if we had elf features! ... Oh well, generic for now:')## TODO: Add specific elvish traits
        traits = ReadListFromFile('generic_traits','traits')
    else:
        traits = ReadListFromFile('generic_traits','traits')

    return random.choice(traits)
