import random
from FileIO import ReadListFromFile

def JobGen(**kwargs):
    jobs = ReadListFromFile('generic_jobs','jobs')
    return random.choice(jobs)
