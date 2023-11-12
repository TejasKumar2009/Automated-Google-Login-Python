import pyautogui as pg
import time


def deleteAllText():
    pg.hotkey('ctrl', 'a')
    pg.press("backspace")

# Inputs
profiles_input = input("Does your Google Chrome has multiple profiles? (Note that multiple chrome profiles does not mean multiple google accounts)  (y/n): ")
username = input("Enter your google account email address : ")
password = input("Enter your google account password (Your password will be safe) : ")

# Common Code
pg.press('win')
time.sleep(1)
pg.write('chrome')
time.sleep(1)
pg.press('enter') 
time.sleep(2)
pg.hotkey('win', 'up')
pg.hotkey('win', 'down')
pg.hotkey('win', 'up')
time.sleep(2)

if (profiles_input=="y" or profiles_input=="Y"):
    pg.press("tab")

time.sleep(1)
pg.press("enter")
time.sleep(3)

# SignIn Main Code
pg.write("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button&theme=glif&flowName=GlifWebSignIn&flowEntry=SignUp")
time.sleep(3)
pg.press("enter")

time.sleep(4)
deleteAllText()
pg.write(username)
pg.press("enter")
time.sleep(4)
deleteAllText()
pg.write(password)
pg.press("enter")