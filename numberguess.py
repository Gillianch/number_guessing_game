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



def number(x,y):
    import random
    y = random.randint(1,10)
    guess_history = []
    while True:
        x = int(input("guess the number"))
        if x > y:
            print("too much")
            guess_history.append(x)
        elif x < y:
            print("too little")
            guess_history.append(x)
        else:
            print("perfect")
            break

        guess_history.append(x)
        for i in guess_history:
            print(i)
