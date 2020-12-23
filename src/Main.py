#!/usr/bin/env python3
from OldEnglishName import OldEnglishName
from TraitGen import TraitGen

print("There is a man named: " + \
                 OldEnglishName('male') + \
                 "\nwho" + " " + TraitGen())

print("A female elf named: " + \
                 OldEnglishName('female') + \
                 "\nwho" + " " + TraitGen(race='elvish'))
