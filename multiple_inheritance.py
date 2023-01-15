class Mario:
    def move(self):
        print("I am moving!")

class Shroom():
    def eat_shroom(self):
        print("now, I am big!")

#create a class hwioch can inherit from both the classes

class BigMario(Mario, Shroom): # multiple inheritance
    pass # no functionality to it , but just need a line


bm = BigMario() # object from the class
bm.move()
bm.eat_shroom()



