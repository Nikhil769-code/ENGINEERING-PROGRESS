nums = [1,2,3,4,5,6,7,8,9]

my_set = set()
for val in nums:
    my_set.add(val)
print(my_set)

# # SET COMPREHENSIONS

my_set = {n for n in nums}
print(my_set)



# GENERATOR EXPRESSIONS
#  I want to yield 'n*n' for each 'n' in nums

def gen_func(nums):
    for val in nums:
        yield val*val
generator = gen_func(nums)


generator = (n*n for n in nums)

for val in generator:
    print(val)


