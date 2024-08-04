#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 20:50:17 2024

@author: dani
"""

def credit_checker():
#Shows the price of a house at $1M.
    house_price = float(1000000)
    buyer_credit = input("Do you have good credit?: ").lower()
    #If the buyer has good credit
    if buyer_credit == "good":
        #Calculates the amount to be put down at 10%
        amount = house_price * .10
        #Prints the down payment
        print(f'Put down 10%: ${amount}')
    #Otherwise
    else: 
        #Calculates the amount to be put down at 20%
        amount = house_price * .20
        #Prints the down payment
        print(f'Put down 20%: ${amount}')
    
credit_checker()
