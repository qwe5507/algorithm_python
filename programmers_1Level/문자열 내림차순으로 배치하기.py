# 프로그래머스 level 1문제
# 문자열 내림차순으로 배치하기
def solution(s):
    return "".join(sorted(s, reverse = True) )