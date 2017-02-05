def _importLists(directory):
    with open(directory) as f:
        data = f.readlines()
    return [[eval(val) for val in line.strip().split(',')] for line in data]

def _pickCombination(x,counter):
    return [x[i][counter[i]] for i in range(0,len(counter))]

def allcombinations(directory):
	 #Import lists
    x = _importLists(directory)
	 #Setup
    counter = [0]*len(x)
    maxCounter = [len(x[i]) for i in range(0,len(x))]
	 #Iterate
    while counter[-1]<maxCounter[-1]:
        #Output
        yield _pickCombination(x,counter)
        #Adjust counter
        counter[0]+=1
        indicator = 0
        while counter[indicator]>=maxCounter[indicator] and indicator<len(x)-1:
            counter[indicator]=0    
            indicator+=1
            counter[indicator]+=1
    return