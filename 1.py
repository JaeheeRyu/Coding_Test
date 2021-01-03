#collision 문제임
#안날 것 같은데 남/테스트케이스 주어지지 않은 것은 못풀었음
#7/14

speed = [8,3,6,3,2,2,4,8,1,6]
pos = 7
#1번 이동시의 위치를 new에 저장
col = 0
temp = 0
Flag = True
new = [speed[i]+i for i in range(len(speed))]

while(Flag):
    for i in range(pos):
        if new[i] >= new[pos]:
            col += 1
    for i in range(pos+1,len(new)):
        if new[i]<=new[pos]:
            try:
                col += 1
                new = new[:i]+new[i+1:]
            except:
                continue
