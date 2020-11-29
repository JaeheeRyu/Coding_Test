def quick_sort_cache(seq):
    if len(seq) < 2:
        return seq
    ipivot = len(seq) // 2  # 피벗 인덱스
    pivot = seq[ipivot]  # 피벗

    before = [x for i, x in enumerate(seq) if x <= pivot and i != ipivot]
    after = [x for i, x in enumerate(seq) if x > pivot and i != ipivot]
    return quick_sort_cache(before) + [pivot] + quick_sort_cache(after)

def solution(array, commands):
    answer = []
    for i in commands:
        sorted_list = quick_sort_cache(array[i[0]-1:i[1]])
        print(sorted_list)
        answer.append(sorted_list[i[2]-1])
    return answer

solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])