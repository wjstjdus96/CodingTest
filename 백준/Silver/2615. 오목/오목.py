board = [list(input().split()) for _ in range(19)]
black = []
white = []

def get_winner(list):
    for i,j in list: 
        if [i, j-1] not in list and [i, j+2] in list and [i, j+3] in list and [i, j+4] in list and [i, j+5] not in list:
            return [i,j]
        if [i-1, j] not in list and [i+1, j] in list and [i+2, j] in list and [i+3, j] in list and [i+4, j] in list and [i+5, j] not in list:
            return [i,j]
        if [i-1, j-1] not in list and [i+1, j+1] in list and [i+2, j+2] in list and [i+3, j+3] in list and [i+4, j+4] in list and [i+5, j+5] not in list :
            return [i,j]
        if [i-1, j+1] not in list and [i+1, j-1] in list and [i+2, j-2] in list and [i+3, j-3] in list and [i+4, j-4] in list and [i+5, j-5] not in list:
            return [i+4, j-4]
    return False

for i in range(19):
    for j in range(19):
        if board[i][j] == "1":
            black.append([i+1,j+1])
        if board[i][j] == "2":
            white.append([i+1,j+1])

b = get_winner(black)
w = get_winner(white)

if b and not w:
    print("1")
    print(" ".join(map(str,b)))
if w and not b:
    print("2")
    print(" ".join(map(str,w)))
if not b and not w:
    print("0")