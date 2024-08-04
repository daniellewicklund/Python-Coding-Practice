#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 16:59:01 2024

@author: dani
"""

#Acts as a program for a hospital
def hospital_check_in():
    #Check-ins a patient named John Smith
    patient = input("Enter your name: ")
    #Asks for his age, 20
    age = input("Enter your age: ")
    #Verifies his new patient status
    new_patient = True
    #Declares and prints the variables and stored values
    print(f'Patient: {patient}, Age: {age}, INew Patient: {new_patient}')
    
hospital_check_in()