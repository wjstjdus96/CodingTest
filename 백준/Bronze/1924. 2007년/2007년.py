monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dayList = ["MON", "TUE", 'WED', 'THU', 'FRI', 'SAT',"SUN"]

month, day = map(int,input().split())

totDays = sum([monthList[i] for i in range(0,month-1)]) + day
answer = dayList[totDays % 7 - 1]

print(answer)