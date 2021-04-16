# Задание 4

#rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

tr = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_list = []
result = []
try:
    file_obj = open("new_file_6.txt", 'r')
    for line in file_obj:
        tokens = line.split(" - ")
        print(tokens)
        if tokens[0] in tr:
            word = tr[tokens[0]]
            result.append(word +' - '+ tokens[1])
    print(result)
except IOError:
    print('Ошибка')
finally:
    file_obj.close()

try:
    file_input = open("new_file_6.txt", "w")
    file_input.writelines(result)
except IOError:
    print('Ошибка')
finally:
    file_input.close()