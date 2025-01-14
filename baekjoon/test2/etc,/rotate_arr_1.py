'''
SW 역량 테스트 준비 - 문제 2

16926번 배열돌리기 1
시뮬레이션
시간초과: deepcopy때문인가? 아님 for문 때문인가? 이유를 모르겠다..;
'''
from copy import deepcopy as dc
N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def rotate(i,n,m):
    global arr 
    r_arr = dc(arr)

    #행
    for x in range(n): 
        arr[i+x+1][i] = r_arr[i+x][i]
        arr[i+n-x-1][i+m] = r_arr[i+n-x][i+m]
    #열
    for y in range(m): 
        arr[i+n][i+y+1] = r_arr[i+n][i+y]
        arr[i][i+m-y-1] = r_arr[i][i+m-y]

    
for _ in range(R):
    #회전 시, 움직이는 행열수 변화 
    n_num = N-1
    m_num = M-1 

    for i in range(min(N,M)//2):
        rotate(i,n_num,m_num)
        n_num-=2
        m_num-=2

#출력
for ar in arr:
    print(*ar)