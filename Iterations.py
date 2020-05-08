x = 4
# simple while, as expected?
while x > 0:
    print(x)
    x -= 1

# foreach, forof, forin... kind of thing
# Anything "iterable", including lists :)
for x in ["FRed", "Jim"]:
    print(x)

for x in enumerate(["FRed", "Jim"]):  # enumerate creates tuples with index
    print(x[0], x[1])

# range takes initial, EXCLUSIVE end, and increment
for x in range(0, 20, 4):
    print(x)

print(range(0))
print(type(range(0)))

# "either break, or else..."
for x1 in range(0, 10):
    import random
    if random.random:
        break
    print(x1)
else:
    print("Hello???")  # "normal" completion (NOT break)

print("finished, x1 is", x1)

