def mincoin(coinvalues, target):
    coinvalues = sorted(coinvalues, reverse=True)
    additions = []
    for value in coinvalues:
        mult = 1
        if value <= target:
            while value*mult <= target:
                mult += 1
        mult -= 1
        for _ in range(mult):
            additions.append(value)
            target -= value
    return additions

print(mincoin([1,2,5,10,20,50], 28))