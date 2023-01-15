class Enemy: # anything indented will be a part of class enemy
    life = 3
    def attack(self): # Self is using anything fom this own class ->  keyword self is filled in which means use something from this own class
        print("Ouuch!!!")
        self.life -=1
        # life -= life cannot be accessed 
    def life_check(self):
        if self.life<=0:
            print("Dead!")
        else:
            print(str(self.life) + " life left")

# before using anything we need to create an object from the class
# if we want to use inside the enemy class

enemy1 = Enemy() # object from enemy class
enemy1.attack()
enemy1.life_check()
enemy2 = Enemy()
enemy2.attack()
enemy2.attack()
enemy2.life_check()


# Enemy.attack() # need to create an object