#OK


def maxShared(friends_nodes, friends_from, friends_to, friends_weight):
    con = list(zip(friends_from,friends_to))
    con1 = []
    for i in range(len(con)):
        if con[i][0] > con[i][1]:
            con[i] = (con[i][1],con[i][0])
    new_con = set(con)
    re = []
    for i in new_con:
        re.append(con.count(i))
    m = max(re)
    re2=[]
    for i in new_con:
        if con.count(i) == m:
            re2.append(i[0]*i[1])
    return max(re2)