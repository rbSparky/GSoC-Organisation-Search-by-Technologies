import time
import pyautogui as g

cross, inspect, getdiv1, getdiv2, ashtml, notepad = (945,651), (1083,263), (1005,706), (1123,359), (1401,359), (89, 20)

def f(n):
    for i in range(n):
        g.click(cross)
        g.click(cross)
        g.click(inspect)
        g.click(getdiv1)
        g.click(getdiv2, button = 'right')
        g.click(ashtml)
        g.hotkey('ctrlleft', 'a', 'ctrlleft', 'c')
        g.click(notepad)
        g.hotkey('ctrlleft', 'v', 'ctrlleft', 's')

f(50)
