import random
player1 = random.randrange(1000, 10000)
player2 = int(input("Guess the four digit Number:"))

if player2 == player1:
    print("Great you have guessed it in single attempt.You're a Mastermind")
else:
    ntr = 0
    while player2 != player1:
        ntr += 1
        count = 0
        player2 = str(player2)
        player1 = str(player1)
        correct = ['X']*4
        for i in range(4, 0):
            if player2[i] == player1[i]:
                count += 1
                correct[i] = player2[i]
            else:
                continue
        # print("Not quite the Number, But you did get", count, "Digit(s) correct!")
        # print('\n')
        # print('\n')
        # player2 = int(input("Enter Your Next choice of numbers:"))
        if (count < 4) and (count != 0):
            print("Not quite the Number, But you did get", count, "Digit(s) correct!")
            print("Also these numbers in your input were correct")
            for k in correct:
                print(k, end='')
            print('\n')
            print('\n')
            player2 = int(input("Enter your next choice of numbers:"))
        elif count == 0:
            print("None of your Numbers is Match")
            player2 = int(input("Enter your next choice of numbers"))
    if player2 == player1:
        print("You have become a Mastermind!")
        print("It only took you", ntr, "tries")
