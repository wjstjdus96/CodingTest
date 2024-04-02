n = int(input())
switch = input().split()
per_n = int(input())

def turn_switch(s):
    if s == "0":
        return "1"
    if s == "1":
        return "0"

def change_male(num):
    for i in range(n):
        if (i+1) % num == 0:
            switch[i] = turn_switch(switch[i])

def change_female(num):
    switch[num-1] = turn_switch(switch[num-1])
    left, right = num-2, num
    while left >= 0 and right < n:
        if switch[left] == switch[right]:
            switch[left] = turn_switch(switch[left])
            switch[right] = turn_switch(switch[right])
        else:
            break
        left -= 1
        right += 1
        
for _ in range(per_n):
    per = input().split()
    if per[0] == "1":
        change_male(int(per[1]))
    if per[0] == "2":
        change_female(int(per[1]))

for i in range(0, len(switch), 20):
    print(*switch[i:i+20])