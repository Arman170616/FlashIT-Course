#loop  

# hello = "hello world!"

# for x in hello:
#     print(x)


# count = 0
# while count <5:
#     print(count)
#     count = count +1


password = ""

while password != "python":
    password = input("Enter password: ")
    if password == "python":
        print("You are logged in")
    else:
        print("Sorry, try again")