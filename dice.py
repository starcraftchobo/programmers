'''
주사위 다 돌려서
승수가 가장 많은 경우를 쏙
오름차순으로
1) 주사위 개수가 다르다
2) 주사위 눈금 고르기 구현 - 재귀로 해야겠어
    1) 주사위와 눈금 하나를 고른다
    2) 넘겨주고 또 주사위랑 눈금 하나 고른다
    3) 주사위 더 없으면 리턴한다.
3) 맞다이 붙이기 패 승 중 max값 골라서 방향
'''
def pick_num(combi, current, hap):          # (1, 2, 3)
    for i in range(6):         # 주사위 골라
        if current == N-1:
            lst.append(hap+dice[combi[current]][i])
        else:
            new_hap = hap + dice[combi[current]][i]
            pick_num(combi, current+1, new_hap)


     # for num in pick[0]:
     #     if current == how_many:
     #         lst.append(hap)
     #     num+ pick_num(current+1)
    pass

from itertools import combinations
dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
N = len(dice)//2
# print(list(combinations(range(len(dice)), len(dice)//2)))
picks = list(combinations(range(len(dice)), len(dice)//2))       # 주사위 고르는 경우


cases = []
for pick in picks:
    lst = []                # 눈금 합 담을 리스트
    pick_num(pick, 0, 0)
    cases.append(lst)
print(N,cases)
