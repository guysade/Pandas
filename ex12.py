typeO = 0
donators = []
for x in range(2):
    name = input('Enter your name: ')
    year = input('Enter your year of birth: ')
    blood = input('Enter your blood type: ')

    donators.append({
        'name': name,
        'year': year,
        'blood': blood
    })

for donator in donators:
    if(donator['blood'] == 'o'):
        typeO = typeO + 1
print(typeO)