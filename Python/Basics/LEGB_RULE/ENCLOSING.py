x = 'global x '

def outer ():
    x = 'outer x '
# Same concept as Local and Global scope 
    def inner():
        nonlocal x  #V.IMP - Here we accesses x of outer() function and not through global x (There is a diffrence )
        x = 'inner x '
        '''Here the print statement intitially checks the local scope for x 
        but as x is not present therefore it checks the local scopes of any enclosing functions'''

        print(x)

    inner()
    print(x)

outer()