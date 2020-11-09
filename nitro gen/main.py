import colorama
import string
import random
import time
import os
from colorama import Fore, init

colorama.init()
os.system('cls')

def logo():
    print("""

        ███╗░░██╗██╗████████╗██████╗░░█████╗░  ░██████╗░███████╗███╗░░██╗
        ████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔════╝░██╔════╝████╗░██║
        ██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░██╗░█████╗░░██╔██╗██║
        ██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░╚██╗██╔══╝░░██║╚████║
        ██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚██████╔╝███████╗██║░╚███║
        ╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝
   made by fighter x""")
    
    print("""
    [1] Discord Nitro Generator
    [2] Exit
    [3] credits
    [4] check requirements
     """)
    choice = int(input("[?]: "))
    if choice == 1:
        
        codeLen = 16 
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        lp = int(input("Enter The Number Of Unchecked Codes You Need: "))
        k = open('unchcekedcodes.txt', 'w')
        for i in range(lp):
            k.write("discord.gift/" + ''.join(random.choice(letters) for i in range(codeLen)) + '\n')
        k.close()
        os.system('cls')
        logo()

    elif choice == 2:
        print('Closing please wait ...'); time.sleep(1)
        os.system('Exit')
        os.system('cls')
        
    elif choice == 3:
        os.system('type important.txt'); time.sleep(5)
        os.system('cls')
        logo()

    elif choice == 4:
        os.system('pip install --user -r req.txt'); time.sleep(2)
        os.system('cls')
        logo()

    else:
        print("invalid choice!")
        time.sleep(2)
        os.system('cls')
        logo()
        
logo()