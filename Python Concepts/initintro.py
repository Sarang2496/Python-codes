class Tuna:
    # this function is called by default whenver we call an object of this class
    def __init__(self) -> None: # instantiator initialize , whatever we write here is called when we call the object
        print("Just a test line!")
        pass
    def swim(self):
        print("I am swimming")

random = Tuna() ## object calling
random.swim()

