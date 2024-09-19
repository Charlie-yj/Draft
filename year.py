y = int(input('Enter the year'))
a = y % 4
b = y % 100
c = y % 400


if a == 0:
    print(f'{y}는 윤년')
elif a != 0:
    print(f'{y}는 평년')
elif b == 0:
    print(f'{y}는 평년')
elif b != 0:
    print(f'{y}는 윤년')
elif c == 0:
    print(f'{y}는 윤년')
elif c != 0:
    print(f'{y}는 평년')   
