import random
import time
from interruptingcow import timeout


def end(w, n, g):
    if (w):
        print("You won!");
    else:
        print("You lost!");
    record(n, g, w)


def record(name, game, score):
    if (score):
        result = "LOST";
    else:
        result = "WON";

    contents = open("result.csv", "a");
    contents.write(f"\n{name}, {game}, {result}");
    contents.close();


def game1(name):
    game = "Guessing Dice"
    again = True;
    while (again):
        tip_num = random.randint(1, 3)
        if tip_num ==1:
            if tip_num%2 == 0:
                print("Hint: the number is even")
            else:
                print("Hint: the number is odd")
        elif tip_num == 2:
            if tip_num > 3:
                print("Hint: the number is big (4, 5, 6)")
            else:
                print("Hint: the number is small (1, 2, 3)")
        else:
            print("There is not hint this time")
        answer = random.randint(1, 6);
        guess = int(input("Guess a number: "));
        if guess == answer:
            end(True, name, game);
        else:
            end(False, name, game);
        o = input("Would you like to keep playing? (y/n): ");
        if not (o == "y" or o == "Y" or o == "yes" or o == "Yes"):
            again = False


def game2(name):
    game = "Sum";
    again = True;
    while (again):
        result = [];

        print("\nAnswer as many as you can in one minute!");
        try:
            with timeout(60, exception=RuntimeError):
                while (True):
                    number1 = random.randint(1, 100)
                    number2 = random.randint(1, 100)
                    print("what the sum of ", number1, "and", number2)
                    guess = int(input("Enter your answer"))
                    if guess == number1 + number2:
                        result.append(1);
                        end(True, name, game);
                    else:
                        result.append(0);
                        end(False, name, game);
                pass
        except RuntimeError:
            print("Time's up!");
            print(f"number answered: {len(result)}, accuracy: {100 * sum(result) / len(result)}%,");

        o = input("Would you like to keep playing? (y/n): ");

        if not (o == "y" or o == "Y" or o == "yes" or o == "Yes"):
            again = False


def game3(name):
    game = "Guessing two dice";
    again = True;
    while (again):
        first = 0
        second = 0
        numbers = []
        numbers.append(random.randint(1, 6));
        numbers.append(random.randint(1, 6));
        total = sum(numbers);
        print("The sum is: ", total)
        if numbers[0] % 2==0:
            first = "even"
        else:
            first = "odd"
        if numbers[1] % 2 ==0:
            second = "even"
        else:
            second = "odd"
        print("Hint: the sum is made of a(n)", first, "number and a(n)", second,"number")
        guessing1 = int(input("Guess first number: "));
        guessing2 = int(input("Guess second number: "));

        anssum = guessing1 + guessing2;

        if (anssum == total and guessing1 in numbers):
            end(True, name, game);
        else:
            end(False, name, game);
        o = input("Would you like to keep playing? (y/n): ");
        if not (o == "y" or o == "Y" or o == "yes" or o == "Yes"):
            again = False





# initializing results file
##contents = open("result.csv", "a");
##contents.write("name, game, result");
##contents.close();

# user set up
name = input("Please enter your name: ");
leave = False;
print(f"Welcome, {name}!");

while (not leave):
    print("\n\n");
    choosing = int(input("Pick a game: "))
    if choosing == 1:
        game1(name)
    elif choosing == 2:
        game2(name)
    elif choosing == 3:
        game3(name)
    else:
        print("Please pick right game")

