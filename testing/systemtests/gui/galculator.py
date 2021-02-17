import pyautogui

pyautogui.PAUSE = 0.2   # pause between actions

# open: F / Accessories / Galculator

# open terminal
pyautogui.click(183, 192) # [C]
pyautogui.click(39,351) # 1
pyautogui.click(39,390) # 0
pyautogui.click(39,390) # 0

pyautogui.click(228,387) # +
pyautogui.click(105,348) # 2
pyautogui.click(39,390)  # 0

pyautogui.click(297,366)  # =

# verification
location = pyautogui.locateOnScreen('Result120.png', region=(10,100, 330, 160))
center = pyautogui.center(location)
print(center)




