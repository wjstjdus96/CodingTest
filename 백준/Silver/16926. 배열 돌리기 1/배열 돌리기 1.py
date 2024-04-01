n,m,r = map(int,input().split())
arr = [list(input().split()) for _ in range(n)]

# 한껍데기씩 떼다
def decomposite(i):
    one_line = []
    right = []
    left = []
    bottom = []
    for item in arr[i][i:m-i]:
        one_line.append(item)
    for j in range(i+1,n-i-1):
        left.append(arr[j][i])
        right.append(arr[j][m-1-i])
    one_line += right
    for item in arr[n-i-1][i:m-i]:
        bottom.append(item)
    one_line += bottom[::-1]    
    one_line += left[::-1]
    return one_line

# 이동시키다
def move(line,num):
    new_line = ["" for _ in range(len(line))]
    for idx, item in enumerate(line):
        new_idx = idx-(num%len(line))
        if new_idx < 0:
            new_idx += len(line)
        new_line[new_idx] = item
    return new_line

# 배열에 재조립시키다
def reassemble(new,start):
    row_num = m - 2*(start) #2개
    col_between_num = n - 2*(start) -2 #0개
    arr_i = start
    arr_j = start
    for i in range(0,len(new)):
        if i == 0:
            arr_j = start
            arr_i = start
            arr[arr_i][arr_j] = new[i]
            continue
        if i+1 <= row_num:
            arr_j += 1
        if i+1 > row_num and i+1 <= row_num+col_between_num:
            arr_i += 1
        if i+1 == row_num+col_between_num + 1:
            arr_i += 1    
        if i+1 > row_num+col_between_num + 1 and i+1 <= 2*row_num+col_between_num:
            arr_j -= 1
        if i+1 > 2*row_num+col_between_num:
            arr_i -= 1
        arr[arr_i][arr_j] = new[i]
        
for i in range(min(n, m)//2):
    line = decomposite(i)
    newArr = move(line,r)
    reassemble(newArr, i)
        
for i in arr:
    print(" ".join(i))