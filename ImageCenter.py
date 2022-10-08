#Manipulação de tela e automação
import pyautogui
from time import sleep

def proc_png(imagem):
    thing2find = pyautogui.locateOnScreen(imagem,region=(18,3,271,26))
    if thing2find != None:
        a = True
    else:
        a = False
    return a

def automate_chrome():
    pyautogui.press('f5')
    sleep(3)
    a = pyautogui.locateOnScreen('makemyjob.png', region=region_makejob)
    pyautogui.click(a)
    print(a)
    pyautogui.hotkey('alt', "tab")  # VOLTAR PARA PÁGINA ANTERIOR (DE NOVAS TASKS EM PORTUGUÊS)
region_makejob = (1040, 400, 1350, 715)
im = pyautogui.screenshot('jobs.png',region=(19,4, 270, 25))
print(im)
pyautogui.alert('Lembre-se de ter 5 abas abertas no Chrome!\n'
                '      Deixe o Chrome atrás do PyCharm!')