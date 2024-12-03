from threading import Thread,Lock

class globalVars():
    pass

G = globalVars() #empty object to pass around global state
G.lock = Lock() #not really necessary in this case, but useful none the less
G.value = 0
G.kill = False
G.delay = .5
G.bright = 1
G.t = 0
G.custom_color1 = (0,0,0)
G.custom_color2 = (0,0,0)
