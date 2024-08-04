#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 20:53:57 2024

@author: dani
"""

#Uses a while loop to build this guessing game
def guessing_game():
    #Sets the secret number to 9
    secret_number = 9
    guess_count = 0
    #Gives the user 3 chances to make a guess
    guess_limit = 3
    while guess_count < guess_limit:
        #Asks the user to make a guess
        user_guess = int(input("Guess: "))
        guess_count += 1
        if user_guess == secret_number:
            #Tells the user that they won, if they are successful
            print("You won!")
            break
        else:
            #Tells the user that they failed, if they are unsuccessful
            print("You failed!")
       
guessing_game()
