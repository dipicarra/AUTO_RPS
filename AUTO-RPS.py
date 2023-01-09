# AUTO ROCK PAPER SCISSORS
# YOU CAN CONTACT ME @ https://discord.com/users/976932346550972477

# THIS IS V1 OF A CS PROJECT
# BY ROMEU

import random
plays = ["r", "p", "s"] # THE PLAYS ALLOWED IN THE GAME
a = True
while a:
    # --- INTRO ---

    print(""" 
    How to play :
    To play ROCK - write 'r'
    To play PAPER - write 'p'")
    To play SCISSORS - write 's")
    That's it have fun! <3
    """)

    # --- INITIALIZATION ---

    p1 = str(input("PLAYER 1 - PLAY : "))
    # --- RANDOM PLAY ---

    # --- VERIFICATION ---
    if p1 in plays:
       
       # --- GENERATE THE AUTO PLAY ---
       # THIS IS INSIDE THE VERIFICATION BECAUSE IF NOT WHEN "P1 != PLAYS" IT WILL STILL PRINT P2
        min = 0
        maxi = 2
        random_numb = random.randint(min , maxi) # I KNOW THERE'S A RANDOM PICKER INSIDE A LIST (RANDOM_CHOICE) BUT THIS WAY IT'S FUNNIER :)
        if random_numb == 0:
            p2 = plays[0]
            print("PLAYER 2 - PLAY :", p2)
        elif random_numb == 1:
            p2 = plays[1]
            print("PLAYER 2 - PLAY :", p2)
        else:
            p2 = plays [2]
            print("PLAYER 2 - PLAY :", p2)

        # --- VERIFY THE WINNER AND THE PLAYS

        if p1 == p2:
            print("PLAYER 1 AND 2 - DRAW")
        elif p1 == "r" and p2 == "p":
            print("PLAYER 2 - WINS")
        elif p1 == "r" and p2 == "s":
            print("PLAYER 1 - WINS")
        elif p1 == "p" and p2 == "r":
            print("PLAYER 1 - WINS")
        elif p1 == "p" and p2 == "s":
            print("PLAYER 2 - WINS")
        elif p1 == "s" and p2 == "r":
            print("PLAYER 2 - WINS")
        elif p1 == "s" and p2 == "p":
            print("PLAYER 1 - WINS")
    else:
        print("""
        Please use the allowed plays:
        - Rock - "w" 
        - Paper - "p"
        - Scissors - "s"
        """)

    # --- LOOP BREAKER ---
    cp = str(input("WOULD YOU LIKE TO CONTINUE PLAYING? (y/n): "))
    if cp == "y":
        a == True
    else:
        break