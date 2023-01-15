def gender(sex="Unknown"):  ## parameter is  given sex and default  value is Unknown
    if sex is "m":
        sex = "Male"
        #print("he is a male!")
    elif sex is "f":
        sex = "Female"
        #print("she is a female!")
    print(sex)
gender("m")
gender("f")
gender()


