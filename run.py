# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import os
import time
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('test_dat')
cpus = SHEET.worksheet('cpus')
ram = SHEET.worksheet('ram')
gpus = SHEET.worksheet('gpus')
hdd = SHEET.worksheet('hdd')
partslist = SHEET.worksheet('partslist')
cpu_selected = 0
ram_selected = 0
gpu_selected = 0
hdd_selected = 0

def clear():
    # check and make call for specific operating system 
    # (https://www.geeksforgeeks.org/clear-screen-python/)
    os.system('clear' if os.name == 'posix' else 'cls')

def slow_print(msg):
    print(msg)
    time.sleep(1)


def main_menu():
    global cpu_selected
    global ram_selected
    global gpu_selected
    global hdd_selected
    while (True):
        print(cpu_selected)
        print(ram_selected)
        print(gpu_selected)
        print(hdd_selected)
        zeroprice = int(0)
        partslist.update('E2', zeroprice) 
        if cpu_selected >= 1 and gpu_selected >= 1 and ram_selected >= 1 and hdd_selected >= 1:
            cpu_choice = partslist.acell('A2').value
            ram_choice = partslist.acell('B2').value
            gpu_choice = partslist.acell('C2').value
            hdd_choice = partslist.acell('D2').value
            total_price = partslist.acell('E7').value
            slow_print("Loading parts selection.... ")
            print("CPU = " + cpu_choice + "\n" + "RAM = " + ram_choice + "\n" + "GPU = " + gpu_choice + "\n" + "HDD = " + hdd_choice)
            print("Calculating total price....")
            time.sleep(4)
            print("€" + total_price)
            time.sleep(8)
            clear()
            slow_print("1 -- Return to start")
            slow_print("2 -- Exit Web Application")
            selected = input("Please pick from the above options... ")
            if selected == '1':
                cpu_selected = 0
                gpu_selected = 0
                ram_selected = 0
                hdd_selected = 0
                clear()
                print("Returning to main menu....")
                continue
            elif selected == '2':
                clear()
                slow_print("Bye for now....")
                break
        else:
            slow_print("1 -- CPU Stocklist")
            slow_print("2 -- RAM Stocklist")
            slow_print("3 -- GPU Stocklist")
            slow_print("4 -- Storage Drive Stocklist")
            slow_print("5 -- Exit Store")
            selected = input("Please pick from the above options... ")
            if selected == '1':
                clear()
                time.sleep(4)
                cpu_list = len(cpus.col_values(1)[1:])

                def show_cpus():
                    for x in range(cpu_list):
                        if cpus.cell((2+x), 1).value is not None:
                            y = x + 1
                            y_string = str(y)
                            entry_cpu = cpus.cell((2+x), 1)
                            entry_core = cpus.cell((2+x), 2)
                            entry_price = cpus.cell((2+x), 5)
                            print("\n")
                            print(y_string + ". : " + entry_cpu.value + " " + entry_core.value + " Cores" + "\n Price: €" + entry_price.value)
                            
                        elif x+1 == range(cpu_list):
                            return
                slow_print("Loading CPUs currently in stock, please be patient...")
                show_cpus()
                selected = input("Input the number of your chosen CPU.")
                if selected == '1':
                    choice = cpus.cell(2, 1).value
                    cpu_price = float(cpus.cell(2, 5).value)
                    partslist.update('A2', choice)
                    partslist.update('E3', cpu_price)
                    cpu_selected = cpu_selected + 1
                elif selected == '2':
                    choice = cpus.cell(3, 1).value
                    cpu_price = float(cpus.cell(3, 5).value)
                    partslist.update('A2', choice)
                    partslist.update('E3', cpu_price)
                    cpu_selected = cpu_selected + 1
                elif selected == '3':
                    choice = cpus.cell(4, 1).value
                    cpu_price = float(cpus.cell(4, 5).value)
                    partslist.update('A2', choice)
                    partslist.update('E3', cpu_price)
                    cpu_selected = cpu_selected + 1
                elif selected == '4':
                    choice = cpus.cell(5, 1).value
                    cpu_price = float(cpus.cell(5, 5).value)
                    partslist.update('A2', choice)
                    partslist.update('E3', cpu_price)
                    cpu_selected = cpu_selected + 1
                    
                else:
                    print("Not a valid selection choice. Exiting....")
                clear()
                time.sleep(4)
                continue

            elif selected == '2':
                clear()
                time.sleep(4)
                ram_list = len(ram.col_values(1)[1:])

                def show_ram():
                    for x in range(ram_list):
                        if ram.cell((2+x), 1).value is not None:
                            y = x + 1
                            y_string = str(y)
                            entry_name = ram.cell((2+x), 1)
                            entry_price = ram.cell((2+x), 3)
                            print("\n")
                            print(y_string + ". : " + entry_name.value + "\n Price: €" + entry_price.value)
                            
                        elif x+1 == range(ram_list):
                            return
                slow_print("Loading RAM currently in stock, please be patient...")
                show_ram()
                selected = input("Input the number of your chosen RAM.")
                if selected == '1':
                    choice = ram.cell(2, 1).value
                    ram_price = float(ram.cell(2, 3).value)
                    partslist.update('B2', choice)
                    partslist.update('E4', ram_price)
                    ram_selected = ram_selected + 1
                elif selected == '2':
                    choice = ram.cell(3, 1).value
                    ram_price = float(ram.cell(3, 3).value)
                    partslist.update('B2', choice)
                    partslist.update('E4', ram_price)
                    ram_selected = ram_selected + 1
                elif selected == '3':
                    choice = ram.cell(4, 1).value
                    ram_price = float(ram.cell(4, 3).value)
                    partslist.update('B2', choice)
                    partslist.update('E4', ram_price)
                    ram_selected = ram_selected + 1
                elif selected == '4':
                    choice = ram.cell(5, 1).value
                    ram_price = float(ram.cell(5, 3).value)
                    partslist.update('B2', choice)
                    partslist.update('E4', ram_price)
                    ram_selected = ram_selected + 1
                else:
                    print("Not a valid selection choice. Exiting....")
                    main_menu()
                    selected = input("Please pick from the above options... ")

                clear()
                time.sleep(4)

            elif selected == '3':
                clear()
                time.sleep(4)
                gpus_list = len(gpus.col_values(1)[1:])

                def show_gpus():
                    for x in range(gpus_list):
                        if gpus.cell((2+x), 1).value is not None:
                            y = x + 1
                            y_string = str(y)
                            entry_name = gpus.cell((2+x), 1)
                            entry_vram = gpus.cell((2+x), 2)
                            entry_price = gpus.cell((2+x), 4)
                            print("\n")
                            print(y_string + ". : " + entry_name.value + " " + entry_vram.value + " " + "\n Price: €" + entry_price.value)
                            
                        elif x+1 == range(gpus_list):
                            return
                slow_print("Loading GPUs currently in stock, please be patient...")
                show_gpus()
                selected = input("Input the number of your chosen GPU.")
                if selected == '1':
                    choice = gpus.cell(2, 1).value
                    gpus_price = float(gpus.cell(2, 4).value)
                    partslist.update('C2', choice)
                    partslist.update('E5', gpus_price)
                    gpu_selected = gpu_selected + 1
                elif selected == '2':
                    choice = gpus.cell(3, 1).value
                    gpus_price = float(gpus.cell(3, 4).value)
                    partslist.update('C2', choice)
                    partslist.update('E5', gpus_price)
                    gpu_selected = gpu_selected + 1
                elif selected == '3':
                    choice = gpus.cell(4, 1).value
                    gpus_price = float(gpus.cell(4, 4).value)
                    partslist.update('C2', choice)
                    partslist.update('E5', gpus_price)
                    gpu_selected = gpu_selected + 1
                elif selected == '4':
                    choice = gpus.cell(5, 1).value
                    gpus_price = float(gpus.cell(5, 4).value)
                    partslist.update('C2', choice)
                    partslist.update('E5', gpus_price)
                    gpu_selected = gpu_selected + 1
                elif selected == '5':
                    choice = gpus.cell(6, 1).value
                    gpus_price = float(gpus.cell(6, 4).value)
                    partslist.update('C2', choice)
                    partslist.update('E5', gpus_price)
                    gpu_selected = gpu_selected + 1
                else:
                    print("Not a valid selection choice. Exiting....")
                    main_menu()
                    selected = input("Please pick from the above options... ")

                clear()
                time.sleep(4)

            elif selected == '4':
                clear()
                time.sleep(4)
                hdd_list = len(hdd.col_values(1)[1:])

                def show_hdd():
                    for x in range(hdd_list):
                        if hdd.cell((2+x), 1).value is not None:
                            y = x + 1
                            y_string = str(y)
                            entry_name = hdd.cell((2+x), 1)
                            entry_rpm = hdd.cell((2+x), 2)
                            entry_price = hdd.cell((2+x), 4)
                            print("\n")
                            print(y_string + ". : " + entry_name.value + " " + entry_rpm.value + "RPM " + "\n Price: €" + entry_price.value)
                            
                        elif x+1 == range(hdd_list):
                            return
                slow_print("Loading storage devices currently in stock, please be patient...")
                show_hdd()
                selected = input("Input the number of your chosen HDD.")
                if selected == '1':
                    choice = hdd.cell(2, 1).value
                    hdd_price = float(hdd.cell(2, 4).value)
                    partslist.update('D2', choice)
                    partslist.update('E6', hdd_price)
                    hdd_selected = hdd_selected + 1
                elif selected == '2':
                    choice = hdd.cell(3, 1).value
                    hdd_price = float(hdd.cell(3, 4).value)
                    partslist.update('D2', choice)
                    partslist.update('E6', hdd_price)
                    hdd_selected = hdd_selected + 1
                elif selected == '3':
                    choice = hdd.cell(4, 1).value
                    hdd_price = float(hdd.cell(4, 4).value)
                    partslist.update('D2', choice)
                    partslist.update('E6', hdd_price)
                    hdd_selected = hdd_selected + 1
                elif selected == '4':
                    choice = hdd.cell(5, 1).value
                    hdd_price = float(hdd.cell(5, 4).value)
                    partslist.update('D2', choice)
                    partslist.update('E6', hdd_price)
                    hdd_selected = hdd_selected + 1
                elif selected == '5':
                    choice = hdd.cell(6, 1).value
                    hdd_price = float(hdd.cell(6, 4).value)
                    partslist.update('D2', choice)
                    partslist.update('E6', hdd_price)
                    hdd_selected = hdd_selected + 1
                else:
                    print("Not a valid selection choice. Exiting....")

                clear()
                time.sleep(4)
            



def shop_intro():
    print("(C)1992 DIGITAL COMPUTER PARTS LTD")
    slow_print("POWERED BY MINITEL")
    slow_print("==========================")
    print("PRESS ANY KEY TO ENTER")
    input("")
    slow_print("Proceeding...")
    main_menu()

shop_intro()