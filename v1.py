import math
import time
import menu
import color

def myModule(name):
    print("This is My Module : "+ name)

def dispTwoColors(color1,color2):
    print("color1: " + str(color1[0])+", "+str(color1[1])+", "+str(color1[2]))
    print("color2: " + str(color2[0])+", "+str(color2[1])+", "+str(color2[2]))

def swapNfade(pixels,color1,color2,direction,tofade):
    for x in range(256):
        if menu.G.kill:
            return
        fadefactor = x/255
        if direction == "up":
            fadefactor = 1-fadefactor
        if(not(tofade)):
            fadefactor=1
        comp = x % 2
        temp_color1 = [math.floor(x*fadefactor) for x in color1]
        temp_color2 = [math.floor(x*fadefactor) for x in color2]
        for i in range(len(pixels)):
            if menu.G.kill:
                return
            if i % 2 == comp:
                pixels[i]=[x*menu.G.bright for x in temp_color1]
            else:
                pixels[i]=[x*menu.G.bright for x in temp_color2]
        pixels.show()
        if(menu.G.delay > 0):
            time.sleep(menu.G.delay)

def Custom(pix,pattern,color1,color2,toFade):
   if pattern=="Solid":
       pix.fill(color1) 
       pix.show()
   if pattern=="Blink":
       print("Blink")
       while(not(menu.G.kill)):
           swapNfade(pix,color1,color2,"down",toFade)
           swapNfade(pix,color1,color2,"up",toFade)
       menu.G.kill=False
   if pattern=="Twinkle": 
       print("Twinkle")

def RedGreen(pix):
    while(not(menu.G.kill)):
        swapNfade(pix,color.RED,color.GREEN,"down",True)
        swapNfade(pix,color.RED,color.GREEN,"up",True)
    menu.G.kill=False

def WhiteFade(pix):
    while(not(menu.G.kill)):
        swapNfade(pix,color.WHITE_MED,color.WHITE_LOW,"down",True)
        swapNfade(pix,color.WHITE_MED,color.WHITE_LOW,"up",True)
    menu.G.kill=False

def Rainbow(pix):
    rainbow=[[1,2,3]]*850
    rainbow[0:122]=[color.RED]*122
    rainbow[122:244]=[color.ORANGE]*122
    rainbow[244:366]=[color.YELLOW]*122
    rainbow[366:488]=[color.GREEN]*122
    rainbow[488:610]=[color.BLUE]*122
    rainbow[610:732]=[color.PURPLE_LIGHT]*122
    rainbow[732:850]=[color.PURPLE]*128
    run=1
    ind=0
    while run>0:
        if menu.G.kill:
            menu.G.kill=False
            return
        temprb=rainbow[ind:]+rainbow[:ind]
        for i in range(850):
            if menu.G.kill:
                menu.G.kill=False
                return
            pix[i]=[math.floor(x*menu.G.bright) for x in temprb[i]]
        pix.show()
        if(menu.G.delay>0):
            time.sleep(menu.G.delay)
        ind=ind+1
        if(ind>849):
            ind=0


