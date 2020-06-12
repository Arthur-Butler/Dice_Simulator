#Importing Tkinter GUI
from tkinter import *  
#Importing Number Randomizer 
from random import randint
#Functions 
def Dice_Roll():
       dice1=str(randint(1,6))
       dice2=str(randint(1,6))
       print ("Dice 1: "+dice1+" Dice 2: "+dice2)
       Welcome_lbl = Message(text = " Dice 1: "+dice1+" Dice 2: "+dice2).place(x=30,y=50)
       Roll_btn = Button(text = "Roll Again",activebackground = "black", activeforeground = "blue", command=Dice_Roll).place(x = 30, y = 170)  
Sim_Welcome=Tk()
Sim_Welcome.geometry("300x200")
Welcome_lbl = Label(text = "WELCOME TO DICE SIMULATOR",).place(x=70,y=20)
Roll_btn = Button(text = "Roll Dice",activebackground = "black", activeforeground = "blue", command=Dice_Roll).place(x = 30, y = 170)  
Exit_btn = Button(text = "Exit",activebackground = "black", activeforeground = "blue").place(x = 240, y = 170)  
Sim_Welcome.mainloop()



