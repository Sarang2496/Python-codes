first = ['Bucky', 'Tom', 'Tailor']
last = ['roberts', 'hanks', 'swift']

names = zip(first, last) # zip function 

# tuples are like "()"
# list are like []
# dict are given by this {}
# it makes a list of tuples
for a,b in names:
    print(a,b)