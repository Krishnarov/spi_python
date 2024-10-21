#import pywhatkit
import pyautogui
import time
time.sleep(10)
i=0
while i<=5:
	pyautogui.typewrite("i hate you"+str(i))
	pyautogui.press('enter')
	i=i+1
	



	#pywhatkit.sendwhatmsg('+917081250781', 'i heat you krishna', 21, 16)
