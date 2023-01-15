# date,  item, price = ['December 23, 2015','Bread Gloves', 9.88] # fiorst second third values are allotted

# Unpacking variables -> *
# list -> []
# dictionary -> {} 
# number of variables mzst be equal to the number of items !!!!!!!!!!
#print(item) # unpacking the list 

# all items in middle variable and laszt item in last variable

def drop_first_last(grades):
    first, *middle, last = grades # unpack a list into variables using * 
    avg = sum(middle)/len(middle)
    print(avg)
    print(middle)

drop_first_last([65, 98, 87, 56, 35, 87])