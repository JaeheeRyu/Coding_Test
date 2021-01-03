# 가장 작은 Swap 구하는 문제
# 테스트케이스 없는 문제 타임에러남
# 6/9

def maxDifference(nums):
    list_len = len(nums)
    re_list = []
    temp = -1
    breaker = False
    k = max(nums)-min(nums)
    for i in range(1,list_len):
        for j in range(i):
            if nums[j]<nums[i]:
                dif = nums[i]-nums[j]
                if dif > temp:
                    temp = dif
                if temp == k:
                    breaker = True
            else:
                breaker = True
        if breaker == True:
            continue
    return temp


def maxDifference(nums):
    list_len = len(nums)
    re_list = []
    temp = -1
    breaker = False
    try:
        for i in range(1,list_len):
            for j in range(i):
                if nums[j]<nums[i]:
                    dif = nums[i]-nums[j]
                    if dif > temp:
                        temp = dif
                else:
                    breaker = True
            if breaker == True:
                continue
        return temp
    except:
        return 99990