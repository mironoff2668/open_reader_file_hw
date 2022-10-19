from pprint import pprint
#
# with open('recipes.txt', 'r', encoding = 'utf8') as cook_dict:
#     cook_book = {}
#     for line in cook_dict:
#         dish_name = line.strip()
#         ingredients = []
#         for i in range(int(cook_dict.readline())):
#             ingredient = cook_dict.readline().split(' | ')
#             ingredients.append({'ingredient_name' : ingredient[0], 'quantity' : ingredient[1], 'measure' : ingredient[2].split()})
#         cook_book[dish_name] = ingredients
#         cook_dict.readline()
# print(cook_book)
#
#
# def get_shop_list_by_dishes(dishes, person_count):
#     shop_list = {}
#     for dish_name in dishes:
#         if dish_name in cook_book:
#             for values in cook_book[dish_name]:
#                 if values['ingredient_name'] in shop_list:
#                     shop_list[values['ingredient_name']] += int(values['quantity']) * person_count
#                 else:
#                     shop_list[values['ingredient_name']] = {'measure' : values['measure'], 'quantity' : int(values['quantity']) * person_count}
#         else:
#             print(f'Такого блюда {dish_name} в меню нет')
#
#     print(shop_list)
# get_shop_list_by_dishes(['Омлет'], 3)
#
#
#
#
# with (open('1.txt', encoding = 'utf8') as first_text,
# open('2.txt', encoding = 'utf8') as second_text,
# open('3.txt', encoding = 'utf8') as third_text):
#
# with open('input.txt', encoding='utf8') as f_in, open('output.txt', 'w', encoding='utf8') as f_out:
#     for i in list(map(str.split, sorted(f_in.readlines()))):
#         f_out.write('{} {} {}\n'.format(i[0], i[1], i[3]))
#


text_list = []

file_names = ('1.txt', '2.txt', '3.txt')
for file_name in file_names:
    with open(file_name, encoding='utf-8') as text_files:
        text_files_list = text_files.readlines()
        txt_all_list = [len(text_files_list), file_name, text_files_list]
        text_list.append(txt_all_list)
text_list.sort()

with open('new_file.txt', 'w', encoding='utf-8') as new_file:
    for el in text_list:
        new_file.write(f'{el[1]}\n')
        new_file.write(f'{el[0]}\n')
        new_file.write(f'{" ".join(el[2])}\n\n')