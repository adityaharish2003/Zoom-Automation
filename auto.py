__author__ = "Aditya Harish"
from pynput.mouse import Controller
from pynput.mouse import Button
from pynput.keyboard import Controller as keycontrol,Key
from csv import reader
import os
import datetime
import subprocess
from time import sleep,localtime,strftime
print("[*]ZOOM AUTOMATION[*]")
mouse = Controller()
keyboard = keycontrol()
def getperiod():
    time_ref = ['08:00' , '08:45' , '09:30', '10:35', '11:20']
    current_time_str = strftime("%H:%M" , localtime())
    for i in range(5):
        if i == 0:
            if current_time_str < time_ref[i]:
                return 1
        elif time_ref[i-1] < current_time_str < time_ref[i]:
            return i + 1
    print("All Lessons Over")
    input("Press any button to continue.....")
    os._exit(0)
def enter(keyboard):
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def tab(keyboard):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
def leftclick(obj , coordinates):
    obj.position = coordinates
    obj.press(Button.left)
    obj.release(Button.left)
def get_id():
    day = datetime.datetime.now().strftime('%w')
    lesson = getperiod()-1
    if lesson == 0 or lesson == 3:
        subprocess.Popen("")#enter the path over here
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
    zoom_id = get_id()
    zoom_pass = get_pass(str(zoom_id))
    subprocess.run('clip' , universal_newlines=True , input=zoom_pass)
    leftclick(mouse , ((705, 326)))
    sleep(1.5)
    keyboard.type(zoom_id)
    for i in range(5):
        tab(keyboard)
        if i == 3 or i == 4:
            enter(keyboard)
    sleep(1.75)
    keyboard.type(zoom_pass)
    keyboard.press(Key.enter)
zoom()

