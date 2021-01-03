# OK

from collections import deque
def minX(arr):
    # if min(tend)<0:
    #     return tend[len(tend)-1]-min(tend)
    # else:
    #     return tend[len(tend) - 1]
    ar = deque(arr)
    ar.reverse()
    tend = []
    if ar[0] < 1:
        num = 1
    else:
        num = ar[0] + 1
    for i in ar:
        num = num - i
        print(num, i)
        tend.append(num)
    if min(tend)<1:
        return tend[len(tend)-1]-min(tend)+1
    else:
        return tend[len(tend) - 1]