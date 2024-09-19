L = input().split()
min = int(L[0]) 
max = int(L[1]) 

while True:
    num = int(input())
    if min <= num <= max:
        print('Nothing to report')
    elif num == -999:
        break
    elif num < min or num > max:
        print('Alert!')
        break