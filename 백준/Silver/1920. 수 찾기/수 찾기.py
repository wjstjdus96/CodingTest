n = int(input())
n_lst = sorted(list(map(int,input().split())))
m = int(input())
m_lst = list(map(int,input().split()))

for i in m_lst:
    left = 0
    right = len(n_lst)-1
    is_exist = False
    while left <= right:
        mid = (left+right)//2
        if n_lst[mid] == i:
            is_exist = True
            break
        elif n_lst[mid] > i:
            right = mid - 1
        else:
            left = mid + 1
    print(1 if is_exist else 0)