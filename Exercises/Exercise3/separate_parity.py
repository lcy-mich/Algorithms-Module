def separateParity(nums):
    res = [None for i in range(len(nums))]
    lastpositive = -2
    lastnegative = -1

    for num in nums:
        print(res)
        if num >= 0:
            lastpositive += 2
            if lastpositive < len(nums):
                res[lastpositive] = num
            else:
                lastnegative += 2
                if lastnegative < len(nums):
                    res[lastnegative] = num
        else:
            lastnegative += 2
            if lastnegative < len(nums):
                res[lastnegative] = num
            else:
                lastpositive += 2
                if lastpositive < len(nums):
                    res[lastpositive] = num
    
    return nums
        
# def quicksort(li):
#     if len(li) == 1: return li[0]
#     return quicksort([x < li[len(li)//2] for x in li].append([li[len(li)//2]].append(quicksort([x > li[len(li)//2] for x in li]))))

print(separateParity([5,4,3,2,1,1,-2,-3,-4,-5]))

# doesnt work