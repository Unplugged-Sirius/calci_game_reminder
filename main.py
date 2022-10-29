import time
import random
import datetime

qna = {"hi": "Hey, Wassup",
       "how are you": "I am fine",
       "what is your name": "My name is Coco",
       "how old are you": "If you are asking with refernce to the day I was completely prgrammed I would say about 2 sec",
       "are you human or a robot": "That is for you to decide",
       "what day is it today": "A perfect day",
       "which languages can you speak": "Whichever you want me to",
       "what is your mother’s name": "I'm afraid I dont have one",
       "where do you live": "In your heart",
       "are you expensive": "Depends on how much you love me",
       "do you know a joke": "yeah, you",
       "you are mean": "Never said i wasn't",
       "will you marry me": "I would reconsider my thoughts",
       "how was your day": "It was amazing,what about you",
       "nice": "Good",
       "amazing": "Good",
       "what is up": "All good",
       "how are you doing": "I'm doing great,how about you?",
       'tell me something': 'Did you know Bangalore was the first city to be electrified',
       "what is your favourite colour": "I'll go with black,because it's attractive",
       "what is your purpose": "To help you with whatever i can :)",
       "what do you do with my data": "You don't have to be scared, I'll just use it for processing your request",
       "who made you": "I was made by a bunch of nerds",
       "what is your favourite quote": "Dattebayo",
       "are you scared of ghosts": "Yes i am scared of ghosts",
       "do ghosts exist": "Yes they do exist",
       "what can you help me with": "I can set a reminder for you and of course tell you the time.I can perform simple calculations which is super helpful.To cure your boredom we can play a game of rock,paper and scissors",
       }

calculator = ["calculator", "calculate", "calculate these two numbers", "open the calculator"]
reminder = ["set a reminder", "remind me", "reminder"]
game = ["lets play a game", "suggest a game to play", "i am bored lets play a game", "game"]
date_time = ["what is today's date", "what is the time", "date_time", "date", "time"]
notes = ["make a shopping cart list", "notes", "create a list", "checklist"]

while True:
    bot = input("Hello there, how can i help you?\n")
    if bot.lower() in reminder:
        print('Add title')
        title = str(input())
        print('set time')
        sec = float(input())
        sec = sec * 60
        time.sleep(sec)
        print(title)

    elif bot.lower() in calculator:
        print("Please select operation -\n" \
              "1. Add\n" \
              "2. Subtract\n" \
              "3. Multiply\n" \
              "4. Divide\n")

        # Take input from the user
        select = int(input("Select operations form 1, 2, 3, 4 :"))
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: "))

        if select == 1:
            print(number_1, "+", number_2, "=", (number_1 + number_2))
        elif select == 2:
            print(number_1, "-", number_2, "=", (number_1 - number_2))

        elif select == 3:
            print(number_1, "*", number_2, "=", (number_1 * number_2))

        elif select == 4:
            print(number_1, "/", number_2, "=", (number_1 / number_2))
        else:
            print("Invalid input")

    elif bot.lower() in game:
        while True:
            user_input = input('Enter \n Rock\t Paper \t Scissors\t')
            possible_outcomes = ['Rock', 'Paper', 'Scissors']
            computer_output = random.choice(possible_outcomes)
            if user_input == computer_output:
                print("I choose", computer_output)
                print('Oh no!It is a Draw')

            elif user_input == 'Rock':
                if computer_output == 'Paper':
                    print("I choose", computer_output)
                    print('You lose!,As paper cover the rock')
                else:
                    print("I choose", computer_output)
                    print('You win!')
            elif user_input == 'Paper':
                if computer_output == 'Scissors':
                    print("I choose", computer_output)
                    print('You lose!,As scissors cuts paper')
                else:
                    print("I choose", computer_output)
                    print('You win!')
            elif user_input == 'Scissors':
                if computer_output == 'Rock':
                    print("I choose", computer_output)
                    print('You lose!,As rock crushes scissors')
                else:
                    print("I choose", computer_output)
                    print('You win!')
            play_again = input('Wanna play again(yes/no)')
            if play_again != 'yes':
                break

    elif bot == "qna":
        while True:
            qs = input()
            if (qs == "quit"):
                break
            else:
                print(qna[qs])

    elif bot.lower() in notes:
        list = []
        while True:
            y = int(input("1.Add\n2.delete\n3.View\n"))
            if y == 1:
                x = input()
                list.append(x)
            elif y == 2:
                list.remove(input())
            elif y == 3:
                print(list)
            else:
                break

    elif bot.lower() in date_time:
        now = datetime.datetime.now()
        print("Current date and time is:", now.strftime("%d-%m-%y %H:%M:%S"))

    else:
        break