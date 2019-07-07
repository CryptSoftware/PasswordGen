#I know I didn't comment on my code but you should figure it out.
import random
import os
import time

low_password_body=["greenland", "parade", "mexico", "challenge"]

moderate_password_body=["mYcat", "oVal", "doritSO", "HobBit"]

high_password_body=["iHaveAbAs", "nEverMinddMe", "pErBinerAl"]

low_password_ending=["52", "56", "72", "3", "89", "32", "96", "64"]

moderate_password_ending=["@8*2", "#65%", "*67", "954", "42", "&683%"]

high_password_ending=["#*4@1!", "!5$#", "567&" , "6$83%", "6@#1", "67%*4!", "9%$4"]
print("""██████╗  █████╗ ███████╗███████╗ ██████╗ ███████╗███╗   ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██╔════╝████╗  ██║
██████╔╝███████║███████╗███████╗██║  ███╗█████╗  ██╔██╗ ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║   ██║██╔══╝  ██║╚██╗██║
██║     ██║  ██║███████║███████║╚██████╔╝███████╗██║ ╚████║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                           """)
print("Created by Crypt, https://github.com/CryptSoftware")
how_messed_up = input("[+] How messed up do you want it to be? (high, moderate and low) Default: Low. ")

if how_messed_up == "high":
    password_body_high=random.choice(high_password_body)
    password_endings_high=random.choice(high_password_ending)
    print("[+] Password Generated! Your password is: " + password_body_high + password_endings_high)
    save_to_file_high = input("[*] Would you like to save it to a file? (y/n): ")
    full_pass_high = password_body_high + password_endings_high

    if save_to_file_high == "y":
        file = open("Saved_Password.txt", "w+")
        file.write(full_pass_high)
        file.close()
        print("[!] WARNING! FILE MAY NOT SAVE IN THE SAME DIRECTORY AS THE REPOSITORY, PLEASE SEARCH YOUR SYSTEM FOR THE FILE.")
        print("[+] File saved successfully!")


if how_messed_up == "moderate":
    password_body_moderate=random.choice(moderate_password_body)
    password_endings_moderate=random.choice(moderate_password_ending)
    print("[+] Password Generated! Your password is: " + password_body_moderate + password_endings_moderate)
    save_to_file_moderate = input("[*] Would you like to save it to a file? (y/n): ")
    full_pass_moderate = password_body_moderate + password_endings_moderate

    if save_to_file_moderate == "y":
        file = open("Saved_Password.txt", "w+")
        file.write(full_pass_moderate)
        file.close()
        print("[!] WARNING! FILE MAY NOT SAVE IN THE SAME DIRECTORY AS THE REPOSITORY, PLEASE SEARCH YOUR SYSTEM FOR THE FILE.")
        print("[+] File saved successfully!")


if how_messed_up == "low":
    password_body_low=random.choice(low_password_body)
    password_endings_low=random.choice(low_password_ending)
    print("[+] Password Generated! Your password is: " + password_body_low + password_endings_low)
    save_to_file_low = input("[*] Would you like to save it to a file? (y/n): ")
    full_pass_low = password_body_low + password_endings_low

    if save_to_file_low == "y":
        file = open("Saved_Password.txt", "w+")
        file.write(full_pass_low)
        file.close()
        print("[!] WARNING! FILE MAY NOT SAVE IN THE SAME DIRECTORY AS THE REPOSITORY, PLEASE SEARCH YOUR SYSTEM FOR THE FILE.")
        print("[+] File saved successfully!")
    
