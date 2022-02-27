# 맨 처음풀이.
# while문을 사용해서 원본lst와 대조lst가 차이 날 동안 연산을 진행했고
# 모든 lst요소를 바꾸는 형식으로 식이 길어졌다.
T = int(input())
for tc in range(1, T+1):
    data = input()
    N = len(data)
    data_lst = []
    for i in range(N):
        data_lst.append(int(data[i]))
    lst = [0] * N
    cnt = 0
    while lst != data_lst:
        for i in range(N):
            if data_lst[i] == lst[i]:
                continue
            else:
                cnt+=1
                if data_lst[i] == 1:
                    for j in range(i, N):
                        lst[j] = 1
                    continue
                else:
                    for j in range(i, N):
                        lst[j] = 0
                    continue
    print(f'#{tc} {cnt}')


# 굳이 while문을 쓸 필요도 없이 그냥 for문 내에서 if문을 돌리면서 전체 요소를 바꾸면 더 줄어든다.
T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input()))
    print(data)
    N = len(data)
    lst = [0] * N
    cnt = 0
    for i in range(N):
        if lst[i] != data[i]:
            for j in range(i, N):
                lst[j] = data[i]
            cnt += 1

    print(f'#{tc} {cnt}')

# 아예 전체 리스트를 바꾸는게 아닌 맨 앞부터 비교해가면서 바뀔 때만 cnt를 체크해주는 방법이 있다.
# 다른 친구의 idea
