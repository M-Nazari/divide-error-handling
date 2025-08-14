# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 11:47:27 2025

@author: Mahjoobe Nazari

this is just a try- except error handeling for a division function
"""

def divide(a, b):
    try:
        result = a / b
        return result
    
    except ZeroDivisionError :
          
        print (" Error: Division by zero is not allowed!")
        return None


while True :
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
        result = divide(num1, num2)
        
        if result is not None :
            print(f" Result is : {result}")
            break
    except ValueError :
        print("Error: Please enter numbers only!")
    
    finally:
        print(" Program executed successfully!")




