import random
import math

def AbilityGen(**kwargs):
    # A default of level 1, basic NPC with no class and human race
    ability_distro = [8,9,10,11,12,13]

    # Randomly add +2 for human
    ability_distro[random.choice(range(0,len(ability_distro)))]+=2

    # Shuffle to randomize ability scores
    random.shuffle(ability_distro)

    # Determine ability modifers
    mod_minimum = -5
    mod = []
    for elem,abil in enumerate(ability_distro):
        mod.append(math.floor(abil/2) + mod_minimum)
        if mod[elem] >= 0:
            mod[elem] = '+' + str(mod[elem])

    # Return a dictionary of abilities
    ability_names = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    abilities = {}
    for elem,abil in enumerate(ability_distro):
        abilities[ability_names[elem]] = str(abil) + ' (' + str(mod[elem]) + ')'
    return abilities
