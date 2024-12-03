import v1
import color
import menu
import neopixel
import board
from threading import Thread,Lock


def inputFunc(pixels):
    choice=input("1 to Stop")
    if choice=="1":
        if menu.G.t.is_alive():
            menu.G.kill=True
    if choice=="2":
        if menu.G.bright<.9999:
            menu.G.bright+=.1
    if choice=="3":
        if menu.G.bright>0.001:
            menu.G.bright-=.1
        print(menu.G.bright)
    if choice=="4":
        if not(menu.G.t.is_alive()):
            menu.G.t = Thread(target=v1.RedGreen, args=(pixels,))
            menu.G.t.start()
        else:
            print("Already running, dummy")
    if choice=="5":
        if not(menu.G.t.is_alive()):
            menu.G.t = Thread(target=v1.WhiteFade, args=(pixels,))
            menu.G.t.start()
        else:
            print("Already running, dummy")
    if choice=="6":
        if not(menu.G.t.is_alive()):
            menu.G.t = Thread(target=v1.Rainbow, args=(pixels,))
            menu.G.t.start()
        else:
            print("Already running, dummy")
    if choice=="7":
        if menu.G.delay<5:
            menu.G.delay+=.1
    if choice=="8":
        if menu.G.delay>0:
            menu.G.delay-=.1
    return True


def main():
    pixels=neopixel.NeoPixel(board.D18,850,auto_write=False)
    menu.G.t = Thread(target=v1.RedGreen, args=(pixels,))
    menu.G.t.start()
    while inputFunc(pixels):
        pass

main()
