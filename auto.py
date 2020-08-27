import pyautogui
import os
import datetime
import subprocess
from time import sleep,localtime,strftime
import argparse
import wordParser
from csv import reader
os.system('cls' if os.name == 'nt' else 'clear')
parser = argparse.ArgumentParser()
parser.add_argument('--m' , help='Select [Y/N] to choose for manual password entry , N by default')
parser.add_argument('--w' , help="Select [Y/N] to parse passwords from MsWord table , N by default")
args = parser.parse_args()
if args.w == 'y':
    try:
        print("Parsing data from MsWord......")
        wordParser.wordParse('wordID.docx')
        print("Data sucessfuly parsed , returning......")
        sleep(1.75)
        os.system('cls' if os.name == 'nt' else 'clear')
    except: 
        print("An error occured while parsing the .docx file")
try:
   with open('path.txt') as f:
       path = str(f.read())
except FileNotFoundError:
   with open('path.txt' , 'w') as f:
       path = input(r"Enter the path of Zoom.exe in the python format(using \\ instead of \) : ")
       f.write(path)
def getperiod():
    time_ref = ['08:05' , '08:47' , '09:32', '10:38', '11:23']
    current_time_str = strftime("%H:%M" , localtime())
    for i in range(5):
        if i == 0:
            if current_time_str < time_ref[i]:
                return 1
        elif time_ref[i-1] < current_time_str < time_ref[i]:
            return i + 1
    print("All Lessons Over")
    input("Press enter to continue.....")
    os._exit(0)                                                
def get_id():
    day = datetime.datetime.now().strftime('%w')
    lesson = getperiod()-1
    print("Opening Zoom.....")
    subprocess.Popen(path)#enter the path in this line
    sleep(4)
    with open('ids.csv') as id_csv:
        id_data = list(reader(id_csv))
    code = id_data[int(day)][lesson]
    return code
def get_pass(code):
    with open('pass.csv') as password:
        pass_data = list(reader(password))
    for i in pass_data:
        if code in i:
            code_pass = i[1]
    return code_pass
def zoom():
    if args.m == 'y':
        print("Manual id / password entry chosen....")
        zoom_id = input("Enter the zoom id: ")
        zoom_pass = input("Enter the meeting password: ")
    else:
        zoom_id = get_id()
        zoom_pass = get_pass(str(zoom_id))
    subprocess.run('clip' , universal_newlines=True , input=zoom_pass)
    print("Locating Join.....")
    while True:
        try:
            pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('joinButton.png')))
            print("Button Found!")
            break
        except:
            continue
    sleep(1.5)
    pyautogui.write(zoom_id)
    for i in range(5):
        pyautogui.press('tab')              
        if i == 3 or i == 4:
            pyautogui.press('enter')
    sleep(1.75)
    pyautogui.write(zoom_pass)
    pyautogui.press('enter')
if  __name__ == "__main__":
    zoom()
