t = int(input())

def func_AC(p,x):
    start, end = 0, len(x)
    is_reversed = False

    for func in p:
        if func == "R":
            is_reversed = not is_reversed
        if func == "D":
            if end == 1 and x[0] == "":
                return "error"
            if start == end:
                return "error"
            if not is_reversed:
                start += 1
            if is_reversed:
                end -= 1
    x = x[start:end]
    if is_reversed:
        x = x[::-1]
    return "[" + ",".join(x)+"]"
    
for _ in range(t):
    p = input()
    n = int(input())
    x_list = input()[1:-1].split(",")
    print(func_AC(p,x_list))