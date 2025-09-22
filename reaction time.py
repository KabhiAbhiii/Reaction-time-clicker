import keyboard
import pyautogui
import time

print("Move the mouse to desired position in 5 sec")
time.sleep(5)
x,y=pyautogui.position()
reply=input("Do you want to scan for a specific color?(Yes/no)")
if reply.lower()=="yes":
   print("Start and select the color of the reaction test's go color(press q to stop the code):")
   ss=pyautogui.screenshot()
   color=ss.getpixel((x,y))
elif reply.lower()=="no":
      print("No screenshot taken")
else :
 print("Invalid answer")
 exit()

while True:
 check=pyautogui.pixel(x,y)
 if check==color:
  pyautogui.click(x,y)
 if keyboard.is_pressed('t'):
   break
 time.sleep(.01) 
