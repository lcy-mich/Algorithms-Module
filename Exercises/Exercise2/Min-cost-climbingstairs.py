# def minCost(costList):
#     cost = 0
#     i = 0
#     while i < len(costList):
#         cost += costList[i]
#         if (i < len(costList) - 2) and (costList[i+2] <= costList[i+1]):
#             i += 2
#         else:
#             i += 1
#     return cost

# print(minCost([1,100,1,1,1,100,1,1,100,1]))

#does not work for the case of
# [1, 10, 20, 30, 20, 10, 1]

def minCostClimbingStairs_1(cost):
    f1 = f2 = 0
    for x in reversed(cost):
        f1, f2 = x + min(f1, f2), f1
    return min(f1, f2)

print(minCostClimbingStairs_1([1,10,20,30,20,10,1]))

#convert to graph, then use min path length

