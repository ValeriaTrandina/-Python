# Задание 1

f = open('new_file.txt', 'w')
a = input('Введите текст \n')
while a:
    f.writelines(a)
    a = input('Введите текст \n')
    if not a:
        break
f.close()

f = open('new_file.txt', 'r')
text = f.readlines()
print(text)
f.close()











