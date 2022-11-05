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

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        for ingr_dict in cook_book[dish]:
            ingredient_name = ingr_dict['ingredient_name']
            ingredient_quantity = ingr_dict['quantity']
            total_quantity = person_count * ingredient_quantity
            if ingredient_name in result:
                result[ingredient_name]['quantity'] += total_quantity
            else:
                product_dict = {
                    'measure': ingr_dict['measure'],
                    'quantity': total_quantity
                }
                result[ingredient_name] = product_dict
    return result


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2))
