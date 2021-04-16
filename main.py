
cook_book = {}
with open('recept.txt', encoding='utf-8') as f:
    while True:
        name = f.readline().strip()
        if not name:
            break
        number = int(f.readline().strip())

        ingridients= []
        for _ in range(number):
            quantity: int
            ingredient_name: str
            measure: str

            leg = f.readline().strip()
            first_a = leg.index('|')
            a_split = leg[first_a:].split('|')
            a_split[0] = leg[:first_a] + a_split[0]
            a_split = [x.strip() for x in a_split]

            dic1 = {}
            dic1['ingredient_name'] = a_split[0]
            dic1['quantity'] = a_split[1]
            dic1['measure'] = a_split[2]
            ingridients.append(dic1)

        f.readline().strip()
        cook_book[name] = ingridients

for key, value in cook_book.items():
    print(f'{key} : \n{value}\n')


