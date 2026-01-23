def mincoin(coinvalues, target):
    additions = []
    for value in sorted(coinvalues, reverse=True):
        mult = 1
        if value <= target:
            while value*mult <= target:
                mult += 1
        mult -= 1
        for _ in range(mult):
            additions.append(value)
            target -= value
    return additions


assert(mincoin([1,2,5,10,20,50], 7) == [5,2])
assert(mincoin([1,2,5,10,20,50], 150) == [50,50,50])
assert(mincoin([1,2,5,10,20,50], 28) == [20,5,2,1])
assert(mincoin([1,4,6], 7) == [6,1])
print(mincoin([1,4,6], 9)) #doesn't work