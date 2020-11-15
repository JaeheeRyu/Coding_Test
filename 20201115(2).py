def solution(s):
    words = s.lower().split(" ")
    words = [i.capitalize() for i in words]
    answer = " ".join(words)
    return answer

solution("3people unFollowed me")
solution("for the last week")