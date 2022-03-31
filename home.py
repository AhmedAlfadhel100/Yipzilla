from ast import If
from select import select
import time
import os
import psutil

battery = psutil.sensors_battery()

login_pas = open("user/password.txt")
login_name = open("user/username.txt")
l_p = login_pas.read()
l_n = login_name.read()

print("""

██╗░░░██╗██╗██████╗░███████╗██╗██╗░░░░░██╗░░░░░░█████╗░
╚██╗░██╔╝██║██╔══██╗╚════██║██║██║░░░░░██║░░░░░██╔══██╗
░╚████╔╝░██║██████╔╝░░███╔═╝██║██║░░░░░██║░░░░░███████║
░░╚██╔╝░░██║██╔═══╝░██╔══╝░░██║██║░░░░░██║░░░░░██╔══██║
░░░██║░░░██║██║░░░░░███████╗██║███████╗███████╗██║░░██║
░░░╚═╝░░░╚═╝╚═╝░░░░░╚══════╝╚═╝╚══════╝╚══════╝╚═╝░░╚═╝
    """)
print("Welcome " + l_n)
print("Date is " + time.strftime ('%d/%m/%y'))
print("The Battery Life: ")
print(battery)
print(""" 
[1] Yip Browser
[2] Yip Code
[3] Yip Files
[4] Close Yipzilla
""")

print("Yip Code can be opened in File Explorer.")
print("Yip Files can be opened in File Explorer.")

select == input("[?]: ")

if select == '1':
    os.startfile("browser.py")
