import sys
sys.stdin = open("input.txt", "r")
 
T = int(input())
 
for test_case in range(1, T + 1):
    text_num = int(input())
    sco = list(map(int, input().split()))
    co = [0] * 101
     
    for s in sco:
        co[s] += 1
    max_count = max(co)
    an = 0
     
    for score in range(100, -1, -1):
        if co[score] == max_count:
            an = score
            break
    print(f'#{text_num} {an}')