import numpy as np
from mechs import *


def check_g1(mech, numVoters, numCandidates, maxVetos, vetoThreshold):
    """
    implements the allocation A and returns True if A has a performance guarantee. Helper function for checkPerformance().
    @param numVoters - the number of parties with rank preferences on all the items
    @param numCandidates - total number of items from which A chooses one
    @param guaranteeThreshold - n such that A has performance guarantee iff the optimal choice was the lowest ranked preference of fewer than n people
    """
    rankVectors = []
    # each element will be a randomly generated list of rank preferences
    for i in range(numVoters):
        rankVectors.append(list(np.random.permutation(numCandidates)))

    optimal = mech(rankVectors)

    guarantee = False
    counter = 0
    vetoThreshold -= 1
    for rank in optimal:
        if rank >= vetoThreshold:
            counter += 1
    if counter < maxVetos:
        guarantee = True
    return(guarantee)


def loopChecker(numReps, guarantee, **args):
    """
    Conducts a vote repeatedly to check all possible distributions
    Uses results to check if the mech satisfies the performance guarantee
    """
    successFlag = True
    for i in range(numReps):
        if not guarantee(**args):
            successFlag = False
            break
    print(successFlag)
