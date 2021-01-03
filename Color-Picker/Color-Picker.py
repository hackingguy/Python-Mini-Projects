import keyboard
from tkinter import *
from pynput import mouse
import win32gui
from win32clipboard import *
import pyautogui

def on_click(x, y, button, pressed):
	root.withdraw()
	root.clipboard_clear()
	root.clipboard_append("#"+hex_result)
	root.update()
	print("Hello")
	root.destroy()
	return False

def motion():
    x,y,r,g,b = getPointerInfo()
    hex_result = "".join([format(val, '02X') for val in [r,g,b]])
    a.configure(text="#{0}\nRGB({1},{2},{3})".format(hex_result,r,g,b))
    colorval = "#%02x%02x%02x" % (r, g, b)
    a.update()
    try:
        canvas.itemconfig(rect, fill=colorval)
        moveWindow(x,y)
    except Exception as e:
        print(e)
	

def make_window():
    global canvas,rect,a
    (x,y) = win32gui.GetCursorPos()
    root.geometry('+%d+%d'%(x+40,y+30))
    root.overrideredirect(1)
    frame = Frame(root,width=220,height=70,borderwidth=0,background='black')
    a = Label(text="Hello World",fg='white',anchor='w',justify=LEFT)
    a.configure(background='black')
    root.call('wm', 'attributes', '.', '-topmost', True)
    root.after_idle(root.call, 'wm', 'attributes', '.', '-topmost', False)
    root.lift()
    root.attributes('-alpha',0.95)
    frame.pack_propagate(False)
    frame.pack()
    canvas = Canvas(frame,width=70,height=70)
    rect = canvas.create_rectangle(0,0,72,68,fill="black",outline="white")
    canvas.place(x=0,y=0)
    a.place(x=78,y=1)

def getPointerInfo():
    (x,y) = pyautogui.position()
    screenshot = pyautogui.screenshot(
        region=(
            x, y, 1, 1
        )
    )
    RGBint = screenshot.getcolors()
    r =  RGBint[0][1][0]
    g =  RGBint[0][1][1]
    b =  RGBint[0][1][2]
    rgb = [r,g,b]
    return [x,y,r,g,b]

def moveWindow(x,y):
    root.geometry('+%d+%d'%(x+40,y+30))
    root.after(1,motion)

root = Tk()
canvas = ''
rect= ''
hex_result = ''
a = ''
keyboard.add_hotkey('esc',lambda: root.destroy())
make_window()

listener = mouse.Listener(
    on_click=on_click)
listener.start()
root.after(1,motion)
root.mainloop()
