import time
import os
import random


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def fun_number_pattern():
    rows = 5  
    symbols = ["*", "#", "@", "!"] 
    for _ in range(10): 
        clear_screen()
        print("🎉 CRAZY NUMBER PYRAMID! 🎉\n")
        for i in range(rows):
           
            print(" " * (rows - i - 1), end="")
            
            for _ in range(2 * i + 1):
                if random.random() < 0.3: 
                    print(random.choice(symbols), end="")
                else:
                    print(random.randint(0, 9), end="")
            print()  
        print("\n~~~ WILD NUMBER PARTY! ~~~")
        time.sleep(0.3) 


if __name__ == "__main__":
    try:
        print("Get ready for a NUMBER BLAST!")
        time.sleep(1)
        fun_number_pattern()
        clear_screen()
        print("Hope you loved the NUMBER MADNESS! 😜")
    except KeyboardInterrupt:
        clear_screen()
        print("Number party crashed! See ya! 🚀")