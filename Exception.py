# tuna = int(input("Please enter a number!\n"))

while True:
    try:
        number = int(input("Please enter a number!\n"))
        print(10/number)
        break
    except ValueError: # this is a type of exception
        print("Enter a number!")
    except ZeroDivisionError:
        print("Dont pick a zero!")
    except:
        break
    finally:
        print("Loop complete")

