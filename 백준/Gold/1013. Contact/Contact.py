n = int(input())

for _ in range(n):
    s = input()
    result = True

    while len(s) > 0:
        if s[:3] == '100':
            s = s[3:]
            while s[:1] == "0":
                s = s[1:]
            if len(s)==0:
                result=False
                break
            s = s[1:]
            while s[:1] == "1":
                if s[:3] == "100":
                    break
                else:
                    s = s[1:]
        elif s[:2] == "01":
            s = s[2:]
        else:
            result = False
            break
    print("YES" if result else "NO")