from tkinter import *
import time
root=Tk()
root.title("Timers_and_Clocks")
root.geometry('600x400')
def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    my_label.config(text= f"{hour} : {minute} : {second}")
    my_label.after(1000, clock)

def  update():
    my_label.config(text="New Text")
    
my_label = Label(root, text="", font= ('Helvetica', 48), fg='green', bg="black")
my_label.pack(pady=20)
my_label.after(5000, update)

clock()
root.mainloop()