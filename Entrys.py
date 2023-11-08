from tkinter import * 
import tkinter as tk 

b_color= "#aba9a6"
root = tk.Tk()
class Application(): 
    def __init__(self)->None: 
        self.root= root 
        self.window()
        root.mainloop()
        pass

    def window(self): 
        root.geometry("800x600")
        root.title("Inductor calculator") 
        root.configure(background=b_color)
        root.resizable(False,False)
        





lb1=tk.Label(root,text="Parametros",font=("Arial",18)).grid(column=1,row=1)

area_text=Label(text="coil_Area",background=b_color).grid(column=1,row=2)
coil_area_e= Entry(lb1,width=20).grid(column=2,row=2)

indutance_text=Label(text="indutance",background=b_color).grid(column=1,row=3)
indutance_e= Entry(lb1,width=20).grid(column=2,row=3)

turns_text =Label(text="number of turns",background=b_color).grid(column=1,row=4)
number_turns_e= Entry(lb1,width=20).grid(column=2,row=4)

lenght_text=Label(text="Coil_Lenght",background=b_color).grid(column=1,row=5)
lenght_coil_e= Entry(lb1,width=20).grid(column=2,row=5) 

call_app= Button(root,text="Calculate",width=20).grid(column=2,row=7)


Application()