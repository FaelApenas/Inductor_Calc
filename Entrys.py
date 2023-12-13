from tkinter import *
import tkinter as tk
from Calcs import *

b_color = "#aba9a6"  # Background color

root = tk.Tk()
root.geometry("800x600")
root.title("Inductor calculator")
root.configure(background=b_color)
root.resizable(False, False)


lb1 = tk.Label(root, text="Parametros", font=("Arial", 18)).grid(column=1, row=1)
Label(text="coil_Area", background=b_color).place(x=10, y=50)
coil_area = Entry(root)
coil_area.place(x=110, y=50, width=200, height=20)

Label(text="Coil lenght", background=b_color).place(x=10, y=75)
coil_len = Entry(root)
coil_len.place(x=110, y=75, width=200, height=20)


Label(text="Indutance", background=b_color).place(x=10, y=100)
indutance = Entry(root)
indutance.place(x=110, y=100, width=200, height=20)


Label(text="Number of turns", background=b_color).place(x=10, y=125)
N_turns = Entry(root)
N_turns.place(x=110, y=125, width=200, height=20)


def Call_calc():  
    result = ""
    numbers= [ coil_area.get(), coil_len.get(),indutance.get(),N_turns.get()] 
    calcs_data(numbers)
 
    Label(text=result, background=b_color).place(x=400, y=100)


    
    
    

call_app = Button(root, text="Calculate", width=20,command=Call_calc)
call_app.place(x=110, y=200)


root.mainloop()
