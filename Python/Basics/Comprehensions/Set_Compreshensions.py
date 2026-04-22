nums = [1,2,3,4,5,6,7,8,9]


# -------------------- Set Creation (Loop) --------------------

my_set = set()
for val in nums:
    my_set.add(val)
# Adds each element → removes duplicates automatically
print(my_set)


# -------------------- Set Comprehension --------------------

my_set = {n for n in nums}
# Compact way to create a set
print(my_set)


# -------------------- Generator (Function) --------------------

# Goal: yield n*n for each n in nums
def gen_func(nums):
    for val in nums:
        yield val * val
# yield → produces values lazily (one at a time)

generator = gen_func(nums)
# Creates a generator object 
# Note - You cannot print values from this object 


# -------------------- Generator Expression --------------------

generator = (n * n for n in nums)
# Compact generator (lazy evaluation, memory efficient)


# -------------------- Consuming Generator --------------------

# Generator can be iterated only once
for val in generator:
    print(val)