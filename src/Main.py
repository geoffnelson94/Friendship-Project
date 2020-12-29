#!/usr/bin/env python3
from NPCProfile import NPC

# Generate a random NPC with no specified options
npc = NPC()
npc.PrintInfo()
#npc.SaveToFile('my_npc')

# Generate a random NPC with a couple options
specific_npc = NPC(gender='female', race='elf', procedural='yes')
specific_npc.PrintInfo()
#specific_npc.SaveToFile('my_specific_npc')
