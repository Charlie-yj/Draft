result = 0

while True:
    num = int(input())
    if num >= 0:
        result = result + num
    elif num < 0:
        pass
        break

print(result)