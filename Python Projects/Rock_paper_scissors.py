import random
def play():
    user = input("'r' for rock, 's' for sci, and 'p' for paper: ")
    computer = random.choice(['r','p', 's'])

    if user == computer:
        return 'Tie!'

    if is_win(user, computer):
        return 'You won!'

    return 'You lose!'

def is_win(player, opponent): # helper function

    if (player =='r' and opponent == 's' or (player =='s' and opponent == 'p')or (player =='p' and opponent == 'r') ):
        return True

print(play())


""" if user =='r' and computer == 'p':
        print(f"You win!!Computer chose {computer}")
    elif user =='p' and computer == 's':
        print(f"You lose!!Computer chose {computer}")
    elif user =='s' and computer == 'r':
        print(f"You lose!!Computer chose {computer}")
    elif user =='r' and computer == 's':
        print(f"You win!! Computer chose {computer}")
    elif user =='p' and computer == 'r':
        print(f"You win!!Computer chose {computer}")
    elif user =='r' and computer == 'p':
        print(f"You lose!! Computer chose {computer}")
    elif user =='s' and computer == 'p':
        print(f"You win!! Computer chose {computer}")
    else :
        print(f"Try another guess!!Computer chose {computer}")
play() """