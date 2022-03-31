import time
import os

print("""

██╗░░░██╗██╗██████╗░███████╗██╗██╗░░░░░██╗░░░░░░█████╗░
╚██╗░██╔╝██║██╔══██╗╚════██║██║██║░░░░░██║░░░░░██╔══██╗
░╚████╔╝░██║██████╔╝░░███╔═╝██║██║░░░░░██║░░░░░███████║
░░╚██╔╝░░██║██╔═══╝░██╔══╝░░██║██║░░░░░██║░░░░░██╔══██║
░░░██║░░░██║██║░░░░░███████╗██║███████╗███████╗██║░░██║
░░░╚═╝░░░╚═╝╚═╝░░░░░╚══════╝╚═╝╚══════╝╚══════╝╚═╝░░╚═╝
    """)

print("""
    [1] Continue with setup
    [2] Already done setup
""")

setup = input("[?]: ")

if setup == '1':
    name = input(str("Enter a username: "))
    pas = input(str("Enter a password: "))

    lines = [name]
    with open("user/username.txt", "w") as f:
        f.writelines(lines)

        lines2 = [pas]
        with open("user/password.txt", "w") as f:
            f.writelines(lines)
            print("Setup Complete!")
            input("Press Enter To Close ")

if setup == "2":

    login_pas = open("user/password.txt")
    login_name = open("user/username.txt")

    l_p = login_pas.read()
    l_n = login_name.read()

while True:
    login = input(str("Enter Password To " + l_n + ": "))
    if login == l_p:
        os.strartfile("home.py")
        break
    else:
        print("False!")