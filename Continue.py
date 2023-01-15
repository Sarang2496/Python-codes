numbers = [11, 22, 3, 44, 55, 66 ,77, 88]

print("Numbers still available!")
for n in range(1,20):
    if n in numbers:
        continue # whenever somethings is after it just skip it and go to the the loop 
    print(n)