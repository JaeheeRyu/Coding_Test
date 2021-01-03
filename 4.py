# 짝홀 정렬 문제
# 테스트케이스 없는 문제 Wrong Answer 에러남
# 9/12

from collections import deque
a = [4,13,10,21,20]
ar = deque(a)
list_len = ar.popleft()
#순회하면서 짝수와 홀수를 정렬함
#짝수가 앞, 홀수가 뒤!
re_num = 0
eo_list = [i for i in ar if i%2==0]
n = len(eo_list)

for i in range(n):
    if ar[i] % 2 != 0:
        re_num += 1