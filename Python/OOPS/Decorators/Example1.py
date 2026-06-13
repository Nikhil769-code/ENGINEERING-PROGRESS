# Closures  - They are basically Inner function that remembers/has access to variables
# of the local scope in which it was created , even after the outer function is done executing
# A Closure closes over the free variable of thier enviornment

def outer_fun(msg):
    message = msg

    def inner_func():
        print(message)
    
    return inner_func

hi_func = outer_fun('Hi')
hello_func = outer_fun('Hello')

hi_func()
hello_func()