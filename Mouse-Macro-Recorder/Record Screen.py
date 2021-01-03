#! /usr/bin/env python3


from pynput.mouse import Listener
import pyautogui
import tkinter


def Play():
	i=0
	n = int(input("No. Of Loops:"))
	time = int(input("Enter The Duration To Play:"))
	for n in range(n,0,-1):
		with open('Akash.txt') as f:
			for line in f:
				if(i%2==0):
					x, y = line.split(",")
					try:
						pyautogui.moveTo(int(x), int(y), duration=time)
						pyautogui.click()
					except KeyboardInterrupt:
						print("Interrupted Session")
				i=i+1
			f.close()
	print('\033c')
	print('Recording Played Successfully')

def Record():
	def on_click(x, y, button, pressed):
		if(x==0 and y==0):
			#record_button.config(text="Recording Done")
			return False
		f.write(str(x)+""+","+str(y)+"\n")
		print ("Mouse clicked")
		pass

	def on_scroll(x, y, dx, dy):
    		print ("Mouse scrolled")


	f= open("Akash.txt","w")
	try:
		with Listener(on_click=on_click, on_scroll=on_scroll) as listener:
			#record_button.config(text="Recording Done")
			listener.join()
	except:
		print("Done")
	f.close()
	print('\033c')
	print("Recording Done")

def close_window():
	print('\033c')
	print("Thanks For Using Our App")
	window.destroy()

try:
	top = tkinter.Tk()
	top.title("Macro Recorder")
	top.resizable()
	record_button = tkinter.Button(top, text ="Record",width=25, command = Record)
	play_button = tkinter.Button(top, text ="Play",width=25, command = Play)
	exit_button = tkinter.Button(top, text ="Quit",width=25, command = quit)
	record_button.pack()
	play_button.pack()
	exit_button.pack()
	top.mainloop()

except KeyboardInterrupt:
	print("Thanks For Using Our App")
