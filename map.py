income = [10, 34, 78] # list square brackets

def double_mopney(dollars):
    return dollars*2


new_income = list(map(double_mopney, income))

print (new_income)
# map(double_mopney, income) # takes two paramterts 