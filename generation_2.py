country = str(input('Are you Korean? (y/n)'))
year = int(input('What year were you born?'))
gen = None

if country == 'y':
    if year <= 1924:
        gen = 'The Greatest Generation'
    if year <= 1954:
        gen = 'The Silent Generation'
    if year <= 1963:
        gen = 'a baby boomer'
    if year <= 1980:
        gen = 'Generation X'
    if year <= 1996:
        gen = 'millennial'
    if year >= 1997:
        gen = 'Generatino Z'
elif country == 'n':
    if year <= 1924:
        gen = 'The greatest Generation'
    if year <= 1945:
        gen = 'The Silent Generation'
    if year <= 1964:
        gen = 'a baby boomer'
    if year <= 1980:
        gen = 'Generation X'
    if year <= 1996:
        gen = 'millennial'
    if year >= 1997:  
        gen = 'Generation Z' 

print(f"You're {gen}.")