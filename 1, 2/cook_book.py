from pprint import pprint

dishes = 'recipes.txt'

with open(dishes, 'r', encoding='utf-8') as file:
    book = {}
    for line in file:
        dish_contents = []
        the_dish = line.strip()
        iterations = int(file.readline())
        for i in range(iterations):
            el = file.readline().strip().split(' | ')
            ingredient = el[0].strip()
            quantity = int(el[1])
            measure = el[2]
            dish_contents.append({'ingredient': ingredient, 'quantity': quantity, 'measure': measure})
        file.readline()
        book[the_dish] = dish_contents


def create_shop_list(dishes: list, person_count: int) -> dict:
    shop_list = {}
    for dish in dishes:
        for ingredients in book.get(dish):
            if ingredients['ingredient'] not in shop_list.keys():
                shop_list[ingredients['ingredient']] = {'measure': ingredients['measure'],
                                                        'quantity': ingredients[
                                                                      'quantity'] * person_count}
            else:
                shop_list[ingredients['ingredient']]['quantity'] += ingredients['quantity']
    return shop_list


pprint(create_shop_list(['Утка по-пекински', 'Фахитос'], 2))
