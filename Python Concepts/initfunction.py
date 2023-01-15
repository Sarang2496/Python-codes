class Enemy:
    def __init__(self,x) -> None: # some has less and some has more energy # need to passs a value 
        self.energy = x # store in variable 
        pass
    def get_energy(self):
        print(self.energy)
    
# two differnet objects of same class
jason = Enemy(5)
sandy = Enemy(18)

jason.get_energy()
sandy.get_energy()
