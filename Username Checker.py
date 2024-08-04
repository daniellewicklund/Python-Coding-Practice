#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 20:50:39 2024

@author: dani
"""

def username_checker():
    username = input("Insert your username: ")
    name_checker = len(username)
    if name_checker < 3:
        print("Try again.")
        print("Your username must be at least 3 characters long.")
    elif name_checker > 50:
        print("Try again.")
        print("Your username cannot be more than 50 characters long.")
    else:
        print("Your username looks great!")
        
username_checker()