from mechs import *
from allocation import *

def checkPerformance(numAgents, numItems, guaranteeThreshold, numReps):
  """
  Conducts an allocation repeatedly to investigate whether it has a performance guarantee for all possible rank distributions.
  """
  successFlag = True  
  for i in range(numReps):
    if allocate(numAgents, numItems, guaranteeThreshold) == False:
      successFlag = False
      break
  print(successFlag)