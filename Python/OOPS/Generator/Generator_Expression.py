# Generators 
nums = [1,2,3,4,5]

# This is a basic Function That squares up the numbers of a list 
def sqaure_numbers(nums):
    temp =[]
    for i in nums:
        temp.append(i*i)
    return temp 

# Same Function But using List Comprehension 
result = [val*val for val in nums]


# This is a Generator That yeilds the required number (One At a time )
def gen_square(nums):
    for val in nums:
        yield (val*val)

# Same Generator but Using Comprehension ( Used ()  brackets to create a generator)
result = (val*val for val in nums)


# print(gen_square(nums))   #This Line Just Prints the memory address(or object ID)
result = gen_square(nums)

print(list(val for val in result)) #This Statement exhaustes the generator first and then prints all the elements as a list 
# Note - Converting the generator into a list will make you loose performance 


# This Loop prints the elements of generator one by one 
for num in result:
    print(num)





