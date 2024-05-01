# Using ChatGPT to Increase your Learning Efficiency🌟
To be honest, it is difficult stepping into a whole new territory, with lots of experts and people who have also made a successful career switch. When you're just starting out and maybe have not found some teachers and friends to share your journey, ChatGPT may be your best friend. To me (and a lot of experts I'm sure), the threat of being replaced by AI is real, but at the same time, it is so convenient to consult ChatGPT... once you know some basic code and how to prompt it in doing what you want.
However, it is not perfect, and may make up some stuff that you did not request it to do. It is still fun to play around with it, and may become your erratic teacher/model or source of inspiration.
(P.S. This document is just me sharing my learning journey and some fun stuff I'm trying out as I play around with coding. Constructive criticism and ideas are welcome!)

## Original Simple Python Calculator Code:
```ruby
"""
Write a program that simulates a simple calculator. The program should allow the user to enter two numbers and an operator (e.g., +, -, *, /), 
and then calculate the result.
"""
#Check if input is numeric
def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a numeric value.")

#Check if input is an operator
def get_operators(prompt):
    while True:
        try:
            opt = input(prompt)
            if opt in ("+", "-", "*", "/"):
                return opt
            else:
                raise ValueError
        except ValueError:
            print("Please enter +, -, *, or /.")

#Request input from user
operator = get_operators("Enter an operator (+ - * /): ")
num1 = get_numeric_input("Enter a number: ")
num2 = get_numeric_input("Enter another number: ")

#Calculation function
def calculation(n1, op, n2):
    def result():
        if op == "+":
            return n1 + n2
        elif op == "-":
            return n1 - n2
        elif op == "*":
            return n1 * n2
        elif op == "/":
            return n1 / n2
        else:
            "Invalid number or operator has been entered."
    return(f"{num1} {operator} {num2} = {result()}")

#Output to user
print(calculation(num1, operator, num2))
```

## Let Your Ideas Flow - Entering a Prompt to Generative AI
I've read about how we should be using AI tools to help with coding or making code readable, so I thought,
_'Why not make the calculator function into just one line?'_
Coincidentally, I was reviewing some basic python and came across using  ```eval()```, which evaluates an expression into a python statement if it can be run. Thus, as a lazy person (who does not like repeating multiple lines of code), I feel like it can be done.

<kbd>
<img src="https://github.com/evelee9393/evelee9393/assets/166385908/2a4ad4da-53c6-4c00-975a-cbd58f23b648"/>
</kbd>

## Final Code
Thus, with some modifications, the calculator function was updated (also reminding I need to consider ZeroDivisionError 😂).
```
"""
Calculator using eval function
"""
#Check if input is numeric
def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a numeric value.")

#Check if input is an operator
def get_operators(prompt):
    while True:
        try:
            opt = input(prompt)
            if opt in ("+", "-", "*", "/"):
                return opt
            else:
                raise ValueError
        except ValueError:
            print("Please enter +, -, *, or /.")

#updated calculator function with eval
def calculation(n1, n2, op):
    try:
        result = eval(f"{n1} {op} {n2}")
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero!"
    except Exception as e:
        return "Invalid number or operator has been entered."

#User intro + input prompt
print("Welcome to the calculator!")

num1 = get_numeric_input("Enter first number: ")
operator = get_operators("Enter operator (+, -, *, /): ")
num2 = get_numeric_input("Enter second number: ")
    
#Output to user
print(calculation(num1, num2, operator))
```

## Conclusion and Pros/Cons
Using ChatGPT has made my learning experience much faster, but there are also some concerns.
| Pros | Cons |
| --- | --- |
| If you have basic code knowledge, you can use it to modify code with minimal effort | You won't do your research and discover more efficient coding techniques by yourself! |
| ChatGPT basically organizes the most efficient method out there! | Sometimes it will return unwanted parts of code or change your variables, so watch out! |
Thanks for reading through my learning journey. I hope it will also help me in the future as well (or maybe I'll have a laugh when I look back at this).
