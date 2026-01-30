
def getLargest(arr, mid_index = 0):
    if len(arr) == 1:
        return arr[0]
    midIndex = len(arr)//2
    midPivot = arr[midIndex]
    if midPivot > arr[midIndex - 1] and midPivot > arr[midIndex + 1]:
        return midPivot, mid_index
    if midPivot < arr[midIndex - 1]:
        return getLargest(arr[0:midPivot], mid_index + midIndex)
    else:
        return getLargest(arr[midPivot:len(arr)], mid_index + midIndex)

print(getLargest([0, 1, 2, 4, 6, 8, 10, 12, 11, 9, 7, 5, 4])) 