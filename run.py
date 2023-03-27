# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


#import gspread
#from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

#CREDS = Credentials.from_service_account_file("creds.json")
#SCOPED_CREDS = CREDS.with_scopes(SCOPE)
#GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
#SHEET = GSPREAD_CLIENT.open('test_dat')

#sales = SHEET.worksheet('sales')

#data = sales.get_all_values()

#print(data)

import time

def slow_print(msg):
    print(msg)
    time.sleep(0.5)

def shop_intro():
    print("(C)1992 DIGITAL COMPUTER PARTS LTD")
    slow_print("POWERED BY MINITEL")
    slow_print("==========================")
    print("PRESS ANY KEY TO ENTER")
    input("")
    slow_print("Proceeding...")
    

shop_intro()