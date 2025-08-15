 # -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 11:47:27 2025

@author: Mahjoobe Nazari

"""

"""
A simple Python program that divides two numbers with error handling.
The program handles:
1. Division by zero (ZeroDivisionError)
2. Non-numeric inputs (ValueError)
"""


def divide(a, b):
    
    """
   Divide two numbers and handle division by zero.

   Parameters:
       a (float or int): Dividend
       b (float or int): Divisor

   Returns:
       float or None: The division result, or None if division by zero occurs.
   """
   
    try:
        result = a / b
        return result
    
    except ZeroDivisionError :
          
        print (" Error: Division by zero is not allowed!")
        return None
    
    

if __name__ == "__main__":
    
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
