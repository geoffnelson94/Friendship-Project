# Import all the tools used to randomly generate NPC profile
from NameGen import NameGen
from ProceduralNameGen import ProceduralNameGen
from TraitGen import TraitGen
from JobGen import JobGen

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
        print('new NPC class details: \n' + \
              'name: ' + self.name + '\n' + \
              'quirk: ' + self.quirk + '\n' + \
              'job: ' + self.job + '\n')
