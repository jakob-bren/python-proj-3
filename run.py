"""Computer parts list creator."""
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import os
import sys
import time
import gspread
import pyfiglet
from prettytable import PrettyTable
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
# these vars below become "1"
# or "2" "3" etc depending on
# how many times a part is
# selected by the user
CPU_SELECTED = 0
RAM_SELECTED = 0
GPU_SELECTED = 0
HDD_SELECTED = 0


def close_prog():
    """Closes the program."""
    clear()
    slow_print("Bye for now....")
    sys.exit()


def clear():
    """Clears the screen."""
    # check and make call for specific operating system
    # (https://www.geeksforgeeks.org/clear-screen-python/)
    os.system('clear' if os.name == 'posix' else 'cls')


def slow_print(msg):
    """Prints after a small delay."""
    print(msg)
    time.sleep(1)


def admin_verify():
    """Verifies admin credentials."""
    while True:
        slow_print("Input credentials to continue.")
        user_name = input("Username: ")
        pass_word = input("Password: ")
        user_list = ['ulaidh', 'root']
        pass_list = ['dundalklouth', 'xY48428z!#2q']
        if user_name in user_list and pass_word in pass_list:
            print("Credentials verified! Proceeding...")
            time.sleep(3)
            clear()
            admin_console()
        elif user_name in user_list and pass_word not in pass_list:
            print("Password incorrect. Please try again.")
            pass_word = input("Password: ")
            if pass_word == 'dundalklouth':
                print("Thanks. Password verified."
                      "\nProceeding... ")
                admin_console()
        elif user_name not in user_list and pass_word not in pass_list:
            clear()
            print("Perhaps you've gotten lost."
                  "\n\nIf you didn't intend to be here,"
                  "\npress \"1\" to continue to the main menu."
                  "\nOtherwise, press 2.")
            lost = input("\nAwaiting input.... ")
            if lost == '1':
                clear()
                print("Proceeding...")
                time.sleep(2)
                clear()
                main_menu()
            elif lost == '2':
                clear()
                continue
            else:
                clear()
                print("Please type either \"1\" or \"2\" without any"
                      "quotation marks.")


def admin_console():
    """Administrative console for managing backend."""
    while True:
        def input_menu():
            print("Do you want to...")
            print("     1-- Modify description")
            print("     2-- Update quantity")
            print("     3-- Update price")
            print("     4-- Return")

        menu_logo = pyfiglet.figlet_format("GOD MODE")
        print(menu_logo)
        slow_print("1 -- Check/modify CPU stock")
        slow_print("2 -- Check/modify RAM Stocklist")
        slow_print("3 -- Check/modify GPU Stocklist")
        slow_print("4 -- Check/modify Storage Drive Stocklist")
        slow_print("5 -- Exit Console")

        selected = input("\nPlease pick from the above options... ")
        if selected == '1':
            clear()
            time.sleep(4)

            def show_cpus():
                data = cpus.get_all_values()
                table = PrettyTable()
                table.field_names = data[0]
                for row in data[1:]:
                    table.add_row(row)
                print(table)
            slow_print(
                "Loading CPUs currently in stock, please be patient...")
            while True:
                show_cpus()
                selected = input("\nInput the number of your chosen CPU. "
                                 "\nType \"exit\" to return to console.")
                if selected == '1':
                    while True:
                        input_menu()
                        selected = input("Choose one.. ")
                        if selected == '1':
                            nu_desc = input("Input new description.. ")
                            print(nu_desc)
                            cpus.update('B2', nu_desc)
                            print("Success! Description updated to " +
                                  nu_desc)
                            time.sleep(4)
                        if selected == '2':
                            nu_qty = input("Input new quantity.. ")
                            print(nu_qty)
                            cpus.update('E2', (int(nu_qty)))
                            print("Success! Quantity updated to " +
                                  nu_qty)
                            time.sleep(4)
                        if selected == '3':
                            nu_price = input("Input new price.. ")
                            print(nu_price)
                            cpus.update('F2', (float(nu_price)))
                            print("Success! Price updated to " +
                                  nu_price)
                            time.sleep(4)
                        if selected == '4':
                            break

                elif selected == '2':
                    while True:
                        input_menu()
                        selected = input("Choose one.. ")
                        if selected == '1':
                            nu_desc = input("Input new description.. ")
                            print(nu_desc)
                            cpus.update('B3', nu_desc)
                            print("Success! Description updated to " +
                                  nu_desc)
                            time.sleep(4)
                        if selected == '2':
                            nu_qty = input("Input new quantity.. ")
                            print(nu_qty)
                            cpus.update('E3', (int(nu_qty)))
                            print("Success! Quantity updated to " +
                                  nu_qty)
                            time.sleep(4)
                        if selected == '3':
                            nu_price = input("Input new price.. ")
                            print(nu_price)
                            cpus.update('F3', (float(nu_price)))
                            print("Success! Price updated to " +
                                  nu_price)
                            time.sleep(4)
                        if selected == '4':
                            break

                elif selected == '3':
                    while True:
                        input_menu()
                        selected = input("Choose one.. ")
                        if selected == '1':
                            nu_desc = input("Input new description.. ")
                            print(nu_desc)
                            cpus.update('B4', nu_desc)
                            print("Success! Description updated to " +
                                  nu_desc)
                            time.sleep(4)
                        if selected == '2':
                            nu_qty = input("Input new quantity.. ")
                            print(nu_qty)
                            cpus.update('E4', (int(nu_qty)))
                            print("Success! Quantity updated to " +
                                  nu_qty)
                            time.sleep(4)
                        if selected == '3':
                            nu_price = input("Input new price.. ")
                            print(nu_price)
                            cpus.update('F4', (float(nu_price)))
                            print("Success! Price updated to " +
                                  nu_price)
                            time.sleep(4)
                        if selected == '4':
                            break

                elif selected == '4':
                    while True:
                        input_menu()
                        selected = input("Choose one.. ")
                        if selected == '1':
                            nu_desc = input("Input new description.. ")
                            print(nu_desc)
                            cpus.update('B5', nu_desc)
                            print("Success! Description updated to " +
                                  nu_desc)
                            time.sleep(4)
                        if selected == '2':
                            nu_qty = input("Input new quantity.. ")
                            print(nu_qty)
                            cpus.update('E5', (int(nu_qty)))
                            print("Success! Quantity updated to " +
                                  nu_qty)
                            time.sleep(4)
                        if selected == '3':
                            nu_price = input("Input new price.. ")
                            print(nu_price)
                            cpus.update('F5', (float(nu_price)))
                            print("Success! Price updated to " +
                                  nu_price)
                            time.sleep(4)
                        if selected == '4':
                            break
                elif selected == 'exit':
                    clear()
                    time.sleep(4)
                    break

                else:
                    clear()
                    print("Not a valid selection choice. Try again.")
                    continue

        elif selected == '2':
            clear()
            time.sleep(4)

            def show_ram():
                data = ram.get_all_values()
                table = PrettyTable()
                table.field_names = data[0]
                for row in data[1:]:
                    table.add_row(row)
                print(table)
            slow_print(
                "Loading RAM currently in stock, please be patient...")
            while True:
                show_ram()
                selected = input("\nInput the number of your chosen RAM. "
                                 "\nType \"exit\" to return to console.")
                if selected == '1':
                    while True:
                        input_menu()
                        selected = input("Choose one.. ")
                        if selected == '1':
                            nu_desc = input("Input new description.. ")
                            print(nu_desc)
                            ram.update('B2', nu_desc)
                            print("Success! Description updated to " +
                                  nu_desc)
                            time.sleep(4)
                        if selected == '2':
                            nu_qty = input("Input new quantity.. ")
                            print(nu_qty)
                            ram.update('C2', (int(nu_qty)))
                            print("Success! Quantity updated to " +
                                  nu_qty)
                            time.sleep(4)
                        if selected == '3':
                            nu_price = input("Input new price.. ")
                            print(nu_price)
                            ram.update('D2', (float(nu_price)))
                            print("Success! Price updated to " +
                                  nu_price)
                            time.sleep(4)
                        if selected == '4':
                            break

                elif selected == '2':
                    while True:
                        input_menu()
                        selected = input("Choose one.. ")
                        if selected == '1':
                            nu_desc = input("Input new description.. ")
                            print(nu_desc)
                            ram.update('B3', nu_desc)
                            print("Success! Description updated to " +
                                  nu_desc)
                            time.sleep(4)
                        if selected == '2':
                            nu_qty = input("Input new quantity.. ")
                            print(nu_qty)
                            ram.update('C3', (int(nu_qty)))
                            print("Success! Quantity updated to " +
                                  nu_qty)
                            time.sleep(4)
                        if selected == '3':
                            nu_price = input("Input new price.. ")
                            print(nu_price)
                            ram.update('D3', (float(nu_price)))
                            print("Success! Price updated to " +
                                  nu_price)
                            time.sleep(4)
                        if selected == '4':
                            break

                elif selected == '3':
                    while True:
                        input_menu()
                        selected = input("Choose one.. ")
                        if selected == '1':
                            nu_desc = input("Input new description.. ")
                            print(nu_desc)
                            ram.update('B4', nu_desc)
                            print("Success! Description updated to " +
                                  nu_desc)
                            time.sleep(4)
                        if selected == '2':
                            nu_qty = input("Input new quantity.. ")
                            print(nu_qty)
                            ram.update('C4', (int(nu_qty)))
                            print("Success! Quantity updated to " +
                                  nu_qty)
                            time.sleep(4)
                        if selected == '3':
                            nu_price = input("Input new price.. ")
                            print(nu_price)
                            ram.update('D4', (float(nu_price)))
                            print("Success! Price updated to " +
                                  nu_price)
                            time.sleep(4)
                        if selected == '4':
                            break

                elif selected == '4':
                    while True:
                        input_menu()
                        selected = input("Choose one.. ")
                        if selected == '1':
                            nu_desc = input("Input new description.. ")
                            print(nu_desc)
                            ram.update('B5', nu_desc)
                            print("Success! Description updated to " +
                                  nu_desc)
                            time.sleep(4)
                        if selected == '2':
                            nu_qty = input("Input new quantity.. ")
                            print(nu_qty)
                            ram.update('C5', (int(nu_qty)))
                            print("Success! Quantity updated to " +
                                  nu_qty)
                            time.sleep(4)
                        if selected == '3':
                            nu_price = input("Input new price.. ")
                            print(nu_price)
                            ram.update('D5', (float(nu_price)))
                            print("Success! Price updated to " +
                                  nu_price)
                            time.sleep(4)
                        if selected == '4':
                            break

                elif selected == 'exit':
                    clear()
                    time.sleep(4)
                    break

                else:
                    clear()
                    print("Not a valid selection choice. Try again.")
                    continue

        elif selected == '3':
            clear()
            time.sleep(4)

            def show_gpus():
                data = gpus.get_all_values()
                table = PrettyTable()
                table.field_names = data[0]
                for row in data[1:]:
                    table.add_row(row)
                print(table)
            slow_print(
                "Loading GPUs currently in stock, please be patient...")
            while True:
                show_gpus()
                selected = input("\nInput the number of your chosen gpus. "
                                 "\nType \"exit\" to return to console.")
                if selected == '1':
                    while True:
                        input_menu()
                        selected = input("Choose one.. ")
                        if selected == '1':
                            nu_desc = input("Input new description.. ")
                            print(nu_desc)
                            gpus.update('B2', nu_desc)
                            print("Success! Description updated to " +
                                  nu_desc)
                            time.sleep(4)
                        if selected == '2':
                            nu_qty = input("Input new quantity.. ")
                            print(nu_qty)
                            gpus.update('C2', (int(nu_qty)))
                            print("Success! Quantity updated to " +
                                  nu_qty)
                            time.sleep(4)
                        if selected == '3':
                            nu_price = input("Input new price.. ")
                            print(nu_price)
                            gpus.update('D2', (float(nu_price)))
                            print("Success! Price updated to " +
                                  nu_price)
                            time.sleep(4)
                        if selected == '4':
                            break

                elif selected == '2':
                    while True:
                        input_menu()
                        selected = input("Choose one.. ")
                        if selected == '1':
                            nu_desc = input("Input new description.. ")
                            print(nu_desc)
                            gpus.update('B3', nu_desc)
                            print("Success! Description updated to " +
                                  nu_desc)
                            time.sleep(4)
                        if selected == '2':
                            nu_qty = input("Input new quantity.. ")
                            print(nu_qty)
                            gpus.update('C3', (int(nu_qty)))
                            print("Success! Quantity updated to " +
                                  nu_qty)
                            time.sleep(4)
                        if selected == '3':
                            nu_price = input("Input new price.. ")
                            print(nu_price)
                            gpus.update('D3', (float(nu_price)))
                            print("Success! Price updated to " +
                                  nu_price)
                            time.sleep(4)
                        if selected == '4':
                            break

                elif selected == '3':
                    while True:
                        input_menu()
                        selected = input("Choose one.. ")
                        if selected == '1':
                            nu_desc = input("Input new description.. ")
                            print(nu_desc)
                            gpus.update('B4', nu_desc)
                            print("Success! Description updated to " +
                                  nu_desc)
                            time.sleep(4)
                        if selected == '2':
                            nu_qty = input("Input new quantity.. ")
                            print(nu_qty)
                            gpus.update('C4', (int(nu_qty)))
                            print("Success! Quantity updated to " +
                                  nu_qty)
                            time.sleep(4)
                        if selected == '3':
                            nu_price = input("Input new price.. ")
                            print(nu_price)
                            gpus.update('D4', (float(nu_price)))
                            print("Success! Price updated to " +
                                  nu_price)
                            time.sleep(4)
                        if selected == '4':
                            break

                elif selected == '4':
                    while True:
                        input_menu()
                        selected = input("Choose one.. ")
                        if selected == '1':
                            nu_desc = input("Input new description.. ")
                            print(nu_desc)
                            gpus.update('B5', nu_desc)
                            print("Success! Description updated to " +
                                  nu_desc)
                            time.sleep(4)
                        if selected == '2':
                            nu_qty = input("Input new quantity.. ")
                            print(nu_qty)
                            gpus.update('C5', (int(nu_qty)))
                            print("Success! Quantity updated to " +
                                  nu_qty)
                            time.sleep(4)
                        if selected == '3':
                            nu_price = input("Input new price.. ")
                            print(nu_price)
                            gpus.update('D5', (float(nu_price)))
                            print("Success! Price updated to " +
                                  nu_price)
                            time.sleep(4)
                        if selected == '4':
                            break
                elif selected == '5':
                    while True:
                        input_menu()
                        selected = input("Choose one.. ")
                        if selected == '1':
                            nu_desc = input("Input new description.. ")
                            print(nu_desc)
                            gpus.update('B6', nu_desc)
                            print("Success! Description updated to " +
                                  nu_desc)
                            time.sleep(4)
                        if selected == '2':
                            nu_qty = input("Input new quantity.. ")
                            print(nu_qty)
                            gpus.update('C6', (int(nu_qty)))
                            print("Success! Quantity updated to " +
                                  nu_qty)
                            time.sleep(4)
                        if selected == '3':
                            nu_price = input("Input new price.. ")
                            print(nu_price)
                            gpus.update('D6', (float(nu_price)))
                            print("Success! Price updated to " +
                                  nu_price)
                            time.sleep(4)
                        if selected == '4':
                            break
                elif selected == 'exit':
                    clear()
                    time.sleep(4)
                    break

                else:
                    clear()
                    print("Not a valid selection choice. Try again.")
                    continue

        elif selected == '4':
            clear()
            time.sleep(4)

            def show_hdd():
                data = hdd.get_all_values()
                table = PrettyTable()
                table.field_names = data[0]
                for row in data[1:]:
                    table.add_row(row)
                print(table)
            slow_print(
                "Loading HDDs currently in stock, please be patient...")
            while True:
                show_hdd()
                selected = input("\nInput the number of your chosen HDD. "
                                 "\nType \"exit\" to return to console.")
                if selected == '1':
                    while True:
                        input_menu()
                        selected = input("Choose one.. ")
                        if selected == '1':
                            nu_desc = input("Input new description.. ")
                            print(nu_desc)
                            hdd.update('B2', nu_desc)
                            print("Success! Description updated to " +
                                  nu_desc)
                            time.sleep(4)
                        if selected == '2':
                            nu_qty = input("Input new quantity.. ")
                            print(nu_qty)
                            hdd.update('C2', (int(nu_qty)))
                            print("Success! Quantity updated to " +
                                  nu_qty)
                            time.sleep(4)
                        if selected == '3':
                            nu_price = input("Input new price.. ")
                            print(nu_price)
                            hdd.update('D2', (float(nu_price)))
                            print("Success! Price updated to " +
                                  nu_price)
                            time.sleep(4)
                        if selected == '4':
                            break

                elif selected == '2':
                    while True:
                        input_menu()
                        selected = input("Choose one.. ")
                        if selected == '1':
                            nu_desc = input("Input new description.. ")
                            print(nu_desc)
                            hdd.update('B3', nu_desc)
                            print("Success! Description updated to " +
                                  nu_desc)
                            time.sleep(4)
                        if selected == '2':
                            nu_qty = input("Input new quantity.. ")
                            print(nu_qty)
                            hdd.update('C3', (int(nu_qty)))
                            print("Success! Quantity updated to " +
                                  nu_qty)
                            time.sleep(4)
                        if selected == '3':
                            nu_price = input("Input new price.. ")
                            print(nu_price)
                            hdd.update('D3', (float(nu_price)))
                            print("Success! Price updated to " +
                                  nu_price)
                            time.sleep(4)
                        if selected == '4':
                            break

                elif selected == '3':
                    while True:
                        input_menu()
                        selected = input("Choose one.. ")
                        if selected == '1':
                            nu_desc = input("Input new description.. ")
                            print(nu_desc)
                            hdd.update('B4', nu_desc)
                            print("Success! Description updated to " +
                                  nu_desc)
                            time.sleep(4)
                        if selected == '2':
                            nu_qty = input("Input new quantity.. ")
                            print(nu_qty)
                            hdd.update('C4', (int(nu_qty)))
                            print("Success! Quantity updated to " +
                                  nu_qty)
                            time.sleep(4)
                        if selected == '3':
                            nu_price = input("Input new price.. ")
                            print(nu_price)
                            hdd.update('D4', (float(nu_price)))
                            print("Success! Price updated to " +
                                  nu_price)
                            time.sleep(4)
                        if selected == '4':
                            break

                elif selected == '4':
                    while True:
                        input_menu()
                        selected = input("Choose one.. ")
                        if selected == '1':
                            nu_desc = input("Input new description.. ")
                            print(nu_desc)
                            hdd.update('B5', nu_desc)
                            print("Success! Description updated to " +
                                  nu_desc)
                            time.sleep(4)
                        if selected == '2':
                            nu_qty = input("Input new quantity.. ")
                            print(nu_qty)
                            hdd.update('C5', (int(nu_qty)))
                            print("Success! Quantity updated to " +
                                  nu_qty)
                            time.sleep(4)
                        if selected == '3':
                            nu_price = input("Input new price.. ")
                            print(nu_price)
                            hdd.update('D5', (float(nu_price)))
                            print("Success! Price updated to " +
                                  nu_price)
                            time.sleep(4)
                        if selected == '4':
                            break
                elif selected == '4':
                    while True:
                        input_menu()
                        selected = input("Choose one.. ")
                        if selected == '1':
                            nu_desc = input("Input new description.. ")
                            print(nu_desc)
                            hdd.update('B6', nu_desc)
                            print("Success! Description updated to " +
                                  nu_desc)
                            time.sleep(4)
                        if selected == '2':
                            nu_qty = input("Input new quantity.. ")
                            print(nu_qty)
                            hdd.update('C6', (int(nu_qty)))
                            print("Success! Quantity updated to " +
                                  nu_qty)
                            time.sleep(4)
                        if selected == '3':
                            nu_price = input("Input new price.. ")
                            print(nu_price)
                            hdd.update('D6', (float(nu_price)))
                            print("Success! Price updated to " +
                                  nu_price)
                            time.sleep(4)
                        if selected == '4':
                            break
                elif selected == 'exit':
                    clear()
                    time.sleep(4)
                    break

                else:
                    clear()
                    print("Not a valid selection choice. Try again.")
                    continue

        elif selected == '5':
            slow_print("Are you sure?")
            slow_print("1 -- Yes, exit now")
            slow_print("2 -- Return to main console")
            slow_print("3 -- Go to user section")
            selected = input("")
            if selected == '1':
                close_prog()
            elif selected == '2':
                admin_console()
            elif selected == '3':
                clear()
                main_menu()


def main_menu():
    """Displays the main menu and holds most of the program functions."""
    global CPU_SELECTED
    global RAM_SELECTED
    global GPU_SELECTED
    global HDD_SELECTED
    while True:
        if CPU_SELECTED >= 1 and GPU_SELECTED >= 1 and RAM_SELECTED >= \
                1 and HDD_SELECTED >= 1:
            cpu_choice = partslist.acell('A2').value
            ram_choice = partslist.acell('B2').value
            gpu_choice = partslist.acell('C2').value
            hdd_choice = partslist.acell('D2').value
            total_price = partslist.acell('E7').value
            slow_print("Loading parts selection.... ")
            print(
                "CPU = " +
                cpu_choice +
                "\n" +
                "RAM = " +
                ram_choice +
                "\n" +
                "GPU = " +
                gpu_choice +
                "\n" +
                "HDD = " +
                hdd_choice)
            print("Calculating total price....")
            time.sleep(4)
            print("€" + total_price)
            time.sleep(8)
            clear()
            slow_print("1 -- Return to start")
            slow_print("2 -- Exit Web Application")
            selected = input("Please pick from the above options... ")
            if selected == '1':
                CPU_SELECTED = 0
                GPU_SELECTED = 0
                RAM_SELECTED = 0
                HDD_SELECTED = 0
                clear()
                print("Returning to main menu....")
                continue
            elif selected == '2':
                close_prog()
        else:
            menu_logo = pyfiglet.figlet_format("MAIN MENU")
            print(menu_logo)
            slow_print("1 -- CPU Stocklist")
            slow_print("2 -- RAM Stocklist")
            slow_print("3 -- GPU Stocklist")
            slow_print("4 -- Storage Drive Stocklist")
            slow_print("5 -- View Parts List")
            slow_print("6 -- Exit Store")

            selected = input("\nPlease pick from the above options... ")
            if selected == '1':
                clear()
                time.sleep(4)

                def show_cpus():
                    data = cpus.get_all_values()
                    table = PrettyTable()
                    table.field_names = data[0]
                    for row in data[1:]:
                        table.add_row(row)
                    print(table)
                slow_print(
                    "Loading CPUs currently in stock, please be patient...")
                while True:
                    show_cpus()
                    print("Loaded. To exit, type \"exit\".")
                    new_qty = 0
                    choice = None
                    selected = input("\nInput the number of your chosen CPU.")
                    if selected == '1':
                        this_qty = cpus.acell('E2').value
                        if this_qty == '0':
                            print("Out of stock.")
                            time.sleep(1.5)
                        elif this_qty >= '1':
                            choice = cpus.cell(2, 2).value
                            cpu_price = float(cpus.cell(2, 6).value)
                            CPU_SELECTED = CPU_SELECTED + 1
                            new_qty = int(this_qty) - 1
                            cpus.update('E2', new_qty)
                    elif selected == '2':
                        this_qty = cpus.acell('E3').value
                        if this_qty == '0':
                            print("Out of stock.")
                            time.sleep(1.5)
                        elif this_qty >= '1':
                            choice = cpus.cell(3, 2).value
                            cpu_price = float(cpus.cell(3, 6).value)
                            CPU_SELECTED = CPU_SELECTED + 1
                            new_qty = int(this_qty) - 1
                            cpus.update('E3', new_qty)
                    elif selected == '3':
                        this_qty = cpus.acell('E4').value
                        if this_qty == '0':
                            print("Out of stock.")
                            time.sleep(1.5)
                        elif this_qty >= '1':
                            choice = cpus.cell(4, 2).value
                            cpu_price = float(cpus.cell(4, 6).value)
                            CPU_SELECTED = CPU_SELECTED + 1
                            new_qty = int(this_qty) - 1
                            cpus.update('E4', new_qty)
                    elif selected == '4':
                        this_qty = cpus.acell('E5').value
                        if this_qty == '0':
                            print("Out of stock.")
                            time.sleep(1.5)
                        elif this_qty >= '1':
                            choice = cpus.cell(5, 2).value
                            cpu_price = float(cpus.cell(5, 6).value)
                            CPU_SELECTED = CPU_SELECTED + 1
                            new_qty = int(this_qty) - 1
                            cpus.update('E5', new_qty)
                    elif selected == "exit":
                        break
                    elif selected >= '5' or selected < '1':
                        print("Not a valid selection choice. "
                              "Please try again.")
                        time.sleep(2)
                        clear()
                    elif selected.isalpha() and selected != "exit":
                        print("Invalid input. Try again.")
                        time.sleep(3)
                        clear()
                    if choice:
                        partslist.update('A2', choice)
                        partslist.update('E3', cpu_price)
                        print("\nSuccess! " + choice + " added to basket."
                              "\n" + str(new_qty) + " left in stock.")
                        time.sleep(4)
                        clear()
                        break

            elif selected == '2':
                clear()
                time.sleep(4)

                def show_ram():
                    data = ram.get_all_values()
                    table = PrettyTable()
                    table.field_names = data[0]
                    for row in data[1:]:
                        table.add_row(row)
                    print(table)
                slow_print(
                    "Loading RAM currently in stock, please be patient...")
                while True:
                    show_ram()
                    choice = None
                    selected = input("Input the number of your chosen RAM.")
                    if selected == '1':
                        this_qty = ram.acell('C2').value
                        if this_qty == '0':
                            print("Out of stock.")
                            time.sleep(1.5)
                        elif this_qty >= '1':
                            choice = ram.cell(2, 2).value
                            ram_price = float(ram.cell(2, 4).value)
                            RAM_SELECTED = RAM_SELECTED + 1
                            new_qty = int(this_qty) - 1
                            ram.update('C2', new_qty)
                    elif selected == '2':
                        this_qty = ram.acell('C3').value
                        if this_qty == '0':
                            print("Out of stock.")
                            time.sleep(1.5)
                        elif this_qty >= '1':
                            choice = ram.cell(3, 2).value
                            ram_price = float(ram.cell(3, 4).value)
                            RAM_SELECTED = RAM_SELECTED + 1
                            new_qty = int(this_qty) - 1
                            ram.update('C3', new_qty)
                    elif selected == '3':
                        this_qty = ram.acell('C4').value
                        if this_qty == '0':
                            print("Out of stock.")
                            time.sleep(1.5)
                        elif this_qty >= '1':
                            choice = ram.cell(4, 2).value
                            ram_price = float(ram.cell(4, 4).value)
                            RAM_SELECTED = RAM_SELECTED + 1
                            new_qty = int(this_qty) - 1
                            ram.update('C4', new_qty)
                    elif selected == '4':
                        this_qty = ram.acell('C5').value
                        if this_qty == '0':
                            print("Out of stock.")
                            time.sleep(1.5)
                        elif this_qty >= '1':
                            choice = ram.cell(5, 2).value
                            ram_price = float(ram.cell(5, 4).value)
                            RAM_SELECTED = RAM_SELECTED + 1
                            new_qty = int(this_qty) - 1
                            ram.update('C5', new_qty)
                    else:
                        print("Not a valid selection choice. "
                              "Please try again.")
                        time.sleep(5)
                        clear()
                    if choice:
                        partslist.update('B2', choice)
                        partslist.update('E4', ram_price)
                        print("\nSuccess! " + choice + " added to basket."
                              "\n" + str(new_qty) + " left in stock.")
                        time.sleep(4)
                        clear()
                        break
            elif selected == '3':
                clear()
                time.sleep(4)

                def show_gpus():
                    data = gpus.get_all_values()
                    table = PrettyTable()
                    table.field_names = data[0]
                    for row in data[1:]:
                        table.add_row(row)
                    print(table)
                slow_print(
                    "Loading GPUs currently in stock, please be patient...")
                while True:
                    show_gpus()
                    choice = None
                    selected = input("Input the number of your chosen GPU.")
                    if selected == '1':
                        this_qty = gpus.acell('C2').value
                        if this_qty == '0':
                            print("Out of stock.")
                            time.sleep(1.5)
                        elif this_qty >= '1':
                            choice = gpus.cell(2, 2).value
                            gpus_price = float(gpus.cell(2, 4).value)
                            GPU_SELECTED = GPU_SELECTED + 1
                            new_qty = int(this_qty) - 1
                            gpus.update('C2', new_qty)
                    elif selected == '2':
                        this_qty = gpus.acell('C3').value
                        if this_qty == '0':
                            print("Out of stock.")
                            time.sleep(1.5)
                        elif this_qty >= '1':
                            choice = gpus.cell(3, 2).value
                            gpus_price = float(gpus.cell(3, 4).value)
                            GPU_SELECTED = GPU_SELECTED + 1
                            new_qty = int(this_qty) - 1
                            gpus.update('C3', new_qty)
                    elif selected == '3':
                        this_qty = gpus.acell('C4').value
                        if this_qty == '0':
                            print("Out of stock.")
                            time.sleep(1.5)
                        elif this_qty >= '1':
                            choice = gpus.cell(4, 2).value
                            gpus_price = float(gpus.cell(4, 4).value)
                            GPU_SELECTED = GPU_SELECTED + 1
                            new_qty = int(this_qty) - 1
                            gpus.update('C4', new_qty)
                    elif selected == '4':
                        this_qty = gpus.acell('C5').value
                        if this_qty == '0':
                            print("Out of stock.")
                            time.sleep(1.5)
                        elif this_qty >= '1':
                            choice = gpus.cell(5, 2).value
                            gpus_price = float(gpus.cell(5, 4).value)
                            GPU_SELECTED = GPU_SELECTED + 1
                            new_qty = int(this_qty) - 1
                            gpus.update('C5', new_qty)
                    elif selected == '5':
                        this_qty = gpus.acell('C6').value
                        if this_qty == '0':
                            print("Out of stock.")
                            time.sleep(1.5)
                        elif this_qty >= '1':
                            choice = gpus.cell(6, 2).value
                            gpus_price = float(gpus.cell(6, 4).value)
                            GPU_SELECTED = GPU_SELECTED + 1
                            new_qty = int(this_qty) - 1
                            gpus.update('C6', new_qty)
                    else:
                        print("Not a valid selection choice. "
                              "Please try again.")
                        time.sleep(2)
                        clear()
                    if choice:
                        partslist.update('C2', choice)
                        partslist.update('E5', gpus_price)
                        print("\nSuccess! " + choice + " added to basket."
                              "\n" + str(new_qty) + " left in stock.")
                        time.sleep(4)
                        clear()
                        break
            elif selected == '4':
                clear()
                time.sleep(4)

                def show_hdd():
                    data = hdd.get_all_values()
                    table = PrettyTable()
                    table.field_names = data[0]
                    for row in data[1:]:
                        table.add_row(row)
                    print(table)
                slow_print(
                    "Loading HDDs currently in stock, please be patient...")
                while True:
                    show_hdd()
                    selected = input("\nInput the ID of your chosen HDD. ")
                    if selected == '1':
                        this_qty = hdd.acell('C2').value
                        if this_qty == '0':
                            print("Out of stock.")
                            time.sleep(1.5)
                        elif this_qty >= '1':
                            choice = hdd.cell(2, 2).value
                            hdd_price = float(hdd.cell(2, 4).value)
                            HDD_SELECTED = HDD_SELECTED + 1
                            new_qty = int(this_qty) - 1
                            hdd.update('C2', new_qty)
                    elif selected == '2':
                        this_qty = hdd.acell('C3').value
                        if this_qty == '0':
                            print("Out of stock.")
                            time.sleep(1.5)
                        elif this_qty >= '1':
                            choice = hdd.cell(3, 2).value
                            hdd_price = float(hdd.cell(3, 4).value)
                            HDD_SELECTED = HDD_SELECTED + 1
                            new_qty = int(this_qty) - 1
                            hdd.update('C3', new_qty)
                    elif selected == '3':
                        this_qty = hdd.acell('C4').value
                        if this_qty == '0':
                            print("Out of stock.")
                            time.sleep(1.5)
                        elif this_qty >= '1':
                            choice = hdd.cell(4, 2).value
                            hdd_price = float(hdd.cell(4, 4).value)
                            HDD_SELECTED = HDD_SELECTED + 1
                            new_qty = int(this_qty) - 1
                            hdd.update('C4', new_qty)
                    elif selected == '4':
                        this_qty = hdd.acell('C5').value
                        if this_qty == '0':
                            print("Out of stock.")
                            time.sleep(1.5)
                        elif this_qty >= '1':
                            choice = hdd.cell(5, 2).value
                            hdd_price = float(hdd.cell(5, 4).value)
                            HDD_SELECTED = HDD_SELECTED + 1
                            new_qty = int(this_qty) - 1
                            hdd.update('C5', new_qty)
                    elif selected == '5':
                        this_qty = hdd.acell('C6').value
                        if this_qty == '0':
                            print("Out of stock.")
                            time.sleep(1.5)
                        elif this_qty >= '1':
                            choice = hdd.cell(6, 2).value
                            hdd_price = float(hdd.cell(6, 4).value)
                            HDD_SELECTED = HDD_SELECTED + 1
                            new_qty = int(this_qty) - 1
                            hdd.update('C6', new_qty)
                    else:
                        print("Not a valid selection choice. "
                              "Please try again.")
                        time.sleep(2)
                        clear()
                    if choice:
                        partslist.update('D2', choice)
                        partslist.update('E6', hdd_price)
                        print("\nSuccess! " + choice + " added to basket."
                              "\n" + str(new_qty) + " left in stock.")
                        time.sleep(4)
                        clear()
                        break
            elif selected == '5':
                clear()
                cpu_choice = partslist.acell('A2').value
                ram_choice = partslist.acell('B2').value
                gpu_choice = partslist.acell('C2').value
                hdd_choice = partslist.acell('D2').value
                total_price = partslist.acell('E7').value

                if cpu_choice and CPU_SELECTED >= 1:
                    print(cpu_choice)

                else:
                    print("No CPU selected yet.")

                if ram_choice and RAM_SELECTED >= 1:
                    print(ram_choice)

                else:
                    print("No RAM selected yet.")

                if gpu_choice and GPU_SELECTED >= 1:
                    print(gpu_choice)

                else:
                    print("No GPU selected yet.")

                if hdd_choice and HDD_SELECTED >= 1:
                    print(hdd_choice)

                else:
                    print("No HDD selected yet.")

                time.sleep(5)

                slow_print("\n1 -- Return to main menu")
                slow_print("2 -- View item prices and subtotal")
                selected = input("Please pick from the above options... ")

                if selected == '1':
                    clear()
                    main_menu()

                elif selected == '2':
                    clear()
                    if CPU_SELECTED >= 1:
                        price_cpu = partslist.acell('E3').value
                        print(cpu_choice + " costs €" + price_cpu)

                    else:
                        print("No CPU selected yet.")

                    if RAM_SELECTED >= 1:
                        price_ram = partslist.acell('E4').value
                        print(ram_choice + " costs €" + price_ram)

                    else:
                        print("No RAM selected yet.")

                    if GPU_SELECTED >= 1:
                        price_gpu = partslist.acell('E5').value
                        print(gpu_choice + " costs €" + price_gpu)

                    else:
                        print("No GPU selected yet.")

                    if HDD_SELECTED >= 1:
                        price_hdd = partslist.acell('E6').value
                        print(hdd_choice + " costs €" + price_hdd)

                    else:
                        print("No HDD selected yet.")

                    if CPU_SELECTED >= 1 or GPU_SELECTED >= 1 or \
                            RAM_SELECTED >= 1 or HDD_SELECTED >= 1:
                        print("Subtotal: €" + total_price)

                    else:
                        print("\nNo parts are selected,"
                              " no subtotal to display.")

                    time.sleep(4)

                    print("\nReturn to main menu?")
                    slow_print("1 -- Yes")
                    slow_print("2 -- No")
                    selected = input("Please pick from the above options. ")

                    if selected == '1':
                        main_menu()
                    elif selected == '2':
                        clear()
                        print("Where else do you think you can go from here??")
                        ban = pyfiglet.figlet_format(
                            "You have \n been \n banned", font="doom")
                        print(ban)
                        time.sleep(4)
                        sys.exit()

                continue

            elif selected == '6':
                slow_print("Are you sure?")
                slow_print("1 -- Yes, exit now")
                slow_print("2 -- Return to main menu")
                selected = input("")
                if selected == '1':
                    close_prog()
                elif selected == '2':
                    main_menu()


def shop_intro():
    """Shop intro and emptying price values before program initialization."""
    zeroprice = int(0)
    partslist.update('E3', zeroprice)
    partslist.update('E4', zeroprice)
    partslist.update('E5', zeroprice)
    partslist.update('E6', zeroprice)
    print("\n")
    logo = pyfiglet.figlet_format("DCP", font="roman")
    print(logo)
    print("(C)1992 DIGITAL COMPUTER PARTS LTD")
    slow_print("POWERED BY MINITEL")
    slow_print("==========================")
    print("\nPRESS ENTER TO BEGIN")
    print("\nTYPE \"ADMIN\" TO ENTER ADMIN CONSOLE")
    enter = str(input(""))
    console_entry = ['admin', 'ADMIN']
    if enter in console_entry:
        slow_print("Proceeding to login screen...")
        clear()
        admin_verify()
    else:
        slow_print("Proceeding...")
        clear()
        main_menu()


shop_intro()
