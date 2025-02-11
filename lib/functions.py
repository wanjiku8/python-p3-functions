#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!") 

def greet(name):
    print(f"Hello, {name}!") 

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!") 

def add(num1, num2):
    return num1 + num2

def halve(number):
    return number / 2 

greet_programmer()
greet("Faith")
greet_with_default()
print(add(3, 4))
print(halve(10)) 
