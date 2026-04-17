nums = [1,2,3,4,5,6,7]

# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter,num))
# print(my_list)

my_list = []
for index,letter in enumerate('abcd'):
    my_list.append((index,letter))
print(my_list)

# my_list = []
# for val in nums:
#     my_list.append(val)
# print(my_list)

# my_list = []
# for val in nums:
#     my_list.append(val*val)
# print(my_list)

# my_list =[]
# for val in nums:
#     if val%2==0:
#         my_list.append(val)
# print(my_list)

#  LIST COMPREHENSION 

# my_list = [val*val for val in nums ]
# print(my_list)

# my_list = [n for n in nums if n%2==0]
# print(my_list)

# my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
# print(my_list)