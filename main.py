
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

    counter =0
    for dish in dic2:
        for dish2, val in dish.items():

            if dish2 == 'ingredient_name':
                d = dict.fromkeys([val], dic3[x])
                resultdict.append(d)
        counter += 1

    for dish_per in resultdict:
        for dish in dish_per:
            print(f'{dish}: {dish_per[dish]}')

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2)


import os
os.chdir(path="hw")
list_of_files = os.listdir(path=".")
dic4 = []
x = 0
d ={}

for _ in range(3):
 with open(list_of_files[x], encoding='utf-8') as f:
    lines = 0
    for line in f:
     lines = lines + 1
     d2 = dict.fromkeys([list_of_files[x]], lines)
     d.update(d2)
 x +=1
dic4.append(d)

sorted_dict = {}
for key1 in dic4:
    sorted_values = sorted(key1.values())
    for i in sorted_values:
        for k in key1.keys():
            if key1[k] == i:
                sorted_dict[k] = key1[k]
                break

with open("final.txt", "w", encoding='utf-8') as file:
    for key, values in sorted_dict.items():
      file.write(f'Имя файла: {key}\n'
                 f'Количество строк в нем:  {values}\n')