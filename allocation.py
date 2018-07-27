import numpy as np
from mechs import *

def allocate(numAgents, numItems, guaranteeThreshold):
  """
  implements the allocation A and returns True if A has a performance guarantee. Helper function for checkPerformance().
  @param numAgents - the number of parties with rank preferences on all the items 
  @param numItems - total number of items from which A chooses one
  @param guaranteeThreshold - n such that A has performance guarantee iff the optimal choice was the lowest ranked preference of fewer than n people
  """
  rankVectors = []
  # each element will be a randomly generated list of rank preferences
  for i in range(numAgents):
    rankVectors.append(list(np.random.permutation(numItems)))
  
  optimal = RankSumMin(rankVectors)


  guarantee = False
  counter = 0
  maxRank = numItems - 1
  for rank in optimal:
    if rank == maxRank:
      counter += 1
  if counter < guaranteeThreshold:
    guarantee = True
  return(guarantee)