import time  # This is required to include time module.
import pyautogui # PyAutoGUI lets Python control the mouse and keyboard, and other GUI automation tasks.
import tkinter as tk  #for developing graphical user interfaces (GUIs)

def screenshot():
    #time.sleep(5) Python time method sleep() suspends execution for the given number of seconds.
    image= pyautogui.screenshot('image.png')
    image.show()


root = tk.Tk() #The root window is created. The root window is a main application window in our programs. It has a title bar and borders.
frame = tk.Frame(root)  #A frame in Tk lets you organize and group widgets. It works like a container. Its a rectangular area in which widges can be placed
frame.pack()

btl = tk.Button()
    frame,
    text ="Take Screenshot",
    command=screenshot)

btl.pack(side = tk.LEFT)

close = tk.Button(
    frame,
    text = "QUIT",
    command=quit)
close.pack(side = tk.RIGHT)   

root.mainloop()  #This method will loop forever, waiting for events from the user, until the user exits the program – either by closing the window, or by terminating the program with a keyboard interrupt in the console.

