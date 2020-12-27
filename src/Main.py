#!/usr/bin/env python3
from NameGen import NameGen
from ProceduralNameGen import ProceduralNameGen
from TraitGen import TraitGen
from JobGen import JobGen
from NPCProfile import NPC

# Generate a random NPC with no specified options
npc = NPC()
npc.PrintInfo()

# Generate a random NPC with a couple options
specific_npc = NPC(gender='female', race='elf')
specific_npc.PrintInfo()
