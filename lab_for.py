L = input().split(' ', 2) 
min = str(L[0])
max = str(L[1])

temp = input().split()


for i in temp:
    if min <= i <= max:
        print('Nothing to report')
    elif i == -999:
        break
    elif i < min or i > max:
        print('Alert!')
        break