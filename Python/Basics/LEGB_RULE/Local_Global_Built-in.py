x = 'global x '
import builtins 

def my_min():
    pass 
# You should never overwrite built-ins when you are using them otherwise you'll get an error 

# print(dir(builtins))
''' Python found the min function in the global scope before it 
fellback to the local scope (That's the reason of error) ''' 
m =min([5,4,3,2,1])
print(m)


def test(z):
    global x    # IMP (This uses the global value of x )
    x = 'local y '
    print(x)
    print(z)

test('local_z')
print(x)
