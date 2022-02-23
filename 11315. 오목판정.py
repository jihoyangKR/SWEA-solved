import sys;sys.stdin = open("11315.txt")
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(input()) for _ in range(N)]
    result = 'NO'
    dr = [1, -1, 0, 0, -1, -1, 1, 1] # 굳이 모든 방향을 고민 할 필요가 없었다. 좌상, 우상, 상, 좌 델타는 이전 좌표에서 검사를 하기 때문.
    dc = [0, 0, 1, -1, -1, 1, -1, 1]
    for r in range(N):
        cnt = 0
        for c in range(N):
            for i in range(8):
                if lst[r][c] == 'o':
                    cnt = 1
                    nr = r + dr[i]
                    nc = c + dc[i]
                    while 0 <= nr < N and 0 <= nc < N and lst[nr][nc] == 'o':
                        cnt += 1
                        if cnt >= 5:
                            result = 'YES'
                            break
                        nr, nc = nr + dr[i], nc + dc[i]

    print(f'#{tc} {result}')