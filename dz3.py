# Задание 1
# Реализуйте функцию count_letter, которая принимает список слов и некоторую букву и возвращает количество слов в списке, в которых эта буква встречается хотя бы один раз.

my_list = ['python', 'c++', 'c', 'scala', 'java']
my_letter = 'c'

def count_letter(my_list, my_letter):
    count_l = 0
    for word in my_list:
        if my_letter in word:
            count_l += 1
    return count_l

print(count_letter(my_list, my_letter))