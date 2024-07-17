from pprint import pprint


def my_cook_book():
    with open('recipes.txt', encoding='utf-8') as f:
        cook_book = {}
        for txt in f.read().split('\n\n'):
            name, _, *args = txt.split('\n')
            tmp = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                tmp.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = tmp
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in my_cook_book()[dish]:
            if ingredient['ingredient_name'] in shop_list:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
            else:
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                            'quantity': ingredient['quantity'] * person_count}
    return shop_list


pprint(my_cook_book())
print()
pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
print()


def line_counter(files):
    total_line_count = {}
    for file in files:
        with open(file, encoding='utf-8') as f:
            line_count = sum(1 for line in f)
        total_line_count[file] = line_count
    while total_line_count:
        target_grade = min(total_line_count.values())
        keys = list(total_line_count.keys())
        index = list(total_line_count.values()).index(target_grade)
        key = keys[index]
        write_to_file('4.txt', key)
        write_to_file('4.txt', str(target_grade))
        with open(key, 'r', encoding='utf-8') as f:
            data = list(f)
            write_to_file('4.txt', ''.join(data))
        total_line_count.pop(key)


def write_to_file(file, text):
    with open(file, 'a', encoding='utf-8') as f:
        f.write(text + '\n')


line_counter(['1.txt', '2.txt', '3.txt'])
