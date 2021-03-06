import statistics


def createDistributions(rankVectors):
    """
    A helper function for our voting mechanisms that creates rank distributions
    @param rankVectors - the list of rank vectors of each voter
    """
    rankDistribs = []
    numCandidates = len(rankVectors[0])
    # each element = list of rank distribs drawn from each voter's rank vector
    for i in range(numCandidates):
        distributionList = []
        for rankVector in rankVectors:
            distributionList.append(rankVector[i])
        rankDistribs.append(distributionList)
    return(rankDistribs)


def RankSumMin(rankVectors):
    """
    Mechanism: rank sum minimization, ties broken by lower variance.
    This is a specific case of Borda count voting.
    @param rankVectors - the list of rank vectors of each voter
    """
    rankDistribs = createDistributions(rankVectors)

    sumList = []
    for distribution in rankDistribs:
        sumList.append(sum(distribution))

    minim = min(sumList)  # we want the minimum rank sum
    indices = [i for i, x in enumerate(sumList) if x == minim]
    # this discovers if multiple allocations have the same rank sum

    if len(indices) == 1:
        rightIndex = indices[0]
        # strictly lowest rank sum => optimal candidate
    else:
        stdevs = []
        for index in indices:
            stdevs.append(statistics.stdev(rankDistribs[index]))
            # we break ties in favour of the lower-variance candidate
        lessSDindex = stdevs.index(min(stdevs))
        rightIndex = indices[lessSDindex]

    optimal = rankDistribs[rightIndex]
    return(optimal)


def FewestVetos(rankVectors, vetoThreshold):
    """
    Mechanism: veto minimization, ties broken by lower rank sum.
    @param rankVectors - the list of rank vectors of each voter
    @param vetoThreshold - the rank a candidate must be given to be considered
    vetoed by the voter (higher number = worse rank)
    """
    rankDistribs = createDistributions(rankVectors)
    vetoCounters = []
    vetoThreshold -= 1  # to account for indexing
    for distribution in rankDistribs:
        vetos = [i for i in distribution if i >= vetoThreshold]
        vetoCounters.append(len(vetos))

    minim = min(vetoCounters)
    indices = [i for i, x in enumerate(vetoCounters) if x == minim]

    if len(indices) == 1:
        rightIndex = indices[0]
        # strictly fewer vetos => the candidate is the optimal candidate
    else:
        sums = []
        for index in indices:
            sums.append(sum(rankDistribs[index]))
        # we break veto ties in favour of the lower rank sum
        rightIndex = indices[sums.index(min(sums))]

    optimal = rankDistribs[rightIndex]
    return(optimal)


def InverseRankSumMax(rankVectors):
    """
    Mechanism: Convert rank sums to an inverse scale and maximize.
    The difference from RankSumMin is, higher ranks are weighted more heavily
    and lower ranks are discounted more heavily, eg. rank 1 (1 point) counts
    twice as much as rank 2 (0.5 points).
    @param rankVectors - the list of rank vectors of each voter.
    """
    for vector in rankVectors:
        vector = [-1/(float(x+1)) for x in vector]
        # x+1 to account for indexing, -ve sign to use RankSumMin to maximize,
        # even though the method actually minimizes based on its input.

    optimal = RankSumMin(rankVectors)
    return(optimal)
