import tkinter as tk
from tkinter import colorchooser
from tktimepicker import AnalogPicker,AnalogThemes 
from tktimepicker import constants
import v1
import color
import menu
import neopixel
import board
import digitalio
import time
from threading import Thread,Lock

def control_star(pin_name, state):
    pin = digitalio.DigitalInOut(pin_name)
    pin.direction = digitalio.Direction.OUTPUT
    if state:
        pin.value = True
    else:
        pin.value = False

def rgb_to_grbhex(rgb):
    return '#%02x%02x%02x' % (rgb[1],rgb[0],rgb[2])
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def runtime_updateBrightness(newB):
    newbrightness=slider_brightness.get()/10
    print("Brightness: %f" % newbrightness)
    menu.G.bright=newbrightness

def runtime_updateSpeed(newB):
    newspeed=slider_speed.get()/10
    print("Speed: %d" % newspeed)
    menu.G.delay=newspeed

def load_preset_RedGreenFade():
    print("Load RG Fade")
    if menu.G.t!=0 and menu.G.t.is_alive():
        menu.G.kill=True
        time.sleep(.5)
    if menu.G.t!=0 and menu.G.t.is_alive():
        menu.G.kill=True
        time.sleep(.5)
    if menu.G.t!=0 and menu.G.t.is_alive():
        menu.G.kill=True
        time.sleep(.5)
    if menu.G.t!=0 and menu.G.t.is_alive():
        menu.G.kill=True
        time.sleep(.5)
    if menu.G.t!=0 and menu.G.t.is_alive():
        menu.G.kill=True
        time.sleep(.5)
    if menu.G.t!=0 and menu.G.t.is_alive():
        menu.G.kill=True
        time.sleep(.5)
    menu.G.t = Thread(target=v1.RedGreen, args=(pixels,))
    menu.G.t.start()

def load_preset_Rainbow():
    print("Load Rainbow Rotate")
    if menu.G.t.is_alive():
        menu.G.kill=True
        time.sleep(.5)
    if menu.G.t.is_alive():
        menu.G.kill=True
        time.sleep(.5)
    if menu.G.t.is_alive():
        menu.G.kill=True
        time.sleep(.5)
    if menu.G.t.is_alive():
        menu.G.kill=True
        time.sleep(.5)
    if menu.G.t.is_alive():
        menu.G.kill=True
        time.sleep(.5)
    if menu.G.t.is_alive():
        menu.G.kill=True
        time.sleep(.5)
    menu.G.t = Thread(target=v1.Rainbow, args=(pixels,))
    menu.G.t.start()

def load_preset_WhiteTwinkle():
    print("Load White Twinkle")
    if menu.G.t.is_alive():
        menu.G.kill=True
        time.sleep(.5)
    if menu.G.t.is_alive():
        menu.G.kill=True
        time.sleep(.5)
    if menu.G.t.is_alive():
        menu.G.kill=True
        time.sleep(.5)
    if menu.G.t.is_alive():
        menu.G.kill=True
        time.sleep(.5)
    if menu.G.t.is_alive():
        menu.G.kill=True
        time.sleep(.5)
    if menu.G.t.is_alive():
        menu.G.kill=True
        time.sleep(.5)
    menu.G.t = Thread(target=v1.WhiteFade, args=(pixels,))
    menu.G.t.start()

def load_custom():
    print("Load Custom")
    if menu.G.t.is_alive():
        menu.G.kill=True
        time.sleep(.5)
    menu.G.t = Thread(target=v1.Custom, args=(pixels,pattern_dropdown.get(),menu.G.custom_color1,menu.G.custom_color2,fade_checkbox.get()))
    menu.G.t.start()

def runtime_quit():
    print("I quit!")
    menu.G.bright=0
    if(not(menu.G.t.is_alive())):
        menu.G.kill=True
        time.sleep(.5)
    if(not(menu.G.t.is_alive())):
        menu.G.kill=True
        time.sleep(.5)
    if(not(menu.G.t.is_alive())):
        menu.G.kill=True
        time.sleep(.5)
    if(not(menu.G.t.is_alive())):
        menu.G.kill=True
        time.sleep(.5)
    control_star(board.D24,False)
    window.destroy()
    exit(0)


def choose_color1():
    # variable to store hexadecimal code of color
    color_code1 = tk.colorchooser.askcolor(title ="Choose Primary Color")
    menu.G.custom_color1=tuple(color_code1[0][i] for i in (1,0,2))
    #print(rgb_to_grbhex(color_code1[0]))
    entry_color1.delete(0,tk.END)
    entry_color1.insert(0,rgb_to_hex(color_code1[0]))
    #print('GRB =', tuple(int(rgb_to_hex(color_code1[0])[i:i+2], 16) for i in (3, 1, 5)))
    
def choose_color2():
    # variable to store hexadecimal code of color
    color_code2 = tk.colorchooser.askcolor(title ="Choose Secondary Color")
    menu.G.custom_color2=tuple(color_code2[0][i] for i in (1,0,2))
    #print(color_code2[0])
    #print(rgb_to_grbhex(color_code2[0]))
    entry_color2.delete(0,tk.END)
    entry_color2.insert(0,rgb_to_hex(color_code2[0]))
    #print('GRB =', tuple(int(rgb_to_hex(color_code2[0])[i:i+2], 16) for i in (3, 1, 5)))

def updateOnTime(time):
    print("On at {}:{} {}".format(*time))
    label_start.configure(text="{}:{:02d} {}".format(*time))

def updateOffTime(time):
    print("Off at {}:{} {}".format(*time))
    label_stop.configure(text="{}:{:02d} {}".format(*time))

def get_time_on():
    top = tk.Toplevel(window)
    time_picker = AnalogPicker(top)
    time_picker.pack(expand=True, fill="both")
    theme = AnalogThemes(time_picker)
    theme.setDracula()
    ok_btn = tk.Button(top,text="OK",command=lambda: (updateOnTime(time_picker.time()),top.destroy()))
    ok_btn.pack()

def get_time_off():
    top = tk.Toplevel(window)
    time_picker = AnalogPicker(top)
    time_picker.pack(expand=True, fill="both")
    theme = AnalogThemes(time_picker)
    theme.setDracula()
    ok_btn = tk.Button(top,text="OK",command=lambda: (updateOffTime(time_picker.time()),top.destroy()))
    ok_btn.pack()

window = tk.Tk()
window.title("The Stick")
#greeting = tk.Label(text="Hello, Tkinter",fg="white",bg="#34A2FE",width=20,height=10)
#greeting.pack()

frame_top = tk.Frame(master=window)
frame_top.pack()
frame_bottom = tk.Frame(master=window)
frame_bottom.pack()

#label = tk.Label(master=frame_top, text="Top")
#label.pack(side=tk.LEFT)
frame_left = tk.Frame(master=frame_top,relief=tk.SUNKEN,borderwidth=1)
frame_left.pack(side=tk.LEFT,fill=tk.BOTH)
label_presets = tk.Label(master=frame_left, text="Presets",anchor="w",width=15,font= ('Helvetica 15 underline'))
label_presets.pack()
button_RedGreenFade = tk.Button(master=frame_left, text="Red Green Fade", width=15, height=2, command=load_preset_RedGreenFade)
button_RedGreenFade.pack()
button_RainbowRotate = tk.Button(master=frame_left, text="Rainbow Rotate", width=15, height=2, command=load_preset_Rainbow)
button_RainbowRotate.pack()
button_Twinkle = tk.Button(master=frame_left, text="White Twinkle", width=15, height=2, command=load_preset_WhiteTwinkle)
button_Twinkle.pack()


#label3 = tk.Label(master=frame_top, text="Top2")
#label3.pack(side=tk.LEFT)
frame_right = tk.Frame(master=frame_top,relief=tk.RAISED,borderwidth=1)
frame_right.pack(side=tk.LEFT,fill=tk.BOTH)
label_custom = tk.Label(master=frame_right, text="Custom",anchor="w",width=20,font= ('Helvetica 15 underline'))
label_custom.pack()
OPTIONS = [
"Solid",
"Blink",
"Twinkle"
]

pattern_dropdown = tk.StringVar(window)
pattern_dropdown.set(OPTIONS[0]) # default value

frame_combo = tk.Frame(master=frame_right)
frame_combo.pack(fill=tk.BOTH)
label_pattern = tk.Label(master=frame_combo, text="Pattern:",width=14,anchor="e")
label_pattern.pack(side=tk.LEFT)
w = tk.OptionMenu(frame_combo, pattern_dropdown, *OPTIONS)
w.config(width=8)
w.pack(side=tk.LEFT)



frame_color1 = tk.Frame(master=frame_right)
frame_color1.pack(fill=tk.BOTH)
label_color1 = tk.Label(master=frame_color1, text="Primary Color:", width=14,anchor="e")
label_color1.pack(side=tk.LEFT)
entry_color1 = tk.Entry(master=frame_color1, width=8)
entry_color1.insert(0,"#FF0000")
custom_color1=(0,255,0)
entry_color1.pack(side=tk.LEFT)
button_color1_pick = tk.Button(master=frame_color1, text="Pick", width=3, height=1,command=choose_color1)
button_color1_pick.pack(side=tk.LEFT)

frame_color2 = tk.Frame(master=frame_right)
frame_color2.pack(fill=tk.BOTH)
label_color2 = tk.Label(master=frame_color2, text="Secondary Color:", width=14,anchor="e")
label_color2.pack(side=tk.LEFT)
entry_color2 = tk.Entry(master=frame_color2, width=8)
entry_color2.insert(0,"#00FF00")
custom_color2=(255,0,0)
entry_color2.pack(side=tk.LEFT)
button_color2_pick = tk.Button(master=frame_color2, text="Pick", width=3, height=1,command=choose_color2)
button_color2_pick.pack(side=tk.LEFT)

frame_fade = tk.Frame(master=frame_right)
frame_fade.pack(fill=tk.BOTH)
#label_fade = tk.Label(master=frame_fade,text="Fade?",width=14,anchor="e")
#label_fade.pack(side=tk.LEFT)

fade_checkbox = tk.IntVar()
fade_checkbx = tk.Checkbutton(frame_fade, text="Fade?", variable=fade_checkbox)
fade_checkbx.pack()

button_custom_apply = tk.Button(master=frame_right, text="Apply", width=8, height=1, command=load_custom)
button_custom_apply.pack()

label_runtime = tk.Label(master=frame_bottom, text="Runtime",anchor="w",width=37,font= ('Helvetica 15 underline'))
label_runtime.pack()
frame_runtime = tk.Frame(master=frame_bottom)
frame_runtime.pack(fill=tk.BOTH)
frame_runtime_left = tk.Frame(master=frame_runtime)
frame_runtime_left.pack(side=tk.LEFT,fill=tk.BOTH)
frame_runtime_right = tk.Frame(master=frame_runtime)
frame_runtime_right.pack(side=tk.LEFT,fill=tk.BOTH)

frame_brightness = tk.Frame(master=frame_runtime_left)
frame_brightness.pack(fill=tk.BOTH)
label_brightness = tk.Label(master=frame_brightness,text="Brightness:",width=10,height=2,anchor="se")
label_brightness.pack(side=tk.LEFT)
slider_brightness = tk.Scale(frame_brightness, from_=0, to=10, orient=tk.HORIZONTAL)
slider_brightness.bind("<ButtonRelease-1>", runtime_updateBrightness)
slider_brightness.set(10)
slider_brightness.pack()

frame_speed = tk.Frame(master=frame_runtime_left)
frame_speed.pack(fill=tk.BOTH)
label_speed = tk.Label(master=frame_speed,text="Delay:",width=10,height=2,anchor="se")
label_speed.pack(side=tk.LEFT)
slider_speed = tk.Scale(frame_speed, from_=0, to=50, orient=tk.HORIZONTAL)
slider_speed.bind("<ButtonRelease-1>", runtime_updateSpeed)
slider_speed.set(10)
slider_speed.pack()

frame_start = tk.Frame(master=frame_runtime_right)
frame_start.pack(fill=tk.BOTH)
button_time_on = tk.Button(master=frame_start,text="Set On Time",command=get_time_on)
button_time_on.pack(side=tk.LEFT)
label_start = tk.Label(master=frame_start,text="<none>",width=10,height=2)
label_start.pack(side=tk.LEFT)

frame_stop = tk.Frame(master=frame_runtime_right)
frame_stop.pack(fill=tk.BOTH)
button_time_off = tk.Button(master=frame_stop,text="Set Off Time",command=get_time_off)
button_time_off.pack(side=tk.LEFT)
label_stop = tk.Label(master=frame_stop,text="<none>",width=10,height=2)
label_stop.pack(side=tk.LEFT)

frame_quit = tk.Frame(master=frame_bottom)
frame_quit.pack(fill=tk.BOTH)
button_quit = tk.Button(master=frame_quit, text="Quit", width=8, height=1, command=runtime_quit)
button_quit.pack()

control_star(board.D24,True)
pixels = neopixel.NeoPixel(board.D18,700,auto_write=False)
#pixels = neopixel.NeoPixel(board.D18,850,auto_write=False)
load_preset_RedGreenFade()
window.mainloop()
