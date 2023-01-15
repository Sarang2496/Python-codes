magic_no= 6

for n in range(101):
    if n == magic_no:
        print(n, "is the magic number") 
        break ## if the condition is true come out of the loop
    else: # no need to keep looping further stop looping once the statement is true
        print(n)