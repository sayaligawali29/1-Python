# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 20:47:22 2023

@author: user
"""

def make_pizza(size,*toppings):
    print(f"\nMaking the {size}-inch pizza with following toppings:")
    for topping in toppings:
        print(f"-{topping}")