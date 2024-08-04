#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 17:00:56 2024

@author: dani
"""
    
#Acts as a weight converter    
def weight_converter():
    #Enters weight
    weight = float(input("Weight: "))
    #Asks if the weight is in kilograms or pounds
    #Type k for kilograms or l for pounds
    conversion = input("(K)g or (L)bs: ").lower()
    #Shows and converts the weight in lbs
    if conversion == "k":
        weight_kg = weight * 2.205
        print(f'Weight in Lbs: {weight_kg}')
    #Shows and converts the weight in kg
    if conversion == "l":
        weight_lb = weight / 2.205
        print(f'Weight in Kg: {weight_lb}')
    
weight_converter()