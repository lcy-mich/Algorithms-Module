def flip(arr, i, j):
    return arr[:i] + arr[j:i-1:-1] + arr[j+1:]

def getbreakpoints(arr):
    breakpoints = []
    if abs(arr[0] - arr[1]) > 1:
        breakpoints.append(1)
    order = 0
    for i in range(2, len(arr)):
        if arr[i] - arr[i-1] == order or abs(arr[i] - arr[i-1]) > 1:
            breakpoints.append(i)
            order = arr[i] - arr[i-1] if abs(arr[i] - arr[i-1]) <= 1 else 0
    return breakpoints

def heuristic(arr, breakpoints = None):
    if not breakpoints:
        breakpoints = getbreakpoints(arr)
    inorder = -1
    for i, elem in enumerate(arr):
        if i == 0 or arr[i-1] < elem:
            inorder += 1
    return inorder + 1/(len(breakpoints)+0.1)



def advancedpancakesort(arr):
    breakpoints = getbreakpoints(arr)
    h_val = heuristic(arr, breakpoints)
    
    resultflips = []
    resultarr = arr
    resultbkpts = breakpoints
    # print(breakpoints)
    while len(resultbkpts) > 0:
        print(resultarr)
        besth_val = 0
        bestflip = []
        for break1 in resultbkpts:
            for break2 in resultbkpts:
                checkarr = resultarr
                if break1 >= break2:
                    continue
                checkarr = flip(checkarr, break1, break2)
                checkh_val = heuristic(checkarr)
                if checkh_val >= besth_val:
                    bestflip = [break1, break2]
                    besth_val = checkh_val
                # print(break1, break2, checkh_val)
        resultflips.append(bestflip)
        resultarr = flip(resultarr, bestflip[0], bestflip[1])
        resultbkpts = getbreakpoints(resultarr)
    return resultflips
# doesnt work

print(advancedpancakesort([1,8,9,3,2,7,6,5,4,10]))
