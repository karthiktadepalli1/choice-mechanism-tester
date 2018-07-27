import numpy as np
import statistics

def createDistributions(rankVectors):
  rankDistribs = []
  numItems = len(rankVectors[0])
  # each element will be a list of rank distributions drawn from each party's rank vector
  for i in range(numItems):
    distributionList = []
    for rankVector in rankVectors:
      distributionList.append(rankVector[i])
    rankDistribs.append(distributionList)
  
  return(rankDistribs)

def RankSumMin(rankVectors):
  """
  Mechanism: rank sum minimization, ties broken by variance. 
  Helper function for allocate()
  """
  rankDistribs = createDistributions(rankVectors)

  sumList = []
  for distribution in rankDistribs:
    sumList.append(sum(distribution))
  
  minim = min(sumList) # we want the minimum rank sum
  indices = [i for i, x in enumerate(sumList) if x == minim]
  # this discovers if multiple allocations have the same rank sum

  if len(indices) == 1:  
    rightIndex = indices[0]
    # if one allocation has a strictly lower rank sum than all others, it's the optimal allocation
  else:
    stdevs = []
    for index in indices:
      stdevs.append(statistics.stdev(rankDistribs[index]))
      # we break rank sum ties using standard deviation - we want the allocation with less deviation
    
    lessSDindex = stdevs.index(min(stdevs))
    rightIndex = indices[lessSDindex]
  
  optimal = rankDistribs[rightIndex]
  return(optimal)


def LeastVetos(rankVectors):
  """

  """
  rankDistribs = createDistributions(rankVectors)
  veto = len(rankVectors[0]) - 1
  vetoCounters = []
  for distribution in rankDistribs:
    vetos = [i for i in distribution if i == veto]
    vetoCounters.append(len(vetos))
  
  minim = min(vetoCounters)
  indices = [i for i, x in enumerate(vetoCounters) if x == minim]

  if len(indices) == 1:  
    rightIndex = indices[0]
    # if one allocation has a strictly lower rank sum than all others, it's the optimal allocation
  else:
    sums = []
    for index in indices:
      sums.append(sum(rankDistribs[index]))
      # we break rank sum ties using standard deviation - we want the allocation with less deviation
    
    rightIndex = indices[sums.index(min(sums))]

  optimal = rankDistribs[rightIndex]
  return(optimal)







