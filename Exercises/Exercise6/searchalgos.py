from random import shuffle, randrange
from time import time, perf_counter
from sys import setrecursionlimit
setrecursionlimit(10000)

def lin_search(haystack, needle):
    for index, value in enumerate(haystack):
        if value == needle:
            return index
    return None

def bin_search(haystack, needle, bottom = None, top = None):
    if not bottom and not top: bottom, top = 0, len(haystack)
    
    if bottom > top:
        return None
    else:
        mid = (top + bottom) // 2
        if haystack[mid] == needle:
            return mid
        elif haystack[mid] > needle:
            return bin_search(haystack, needle, bottom, mid - 1)
        else:
            return bin_search(haystack, needle, mid + 1, top)
        
def tri_search(haystack, needle, bottom = None, top = None):
    if not bottom and not top: bottom, top = 0, len(haystack)
    
    if bottom > top:
        return None
    else:
        mid_1 = ((top + bottom) // 3)
        mid_2 = (2*(top + bottom)//3)
        if haystack[mid_1] == needle:
            return mid_1
        elif haystack[mid_2] == needle:
            return mid_2
        elif haystack[mid_1] > needle:
            return tri_search(haystack, needle, bottom, mid_1 - 1)
        elif haystack[mid_2] < needle:
            return tri_search(haystack, needle, mid_2 + 1, top)
        else:
            return tri_search(haystack, needle, mid_2 + 1, mid_1 - 1)

total_lin, total_bin, total_tri = 0,0,0
amt = 100000
itmcnt = 1000
search = randrange(0, itmcnt)

print(search)
for _ in range(amt):
    sorted = range(0, itmcnt)
    unsorted = list(sorted).copy()
    shuffle(unsorted)

    start = perf_counter()
    lin_search(unsorted, search)
    total_lin += perf_counter() - start

    start = perf_counter()
    bin_search(sorted, search)
    total_bin += perf_counter() - start

    start = perf_counter()
    tri_search(sorted, search)
    total_tri += perf_counter() - start

print(f"For {itmcnt} items, averaged over {amt} times:\n\tLinear: {total_lin/amt}\n\tBinary: {total_bin/amt}\n\tTrinary: {total_tri/amt}")