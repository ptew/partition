import sys

def partition(n):
    # 2-D cached results by length and last partition size
    results       = [[0]*max(4,n+1) for _ in xrange(max(4,n+1))]
    results[0][1] = 1
    results[1][1] = 1
    results[2][2] = 1
    results[2][1] = 2
    results[3][3] = 1
    results[3][2] = 1
    results[3][1] = 3

    # Iterate over all the sub problems from 1 to n
    # Because we already added 0-3 base cases start with 4
    for subN in range(4,n+1):
        # Iterate over the minimum sizes from the largest (most constraining)
        # to the smallest size of 1
        for subSize in range(subN,0,-1):
            if subSize == subN:
                results[subN][subSize] = 1
                continue
            elif subN >= 2 * subSize:
                results[subN][subSize] = results[subN - subSize][subSize]
            results[subN][subSize] += results[subN][subSize+1]
    return results[n][1]

cachedResults = {}
cachedResults[0] = {}
cachedResults[0][1] = 1
cachedResults[1] = {}
cachedResults[1][1] = 1
cachedResults[2] = {}
cachedResults[2][2] = 1
cachedResults[2][1] = 2
cachedResults[3] = {}
cachedResults[3][3] = 1
cachedResults[3][2] = 1
cachedResults[3][1] = 3

# n is the number of items to partition
# minSize is the smallest block size that can be used
def recursiveParition(n,minSize):
    if n in cachedResults:
        if minSize in cachedResults[n]:
            return cachedResults[n][minSize]
    else:
        cachedResults[n] = {}

    cachedResults[n][minSize] = 0
    if n == minSize:
        cachedResults[n][minSize] = 1
    elif n >= 2 * minSize:
        for subSize in range(minSize,0,-1):
            print "n: %d subsize: %d" % (n, subSize)
            cachedResults[n][minSize] += recursivePartition(n,subSize+1) + recursivePartition(n-subSize,subSize)
    else:
        cachedResults[n][minSize] = recursivePartition(n,minSize+1)
    return cachedResults[n][minSize]

if __name__ == "__main__":
	if len(sys.argv) > 1:
		print partition(int(sys.argv[1]))
	else:
		answers = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56, 77, 101, 135, 176, 231, 297, 385, 490, 627, 792, 1002, 1255, 1575, 1958, 2436, 3010, 3718, 4565, 5604]

		for index in range(len(answers)):
		  result = partition(index)
		  passed = result == answers[index]
		  print "Passed: %d Index: %d Expected: %d  Answer: %d" % (passed, index, answers[index], result)
