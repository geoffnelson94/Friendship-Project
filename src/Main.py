#!/usr/bin/env python3
from OldEnglishName import OldEnglishName
from ProceduralNameGen import ProceduralNameGen
from TraitGen import TraitGen
from JobGen import JobGen

print("There is a man named: " + \
                 OldEnglishName(gender='male') + \
                 "\nwho" + " " + TraitGen() + '\n'
                 "and works as a " + JobGen() + '\n' )

print("A female elf named: " + \
                 OldEnglishName(gender='female') + \
                 "\nwho " + TraitGen(race='elvish') + '\n'
                 "and works as a " + JobGen() + '\n' )

print("A random name generated procedurally: " + \
                 ProceduralNameGen('male_old_english'))
