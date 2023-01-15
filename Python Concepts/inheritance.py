# whatever is passed on to child from your parents or someone else

class Parent():

    def print_last_name(self):
        print("Bilwankar")
    
class Child(Parent): # type the name of the class from which you want the variables and the objects from 
    def print_first_name(self):
        print("Sarang")
    
    # It overwrites the function of the parent class with the same function and the same exact name and then it will overwrite the function 
    def print_last_name(self):
        print("Müller")

bucky = Child()
bucky.print_first_name()
bucky.print_last_name()

