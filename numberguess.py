#x = 500
# y = 0
#y isnt needed

# while True:
#     if x > 0:
#         x = x - 100
#         print(x)
#     else:
#         break





# x = 500

# while x > 0:
#     x = x - 100
#     print(x)





# while True:
#     z = input("multiply?")
#     if z == "exit":
#         break



# while True:   
#     z = input("enter a number to multiply by 2 (or 'exit' to quit):")

#     if z == "exit":
#         break
#     number = float(z)
#     print(number * 2)



def number():
    import random
    y = random.randint(1,10)
    guess_history = []

    while True:
        x = int(input("guess the number"))
        guess_history.append(x)

        if x > y:
            print("too much")
        elif x < y:
            print("too little")
        else:
            print("perfect")
            break

    print(guess_history)
    for i in guess_history: 
        print(i)
                

number()