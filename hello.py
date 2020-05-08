# script-like structure top to bottom of file.
# PEP-8 coding standards

print('Hello Python " world')

# variables are created on initial assignment
x = 99
# variables are "pointers/references" untyped... But objects have type
print(x, type(x))
x = "Hello"
print(x, type(x))
x = 14e+3
print(x, type(x))
x = 1234567890123456789
print(x)
# number bases 0b binary, 0x hexadecimal, 0o
# python2 leading zeroes meant OCTAL (C, C++, Java!) REALLY BAD
x = 0b0101010
print(x, type(x))

x = 0o010
print(x, type(x))

x = "hello" + " world"
print(x)
x += str(99)  # no "autoconversion" during string concatenation
print(x)

print("Hello", "Fred", "how", "are", "you", 99, sep=":", end="ENDODFLINE\n")
print("On a new line")

x = "hello"
y = "bonjour"
msg = f"The word {x} translates to French as {y}"
print(msg)

print(x * 3)
# python uses "dictionaries" for namespaces
del x
# cannot print this any more. Does not exist!
# print(x)

x = 3
y = 2
print(type(x), type(y))
# int div by int => float!!!
print(x / y)
# int division is //
print(x // y)
import math
t = math.modf(x / y)
print(type(t), t)

f,w = t
print(f"fractional is {f} whole is {w}")
(f,w) = t
# destructuring assignment MUST have matching element counts..
# (f,) = t  # trailing comma, (always allowed) here necessary to indicate TUPLE OF ONE element
print("tuple item zero", t[0])
# but IMMUTABLE structures
# t[0] = "banana"

x = 1j
print(type(x), x, x**2)

# Lists
x = ["Fred", "Jim", "Sheila"]
print(type(x), x)
# access using square bracket subscripts
print(x[0])
# mutable...
x[0] = "Frederick"
print(x)
# boolean True, False, first letter caps
x.sort(reverse=True)
print(x)

dict = { "Fred" : "Jones", "Alan" : "Smith"}
print(dict, type(dict))
print(dict.get("Fred"))

x = "Hello"
y = "He"
y += "llo"
# == "content based" equality ONLY IF THE TYPE defines it :) __eq__ method :)
print("x == y?", x == y)
# identity with "is"
print("x is y?", x is y)
print("x is not y?", x is not y)
