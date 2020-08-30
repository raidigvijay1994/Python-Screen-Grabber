import time  # This is required to include time module.
import pyautogui # PyAutoGUI lets Python control the mouse and keyboard, and other GUI automation tasks.
import tkinter as tk  #for developing graphical user interfaces (GUIs).

def screenshot():
    #time.sleep(5)
    image= pyautogui.screenshot('image.png')
    image.show()


root = tk.Tk()
frame = tk.Frame(root)
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

root.mainloop()  #This method will loop forever, waiting for events from the user, until the user exits the program – either by closing the window, or by terminating the program with a keyboard interrupt in the console

