# решение кодом здесь
num_list =[1, 2, 3, 4, 5]
num_shift = 2
new_list = []

new_list = num_list [-num_shift:] + num_list[:-num_shift]
print(num_list, num_shift, new_list)



'''

Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.

Input:

[1, 2, 3, 4, 5]

k = 3

Output: [4, 5, 1, 2, 3]

'''
