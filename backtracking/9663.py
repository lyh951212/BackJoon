# 백트래킹 대표문제 1
# n queen
import sys
input = sys.stdin.readline
n = int(input())
answer = 0
chess = [0]*15

def IsPromising(x):
    for i in range(x): 
        # 열이 같거나 대각선이 같으면 false
        # 대각선이 같은경우는 두 좌표에서 행 - 행 = 열 - 열 이 같으면 두개는 같은 대각선상에 있다.
        if chess[x] == chess[i] or abs(chess[x] - chess[i]) == x - i: 
            return False 
    return True
    
def BackTracking(rowPos):
    global answer
    global n
    if rowPos == n:
        answer += 1
        return
    
    for col in range(n):
        chess[rowPos] = col
        if IsPromising(rowPos):
            BackTracking(rowPos+1)
 
BackTracking(0)               
print(answer)