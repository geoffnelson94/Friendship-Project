# Import all the tools used to randomly generate NPC profile
from NameGen import NameGen
from ProceduralNameGen import ProceduralNameGen
from TraitGen import TraitGen
from JobGen import JobGen

# Import needed file I/O
from FileIO import PathContructor

# Main class for holding NPC information and utility for it
class NPC:
    name = None
    quirk = None
    job = None

    def __init__(self, **kwargs):
        # Generate name
        self.name = NameGen(**kwargs)
        # Generate trait
        self.quirk = TraitGen(**kwargs)
        # Generate Job
        self.job = JobGen(**kwargs)

    def PrintInfo(self):
        print('NPC class details: \n' + \
              'name: ' + self.name + '\n' + \
              'quirk: ' + self.quirk + '\n' + \
              'job: ' + self.job + '\n')

    def SaveToFile(self,filename):
        # Contruct path for saving file
        path = PathContructor(filename, 'save')

        # Contruct output formatting
        npc_details = ["NPC class details:"]
        npc_details.append('name: ' + self.name)
        npc_details.append('quirk: ' + self.quirk)
        npc_details.append('job: ' + self.job)

        with open(path,'w') as filehandle:
            filehandle.writelines("%s\n" % elem for elem in npc_details)
