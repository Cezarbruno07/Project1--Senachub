import pyautogui

pyautogui.press('win')
pyautogui.typewrite('notepad')
pyautogui.press('enter')

pyautogui.typewrite('Ola, Py')

pyautogui.hotkey("ctrl",'s')
pyautogui.typewrite('Exemplo.txt')
pyautogui.press('enter')