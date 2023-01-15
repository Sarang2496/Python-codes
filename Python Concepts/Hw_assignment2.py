ages =[]
for x in range(15,61):
    ages.append(x)

def age_limit():
    for a in ages:
        g_age = (a / 2)  + 7
        print("The limit for", a, "is",g_age)

age_limit()
