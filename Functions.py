
# def, name (no explicit return type) parens arg-list (names only) colon
def show_me(n, count):
    """Shows two arguments...
    """
# decorations have NO MEANING to python, but are permitted for external type checking tools
# def show_me(n: str, count: int) -> str:
    if type(n) == int:
        print("nice, I got a name as an int...? Really")
        # raise TypeError  # shorthand for raise TypeErro() i.e. make one and raise it...
        raise TypeError("silly, this should be a string", n)  # "throw" or sending an exception
    print("n is ", n)
    print("count is ", count)
    return "I'm done"

print(show_me.__doc__)  # intended for document generator tools...
show_me("Hello", 99)
try:
    print("about to violate type expectations")
    show_me(99, "Hello")
    print("still here")
# except:  # Processes *all failures*
# except TypeError:
except TypeError as t:
    print("it broke, with a type error", t)  # t picks up the tuple of initializer arguments

print("main flow still here")

import random
try:
    if random.random() > 0.5:
        raise ValueError("Bad Value")
    else:
        raise TypeError("Bad Type")
except (ValueError, TypeError) as e:
    print("That broke", e)

try:
    if random.random() > 0.5:
        raise ValueError("Bad Value")
    else:
        raise TypeError("Bad Type")
except TypeError as e:
    print("type error", e)
except ValueError as v:
    print("value error", v)

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# IF default is "expression" rather than literal, it is evaluated ONCE
def days_in_month(month, year=2020):
    if month in [9, 4, 6, 11]: return 30
    if month in [1, 3, 5, 7, 8, 10, 12]: return 31
    if month == 2: return 29 if is_leap(year) else 28
    raise ValueError('Bad month')

# named argument passing
print(days_in_month(year=2020, month=4))
print(days_in_month(month=4))

# varargs and keyword args
# NO FUNCTION OVERLOADING, use varargs, kwargs to simulate
def show_all(a, b, *many, **kwargs):
    print(f"a is {a}, b is {b}")
    for v in many:
        print(">", v)
    for t in kwargs.items():
        print(f">> {t[0]} = {t[1]}")

show_all(1, 2, "three", 4, [5, 6, 7], fruit="banana", spice="chilli")
show_all(1, 2, "three", 4, [5, 6, 7], fruit="banana", spice="chilli", a="bad")