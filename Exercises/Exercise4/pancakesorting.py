def flip(arr, i):
    return arr[i::-1] + arr[i+1::]

def pancakesort(arr):
    flips = []
    sortedpointer = len(arr)
    while sortedpointer > 0:
        maximum = arr[0]
        maxindex = 0
        for i, element in enumerate(arr[:sortedpointer]):
            if element >= maximum:
                maximum = element
                maxindex = i
        sortedpointer -= 1
        if maxindex != sortedpointer:
            arr = flip(arr, maxindex)
            flips.append(maxindex)
        arr = flip(arr, sortedpointer)
        flips.append(sortedpointer)
    return flips

from queue import PriorityQueue

def pancakesort_leastflips(arr):
    def heuristic(_arr):
        inorder = -1
        for i, elem in _arr:
            if i == 0 or _arr[i-1] < elem:
                inorder += 1
        return inorder
    
    priority = PriorityQueue()
    priority.put((heuristic(arr), 0))
    while priority.not_empty:
        check_arr = arr
        current_flip = priority.get()

        



