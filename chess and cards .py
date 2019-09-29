# problem 2
# make a shuffle cards and print all its content
import random
cardfaces = []
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
royals = ["J", "Q", "K", "A"]
# for combined
deck = []
for i in range(2,11):
    cardfaces.append(str(i))
for j in range(4):
    cardfaces.append(royals[j])
for k in range(4):
    for l in range(13):
        card = (cardfaces[l] + " of " + suits[k])
        deck.append(card)
random.shuffle(deck)
for m in range(52):
    print(deck[m])

# problem 3
# hangman game
import random
possible_answers = ["SNAKE", "COW", "ELEPHANT", "BEAR", "BIRD", "WOLF","WORM"]
random.shuffle(possible_answers)
answer = list(possible_answers[0])
display = []
display.extend(answer)
for i in range(len(display)):
    display[i] = "_"
print("Hangman\n")
print(" ".join(display))
print("\n")
count = 0
while count < len(answer):
    guess = input("Please guess a letter : ")
    guess = guess.upper()
    for i in range(len(answer)):
        if answer[i] == guess:
            display[i] = guess
            count += 1
    print(" ".join(display))
    print("\n\n\n")
print("you Guessed It !!!")


# problem 1
def notes(x):
    a = x[0]
    b = int(x[1:])
    a = ord(a) -64
    return [a-1,b-1]
def post(li,z):
    second = [-2,2]
    one = [-1,1]
    li[z[0]][z[1]] = "o"
    for i in one:
        for j in second:
            if(z[0]-i>=0) and (z[1]-j>=0):
                li[z[0]-i][z[1]-j]="+"
    for i in second:
        for j in one:
            if(z[0]-i>0) and (z[1]-j>0):
                li[z[0]-i][z[1]-j]="+"
    return li
def chess(z,x=8,y=8):
    li=[]
    for i in range(x):
        li.append([])
        for j in range(y):
            li[i].append("-")
    z=notes(z)
    li=post(li,z)
    for i in range(y)[::-1]:
        for j in range(x):
            print(li[j][i],end="")
        print("")
chess("E4")



