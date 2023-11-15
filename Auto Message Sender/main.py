import pyautogui
import time

belirli_saat = 20
belirli_dakika = 17

while True:
    saat, dakika = time.localtime().tm_hour, time.localtime().tm_min
    if saat == belirli_saat and dakika == belirli_dakika:
        metin = "Uyandım"
        pyautogui.write(metin)
        pyautogui.press('enter')
        break
    time.sleep(1)