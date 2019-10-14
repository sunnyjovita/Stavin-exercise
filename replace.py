# password
password = str(input("enter the password : "))
vowels = ["a", "e", "i", "o", "u"]
new_pass =  password.replace("a", "x").replace("e", "x").replace("u", "x").replace("i", "x").replace("o", "x").replace("A", "X").replace("E", "X").replace("I", "X").replace("U", "X").replace("O", "X")
l = len(password)

if (l<8):
    print("rejected!", new_pass)
elif ("xx" in password):
    print("Rejected!")
else:
    print(new_pass)








































