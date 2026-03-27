def rec_equalcosteditdist(str1 : str, str2 : str) -> int:
    if not str1:
        return len(str2)
    if not str2:
        return len(str1)
    
    if str1[-1] == str2[-1]:
        return rec_equalcosteditdist(str1[:-1], str2[:-1])
    
    return min(
        1+ rec_equalcosteditdist(str1, str2[:-1]), 
        1+ rec_equalcosteditdist(str1[:-1], str2), 
        1+ rec_equalcosteditdist(str1[:-1], str2[:-1])
    )


def dp_equalcosteditdist(str1 : str, str2 : str) -> int:
    # create table to store sub problems
    # dp = [[0 for x in range(len(str2) + 1)]]


    # for index1, char1 in enumerate(str1):
    #     if index1 < len(str2):
    #         for index2, char2 in enumerate(str2[index1:]):
    #             if index1 == index1+index2 and char1 == char2:
    #                 continue
                # cost += 1
    return -1

    # return cost

# replace

# ABCDE
# ABDDE

# insert

# ABCDE
# ABCFDE

# remove

# ABCDE
# ABCE