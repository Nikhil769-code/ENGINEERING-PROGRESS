x = 'global x '

import builtins  
# builtins:
# - Contains all default Python functions (min, max, print, etc.)


# -------------------- Avoid Overwriting Built-ins --------------------

def my_min():
    pass 
# Defining a function named like a built-in (e.g., min) can override it
# This should be avoided → it can break expected behavior


# print(dir(builtins))
# Shows all built-in names available in Python


# NOTE:
# Python resolves names using LEGB rule:
# Local → Enclosing → Global → Built-in
# If you override a built-in in global scope, Python will use that first


m = min([5,4,3,2,1])
# Uses built-in min() (since we did NOT override it)
print(m)


# -------------------- Global Keyword --------------------

def test(z):
    global x  
    # Refers to global variable 'x' (not creating a new local one)

    x = 'local y '
    # Modifies global 'x'

    print(x)
    print(z)


test('local_z')

print(x)
# Global x is now modified by function

