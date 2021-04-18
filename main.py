
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

def get_shop_list_by_dishes(dishes, person_count):

    dic2 = []
    dic3 = []
    resultdict = []
    for key, values in cook_book.items():
        for val in dishes:
            if key == val:
                for df in values:
                    dic2.append(df)

    for dish in dic2:
        for dish2, val in dish.items():

            if dish2 == 'quantity':
               d1 = dict.fromkeys(['quantity'], int(val)* person_count)
            if dish2 == 'measure':
               d = dict.fromkeys(['measure'], val)
               d.update(d1)
               dic3.append(d)

    x =0
    for dish in dic2:
        for dish2, val in dish.items():

            if dish2 == 'ingredient_name':
                d = dict.fromkeys([val], dic3[x])
                resultdict.append(d)
        x += 1

    for dish_per in resultdict:
        for dish in dish_per:
            print(f'{dish}: {dish_per[dish]}')

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2)


import os
f = os.listdir(path="hw")
print()
print(f)