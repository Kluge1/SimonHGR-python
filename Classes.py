
class Stuff:
    pass

st = Stuff()

print(st, type(st))

st.name = "My name is stuff!"
st.address = "over here"

print(st.name, "I live", st.address)

class UsefulStuff:
    """
    Document your class!
    """
    # me, myself, I, aka "this" in many other languages, is called "self"
    # and is *never* implied i.e. x NEVER means self.x (like JavaScript...)
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):  # implements str() ... "readable"
        return f"I'm a UsefulStuff, name is {self.name} address is {self.address}"

    def __repr__(self):  # "precise form" / unambiguous ... used by "containers"
        return self.__str__()

    def get_address(self):
        return "Mr/Ms" + str(self.name) + " living at " + str(self.address)

    # WRONG
    def staticy_method(x):
        print("staticy method x is", x)

    @staticmethod  # function decorator (wrapper function)
    def real_static():
        print("real static method :)")

u = UsefulStuff("Fred", "over here")
print(u)  # delegates to __str__
print(str(u))

lu = [UsefulStuff("Fred", "here"), UsefulStuff("Jim", "there")]
print(lu)
print(u.get_address())

# NOT REALLY static...
UsefulStuff.staticy_method("banana")
# u.staticy_method("Banana")  # Breaks

UsefulStuff.real_static()
u.real_static()

class WithPrivatish:
    def __init__(self, a, b):
        self.a = a
        self.__b = b  # double underscore on variable is "kinda private"

wp = WithPrivatish(1, 2)
print(wp.a)
# print(wp.__b)  # "NAME MANGLED"
print(wp._WithPrivatish__b)  # consenting adults never do this... :)
wp.a = 99
print(wp.a)

# object, ommited, is implied...
class BaseClass(object):
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f"Base with a = {self.a}"

class SubClass(BaseClass):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def __str__(self):
        return f"I'a sub, with b={self.b} " + super().__str__()

sub = SubClass("A", "B")
print(sub)
