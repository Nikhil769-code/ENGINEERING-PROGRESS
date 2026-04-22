nums = [1,2,3,4,5,6,7]


# -------------------- Nested Loops --------------------

my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
# Creates pairs → (letter, number)
print(my_list)


# -------------------- Enumerate --------------------

my_list = []
for index, letter in enumerate('abcd'):
    my_list.append((index, letter))
# enumerate() → gives (index, value)
print(my_list)


# -------------------- Copy List --------------------

my_list = []
for val in nums:
    my_list.append(val)
# Copies elements from nums
print(my_list)


# -------------------- Square Values --------------------

my_list = []
for val in nums:
    my_list.append(val * val)
# Squares each number
print(my_list)


# -------------------- Filter Even Numbers --------------------

my_list = []
for val in nums:
    if val % 2 == 0:
        my_list.append(val)
# Keeps only even numbers
print(my_list)


# ==================== LIST COMPREHENSION ====================

my_list = [val * val for val in nums]
# Squares each number (compact version)
print(my_list)


my_list = [n for n in nums if n % 2 == 0]
# Filters even numbers (compact version)
print(my_list)


my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# Nested loop in one line → (letter, number)
print(my_list)
