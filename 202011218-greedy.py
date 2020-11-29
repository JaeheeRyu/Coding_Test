def solution(n, lost, reserve):
    cnt = 0
    for i in range(1,n+1):
        if i not in lost:
            cnt += 1
        elif i in reserve:
            cnt += 1
            reserve.remove(i)
            lost.remove(i)

    for lo in lost:
        print(lo)
        if lo-1 in reserve:
            reserve.remove(lo-1)
            cnt += 1
        elif lo+1 in reserve:
            reserve.remove(lo+1)
            cnt += 1
    answer = cnt
    return answer
solution(5, [3,5], [4])