#   s = [[..r..]..c..]
# start at [0][0]
# move using only right or down, to g
# for any two integers (r,c)
# return unique paths from s to g


# bijective counting??

def uniquePaths(r, c):
    s = [[0 for _ in range(r)] for _ in range(c)]
    
    for _r in range(r):
        for _c in range(c):
            if (_r == 2) or (_c == 2):
                s[_c][_r] = max(_r,_c)
