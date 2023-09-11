

def give_instructions():
    print('''/n Wordle is a word guessing game.
        You have 5 attempts
        (C) means the letter is in word and the right place
        (WP) means the letter is in the word but is 9n the worng place
        (Nt) means the letter is not there in the word
        Good Luck Fellow Gamer :3
        ''')
give_instructions()


import random

words = ["this", "late", "pink", "five", "goat", "poop", "fart", "cats", "yell", "able", "ship", "rift", "read", "does", "wind"]


hidden_word = random.choice(words) 

attempt = 5


def check_word(guess):

        if hidden_word == guess:
            print("Congrats!! You did it.")
            return True
        else: 
            result = ""
            for i,j in zip(guess, hidden_word):
                if i==j:
                    result = result + "(C)"    
                elif i in hidden_word:
                    result = result + "(WP)"
                else: 
                    result = result + "(NT)"
            print (result)
            return False
        
def main_loop():
    attempt = 5
    while attempt > 0:
        guess = input("enter a four letter word: ")
        if check_word(guess):
            break
        else:
            attempt -= 1 #attempt = attempts -1 
            print (f"You have {attempt} attempts left") 
    else: 
         print("GAME OVER HAHAHAHAHAHAHAHHAHAHAH")

main_loop()

check_word("five") 
