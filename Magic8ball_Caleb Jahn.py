# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 09:33:14 2024

@author: Caleben Jahn
"""

import random

fortune=("nah", "it's no use", "tough", "not gonna happen dude", "I'm not gonna stop you", "go for it", "heck yeah", "maybe ¯\_(ツ)_/¯", "YES YES YES", "live and learn")

print("Option 1: Print all your fortunes")

print("Option 2: Get a specific fortune")

print("Option 3: Ask your questions")


option=input("please choose from options 1, 2, or 3: ")

if option == "1":
    print("Here are your possible fortunes.")
    for index, value in enumerate(fortune):
        print(f'{index}) {fortune[index]}')

elif option == "2":
    choice= input("please pick a number 0-9: ")
    
    choice = int(choice)
    
    print(fortune[choice])

     
elif option == "3":
    question= input("ask your questions, recieve your answers: ")
    number = random.randrange(len(fortune))
   
    print(fortune[number])

else:
    print("guess you don't want your fortune. You're boring")
    
    
    
    
    
