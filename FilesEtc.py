
# open takes filename, "mode", r-readonly, w-writeonly, r+ read and write, "b" for binary mode
f = open("data.txt", "r")
for line in f:  # includes newline :)
    print("> ", line, end="")
f.close()  # don't forget...

# "r" mode is default
# with... as... guarantees to close the file when this block ends
with open("data.txt") as f:
    for line in f:
        print(line, end="")

# methods used for autoclosing are __enter__ __exit___ :) read about contexts...
# can open multiple resources and have them all closed at once at the end :)
with open("data.txt") as f, open("copy.txt", "w") as output:
    for line in f:
        print(line, end="", file=output)




