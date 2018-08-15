import numpy as np
from mechs import *


def g1_checker(mech, numVoters, numCandidates, maxVetos, vetoThreshold):
    """
    Checks if the given mechanism fulfills the "least disliked" guarantee
    Formally expressed as G1 in README.md
    @param mech - the voting mechanism being tested
    @param numVoters - the number of voters
    @param numCandidates - the number of candidates
    @param maxVetos - maximum acceptable vetos for a winning candidate
    @param vetoThreshold - the highest rank that constitutes a veto
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


def g2_checker(mech, numVoters, numCandidates):
    """
    Checks if the given mechanism satisfies the Condorcet criterion, i.e the
    winner of the election is also the winner of every two-person election
    between that candidate and any other candidate.
    """


def loopChecker(numReps, g_checker, *args):
    """
    Conducts a vote repeatedly to check all possible distributions
    Uses results to check if the mech satisfies the performance guarantee
    """
    successFlag = True
    for i in range(numReps):
        if not g_checker(*args):
            successFlag = False
            break
    print(successFlag)
