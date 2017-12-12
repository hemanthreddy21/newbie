player_name =  input("What's your name? ")
print("Your name is {}".format(player_name))
print("Let's start our adventure!!!\n")
print("Guess the colour treasure box")
print(" Press 1 for blue")
print(" Press 2 for red")
print(" Press 3 for orange")
a=int(input("Enter your choice"))

if a==1:
    print("bad luck")
    exit()
elif a==2:
    print("correct choice")
    print("You have two keys with you")
    print("Choose any one")
    print(" Press 1 for first key ")
elif a==3:
    print("bad luck")
    exit()    
print(" Press 2 for second key r")
b=int(input("Enter your choice"))
if b==1:
    print("bad luck")
    exit()
elif b==2:
    print("correct choice")


