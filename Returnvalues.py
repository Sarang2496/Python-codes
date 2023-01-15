def age_allowed(myage): ##stores the value -> The return keyword is to exit a function and return a value.
    g_age = (myage / 2)  + 7
    return g_age

limit= age_allowed(27)
limit_2= age_allowed(66)
print("The limit is ",limit)
print("The limit is ",limit_2)
