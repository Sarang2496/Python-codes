# writing a program is giving an instructions to follow 
# order needs to be followed whch is called "Threading"

# two different programs run at a time, for sending message 
# one programme has to send and another has to receive a message from the threading


# makes the program powerful and faster
# whenver we want to run anything concurrently adn at the same time wihtout depending on the other instruction is called threading

import threading 

# inherit from this class "threading.Thread"
class SarangsMessenger(threading.Thread):
    def run(self): 
        for _ in range(10): # no variable needed just want a loop to run 10 times 
            print(threading.currentThread().getName) # default property

x = SarangsMessenger(name='Just a random messenger') # built in property that we can give a name 
y = SarangsMessenger(name='hello')

x.start() # goes to class and searches run fucntion
y.start()