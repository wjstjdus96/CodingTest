from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    p = list(map(int, input().split()))
    docs = deque((idx, val) for idx, val in enumerate(p))
    order = 0

    while True:
        idx, pri = docs[0]
        pri_max = max(docs, key=lambda x: x[1])[1]

        if pri < pri_max:
            docs.append(docs.popleft())
        else:
            order += 1
            docs.popleft()
            if idx == m:
                print(order)
                break