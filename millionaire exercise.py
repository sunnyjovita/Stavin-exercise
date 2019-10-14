money = 0
def intro():
    print("Welcome to the Who Wants To Be A Millionaire? Today you will try to get $1000,000.")
    name = input("Your name :")
    print("Hello", name, "Goodluck!")
    print("your current cash $", money, "dollars.")
    game()
def question(question_name, question_answer, alternative_answer, current_money, money):
    answer = input(question_name)
    if(answer == question_answer) or (answer == alternative_answer):
        print("you got the answer right! Good job!")
        money = current_money
        print("your current cash $",money, "dollars")
    else:
        print("Sorry your answer is wrong, better luck next time!")
        money = 0
        exit()
def game():
    question("What's 10+10 ?\n", "20", "twenty", 100, money)
    question("How many days in a week?\n", "7", "seven", 1000, money)
    question("How many times we eat in a day?\n", "3", "three", 10.000, money)
    question("Who is the previous president of USA?\n", "Obama", "obama", 50000, money)
    question("Which country features a maple leaf on its flag?\n", "Canada", "canada", 100000, money)
    question("What is the capital of Indonesia?\n", "Jakarta", "jakarta", 150000, money)
    question("How many colours are there in a rainbow?\n", "7", "seven", 200000, money)
    question("In which direction does the sun rise?\n", "east", "East", 250000, money)
    question("Which month of the year has the least number of days?\n", "February", "february", 300000, money)
    question("How many hours are there in two days?\n", "48","forty eight", 500000, money)
    question("How many weeks are there in one year?\n", "52", "fifty two", 600000, money)
    question("How many lungs does the human body have?\n", "2", "two", 700000, money)
    question("How many years are there in a century?\n", "100", "one hundred", 800000, money)
    question("Who is the founder of Microsoft?\n", "Bill Gates", "bill gates", 900000, money)
    question("Which country is home for the kangaroo?\n", "australia", "Australia", 1000000, money)
    print("CONGRATS, YOU WON THIS GAME!!!!")
    print("HERE YOU GO $1000.000")
    exit()
intro()