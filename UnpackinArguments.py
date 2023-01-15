def health_calc(age, apples_ate, cigs_smoked):
    answer = (100 -age) + (apples_ate*3.5) -(cigs_smoked*2)
    print(answer)


data = [26, 35,20]

health_calc(data[0], data[1], data[2]) 
health_calc(*data)  # unpacking arguments but in order
