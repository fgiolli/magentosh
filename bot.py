from json.decoder import JSONDecoder
import random
import win32gui
import json
import ctypes
import pyautogui
import time
from PIL import ImageGrab
import numpy as np

def cargarData():
    jsond = open('test.json') #Abre el archivo
    data = json.load(jsond) #Vuelca los datos en la variable
    return data

def login(data):
    
    #Carga las posiciones de los input y botones a clickear
    labelUser = pyautogui.locateOnScreen("user.png")
    labelPass = pyautogui.locateOnScreen("pass.png")
    btnJugar = pyautogui.locateOnScreen("jugar.png")
    
    pyautogui.click(labelUser)
    pyautogui.typewrite(data["user"])
    
    pyautogui.click(labelPass)
    pyautogui.typewrite(data["password"] + '\n')
    print("Sleeping for 10 seconds")
    time.sleep(10.5)
    pyautogui.click(btnJugar)
    
    while(pyautogui.locateOnScreen("juega.png") == None):
        print("Sleeping for 20 seconds or more, wait until program start")
        time.sleep(20)
    print("Launcher ready")

def playIA():
    pyautogui.click("juega.png")
    time.sleep(1.5)
    coopia = pyautogui.locateOnScreen("coopia.png")
    pyautogui.click(coopia)
    time.sleep(1.5)
    coopia2 =pyautogui.locateOnScreen("coopia2.png")
    pyautogui.click(coopia2)
    time.sleep(1.5)
    coopia3 =pyautogui.locateOnScreen("coopia3.png")
    pyautogui.click(coopia3)
    print("In Lobby")
    time.sleep(1.5)
    coopia4 =pyautogui.locateOnScreen("coopia4.png")
    pyautogui.click(coopia4)
    while(pyautogui.locateOnScreen("aceptar.png") == None):
        print("Waiting for a game")
        time.sleep(2)
    print("Game found!")
    pyautogui.click("aceptar.png")
    time.sleep(20)
    
def champ_pick():
    champs = {'ashe': None, 'kaisa': None, 'sivir': None}
    available_champs = {}
    pyautogui.click("adc.png")
    time.sleep(0.5)
    for x in champs:
        champs[x] = pyautogui.locateOnScreen(x + ".png")
        if champs[x] != None:
            available_champs[x] = champs[x]
    return pyautogui.click(random.choice(available_champs.values()))
    

def get_window_info():
    window_info = {}
    win32gui.EnumWindows(set_window_coordinates, window_info)
    return window_info

def set_window_coordinates(hwnd, window_info):
    if win32gui.IsWindowVisible(hwnd):
        if windows_name in win32gui.GetWindowText(hwnd):
            rect = win32gui.GetWindowRect(hwnd)
            x = rect[0]
            y = rect[1]
            w = rect[2] - x
            h = rect[3] - y
            window_info['x'] = x
            window_info['y'] = y
            window_info['x2'] = rect[2]
            window_info['y2'] = rect[3]
            window_info['width'] = w
            window_info['height'] = h
            window_info['name'] = win32gui.GetWindowText(hwnd)
            print(win32gui.GetWindowText(hwnd))
            win32gui.SetForegroundWindow(hwnd)


def get_screen(x1, y1, x2, y2):
    box = (x1 + 8, y1 + 30, x2 - 8, y2)
    screen = ImageGrab.grab(box)
    img = np.array(screen.getdata(), dtype=np.uint8).reshape(
        (screen.size[1], screen.size[0], 3))
    return img

def initializeLogin():
    data = cargarData()
    login(data)
    time.sleep(1)

def interfaceison():
    interface = None
    interface_enable = False
    while(interface == None):
        interface = pyautogui.locateOnScreen("main.png")
        if(interface != None):
            interface_enable = True
            print("game start")
        else:
            print("wait until game start")
    return interface_enable

def push():
    time.sleep(3)
    pyautogui.press("a")
    time.sleep(1)
    pyautogui.moveTo(x=870, y=624)
    time.sleep(2)
    pyautogui.leftClick(x=870, y=624)
    time.sleep(5)
    pyautogui.leftClick()
    time.sleep(80)
    pyautogui.click(x=881, y=611)
    
def go_base():
    pyautogui.press("b")
    time.sleep(10)
    
#def get_selfHP():
    
def buy():
    pyautogui.press("p")
    time.sleep(1)
    pyautogui.click(x=312, y=324, clicks=2) #CLICK2BUY 452,
    pyautogui.press("p")

if __name__ == "__main__":
    ctypes.windll.user32.MessageBoxW(0, 'PLEASE, CHECK that your in-game mail be verified\n If its not, then you have to close windows(verify mail) manually', "BEFORE LOGIN", 1)
    windows_name = "League of Legends (TM) Client"
    
    initializeLogin() 
    playIA()
    champ_pick()
    time.sleep(120)
    cliente = get_window_info()
    time.sleep(1)
    buttonend = None
    while(interfaceison()):
        buttonend = pyautogui.locateOnScreen("buttonend.png")
        while(buttonend==None):
            buy()
            push()
            time.sleep(540)
            go_base()
            buttonend = pyautogui.locateOnScreen("buttonend.png")
            if(buttonend != None):
                pyautogui.click(buttonend)
        break
            
            
        
        
    
    
    #1178, 664 1 click
    #1191, 636 2 click
    #1224, 619 3 click