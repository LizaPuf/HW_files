from pprint import pprint


cook_book = {}

with open('recipy.txt', encoding='utf8') as file:
    for line in file:
        dish_name = line.strip()
        ingredient_count = int(file.readline().strip())
        dish_list = []
        for _ in range(ingredient_count):
            ingredient_line = file.readline()
            ingredient_name, quantity, measure = ingredient_line.strip().split(' | ')
            quantity = int(quantity)
            ingredient_dict = {
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            }
            dish_list.append(ingredient_dict)
        cook_book[dish_name] = dish_list
        file.readline()

pprint(cook_book)