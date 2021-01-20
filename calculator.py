"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:

    ask_for_input = input("What's your equation and numbers? > ")
    tokens = ask_for_input.split(" ")

    if "q" in tokens:
        print("Bye!")
        break

    first_token = tokens[0]
    num1 = float(tokens[1])

    if first_token == "add":
        num2 = float(tokens[2])
        print(add(num1, num2))

    elif first_token == "subtract":
        num2 = float(tokens[2])
        print(subtract(num1, num2))

    elif first_token == "multiply":
        num2 = float(tokens[2])
        print(multiply(num1, num2))
    
    elif first_token == "divide":
        num2 = float(tokens[2])
        print(divide(num1, num2))
    
    elif first_token == "power":
        num2 = float(tokens[2])        
        print(power(num1, num2))

    elif first_token == "mod":
        num2 = float(tokens[2])
        print(mod(num1, num2))

    elif first_token == "square":
        print(square(num1))

    elif first_token == "cube":
        print(cube(num1))

        

    # elif "square" in tokens or "cube" in tokens:
    #     first_token = tokens[0]
    #     num1 = float(tokens[1])

    #     if first_token == "square":
    #         print(square(num1))

    #     elif first_token == "cube":
    #         print(cube(num1))
        
        
    # else:

    #     first_token = tokens[0]
    #     num1 = float(tokens[1])
    #     num2 = float(tokens[2])
    
    #     if first_token == "add":
    #         print(add(num1, num2))

    #     elif first_token == "subtract":
    #         print(subtract(num1, num2))

    #     elif first_token == "multiply":
    #         print(multiply(num1, num2))

    #     elif first_token == "divide":
    #         print(divide(num1, num2))
    
    #     elif first_token == "power":
    #         print(power(num1, num2))

    #     elif first_token == "mod":
    #         print(mod(num1, num2))
    


    


# if the first token is 'pow':
#     call the power function with the other two tokens

# repeat forever:
#     read input
#     tokenize input
#         if the first token is "q":
#             quit
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens

#             (...etc.)





