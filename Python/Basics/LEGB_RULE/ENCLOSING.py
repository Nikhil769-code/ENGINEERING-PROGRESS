x = 'global x '


def outer():
    x = 'outer x '
    # Local to outer()

    # -------------------- Enclosing Scope --------------------

    def inner():
        nonlocal x  
        # Refers to variable from enclosing function (outer), NOT global

        x = 'inner x '
        # Modifies x inside outer()

        # Variable lookup follows LEGB:
        # Local → Enclosing → Global → Built-in

        print(x)  # Prints 'inner x'

    inner()
    print(x)  
    # Prints modified value from inner() → 'inner x'


outer()