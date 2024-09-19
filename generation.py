y = int(input('What year were you born?'))

gen = None

if y <= 1924:
    gen = 'The Great Generation'
elif y <= 1925:
    gen = 'The Silent Generation'
elif y <= 1964:
    gen = 'a baby boomer'
elif y <= 1980:
    gen = 'Generation X'
elif y <= 1996:
    gen = 'a millennial'
else:
    gen = 'Generation Z'

print(f"You're {gen}.")