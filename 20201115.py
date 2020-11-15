def cal_round(num):
    if num % 2 == 0:
        return num//2
    else:
        return num//2+1
def solution(n,a,b):
    cnt = 0
    while(True):
        cnt += 1
        a = cal_round(a)
        b = cal_round(b)
        if a == b:
            break;
    return cnt
solution(8,4,7)