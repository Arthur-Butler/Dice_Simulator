#Importing Tkinter GUI
from tkinter import *  
#Importing Number Randomizer 
from random import randint
import sys
#Function that simultes dice roll
def Dice_Roll():
       #Assigning random value to two dice variables 
       dice1=str(randint(1,6))
       dice2=str(randint(1,6))
       print ("Dice 1: "+dice1+" Dice 2: "+dice2)
       #Showing results on GUI and changing the Roll dice button to a roll again button
       Welcome_lbl = Message(text = " Dice 1: "+dice1+" Dice 2: "+dice2).place(x=130,y=60)
       Roll_btn = Button(text = "Roll Again",activebackground = "black", activeforeground = "blue", command=Dice_Roll).place(x = 30, y = 170)  
# Function Closing Tkinter 
def close_window (): 
       Sim_Welcome.destroy()
#Creating a GUI to interact with the user
Sim_Welcome=Tk()
Sim_Welcome.geometry("300x200")
Welcome_lbl = Label(text = "WELCOME TO DICE SIMULATOR", font='times', bg='black', fg='yellow').place(x=30,y=20)
Roll_btn = Button(text = "Roll Dice",activebackground = "black", activeforeground = "blue", command=Dice_Roll).place(x = 30, y = 170)  
Exit_btn = Button(text = "Exit",activebackground = "black", activeforeground = "blue", command=close_window).place(x = 240, y = 170)  
Sim_Welcome.mainloop()





