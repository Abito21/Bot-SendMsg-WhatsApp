import time
import pywhatkit
import pyautogui

# Send Message
# Hp Number, Message, time_hour, time_minute
pywhatkit.sendwhatmsg("+62xxxxxxxxx", "Halo nama saya Abid Juliant Indraswara", 9, 33)
time.sleep(1)
# Click Message
pyautogui.click()
time.sleep(1)
# Enter Message
pyautogui.press('enter')