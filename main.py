import pyautogui, time
time.sleep(5)

filename = input("\n[+] Nombre del archivo que deseas spammear >> ")

f = open(filename, 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

      
