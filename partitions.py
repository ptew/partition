#!/usr/bin/python
import sys

def partition(n):
  # Results cached in an array
  results = []
  results.append(1)
  results.append(1)
  results.append(2)
  results.append(3)

  # 2-D cached results by length and last partition size
  resultsByLength       = {}
  resultsByLength[1]    = {}
  resultsByLength[1][1] = 1
  resultsByLength[2]    = {}
  resultsByLength[2][2] = 1
  resultsByLength[3]    = {}
  resultsByLength[3][2] = 1
  resultsByLength[3][3] = 1

  for index in range(4,n+1):
    result = results[index-1]
    resultsByLength[index] = {}
    newCombinations = 0

    for length in range(index,1,-1):
      resultsByLength[index][length] = 0
      if length == index:
        resultsByLength[index][length] = 1
        newCombinations = 1
      elif (index - length) > 1 and (index - length) >= length:
        resultsByLength[index][length] += resultsByLength[index - length][length] + newCombinations
        newCombinations += resultsByLength[index - length][length]
      else:
        resultsByLength[index][length] += newCombinations

    result += resultsByLength[index][2]
    results.append(result)
  return results[n]

cachedResults = {}
def recursiveParition(n, minBlockSize):
  if
  elif n == 0:
    return 1
  elif n == 1:
    cachedResults[1]    = {}
    cachedResults[1][1] = 1
    return 1
  elif n == 2:
    cachedResults[2]    = {}
    cachedResults[2][2] = 1
    cachedResults[2][1] = 2
    return 2
  elif n == 3:
    cachedResults[3]    = {}
    cachedResults[3][3] = 1
    cachedResults[3][2] = 1
    cachedResults[3][1] = 3
    return 3


  result = 0
  cachedResults[n] = {}
  for minBlock in range(minBlockSize,n):
    subProblemLength = n - minBlock
    if (subProblemLength > 1) and subProblemLength >= minBlock:
      cachedResults[subProblemLength][minBlock] = recursiveParition(subProblemLength, minBlock)
      result += cachedResults[subProblemLength][minBlock]
    elif subProblemLength == minBlockSize:
      result += 1

  cachedResults[n][minBlockSize] = result
  print cachedResults

  return result

if __name__ == "__main__":
	if len(sys.argv) > 1:
		print partition(int(sys.argv[1]))
	else:
		#answers = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56, 77, 101, 135, 176, 231, 297, 385, 490, 627, 792, 1002, 1255, 1575, 1958, 2436, 3010, 3718, 4565, 5604]
		answers = [1, 1, 2, 3, 5, 7, 11]#, 15, 22, 30, 42, 56, 77, 101, 135, 176, 231, 297, 385, 490, 627, 792, 1002, 1255, 1575, 1958, 2436, 3010, 3718, 4565, 5604]

		for index in range(len(answers)):
			result = recursiveParition(index,1)
			passed = result == answers[index]
			print "Passed: %d Index: %d Expected: %d  Answer: %d" % (passed, index, answers[index], result)
