x = 99

# indentation matters!!!
# "block scoping" is DETERMINED BY indentation.
# level MUST BE CONSISTENT!!!
# NEVER allow a TAB character to be in your file!!!
# use "any number of spaces" (consistently) as long as it's 4 :)
if x > 50:
    print("x is fairly big")
    # print("yup, it's big alright")  # THIS fails because of extra indent!

    print("be consistent")
# "truthiness"
if x:
    print("yup, x is 'True'")

print("zero is", bool(0))
print("1 is", bool(1))
print("[1] is", bool([1]))
print("[0] is", bool([0]))
print("[] is", bool([]))

# single line, yeah, sometimes, but stuck there...
# semicolon can be used to separate on a single line
# DON'T you'll get laughed at.
if x > 100:
    print("Really big")
else:
    print("not huge"); print('not big')

# works, but don't :)
# if x < 50:
#     print("small")
# else:
#     if x < 100:
#         print("fairly small")
#     else:
#         print("fairly big")

if x < 50:
    print("small")
elif x < 100:
    print("fairly small")
    y = "That's a small value"
else:
    print("fairly big")

print(y)

x = 200
msg = "x is pretty small" if x < 100 \
    else "x is faily large"
print(msg)

# No SWITCH...
