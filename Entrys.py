from tkinter import *
import tkinter as tk
from Calcs import *
 
##000000, #151515, #f8a145, #f07900 and #d35100
b_color = "#D4D4D4"  # Background color
font_v  = "Times" 


root = tk.Tk()
root.geometry("800x600")
root.title("Inductor calculator")
root.configure(background=b_color)
root.resizable(False, False)



#Frame "Inductor calculator"--------------------------------------------
frame_p_back= "#283618"
Frame_p= Frame(root,borderwidth=1,relief="sunken",background=frame_p_back)
Frame_p.place(x=0,y=0,width=800,height=40)
lb1 = Label(root, text="Inductor Calculator", font=(font_v, 20),background=frame_p_back,fg="white").place(x=300,y=0)


#--------------------------------------------------------------------- 

#Frame Parameters -------------------------------------------------------

framec_back= "#F0EFEB"
Frame_c= Frame(root,borderwidth=2,relief="sunken",background=framec_back)
Frame_c.place(x=5,y=45,width=700,height=200)

Label(Frame_c,text="Air Gap Área",font=(font_v, 12),background=framec_back).place(x=0,y=0)
air_gap = Entry(Frame_c)
air_gap.place(x=120, y=5, width=40, height=20)
Label(Frame_c,text="Square meters",font=(font_v, 8,"bold italic"),background=framec_back).place(x=150,y=5)


Label(Frame_c,text="Peak current ",font=(font_v, 12),background=framec_back).place(x=0,y=30)
peak_c = Entry(Frame_c)
peak_c.place(x=120, y=30, width=40, height=20)
Label(Frame_c,text="Amperes",font=(font_v, 8,"bold italic"),background=framec_back).place(x=150,y=30)


Label(Frame_c,text="Indutance",font=(font_v, 12),background=framec_back).place(x=0,y=60)
indutance = Entry(Frame_c)
indutance.place(x=120, y=60, width=40, height=20)
Label(Frame_c,text="Henrys",font=(font_v, 8,"bold italic"),background=framec_back).place(x=150,y=60)


Label(Frame_c,text="Number of turns",font=(font_v, 12),background=framec_back).place(x=0,y=90)
N_turns = Entry(Frame_c)
N_turns.place(x=120, y=90, width=40, height=20)
Label(Frame_c,text="undimensional",font=(font_v, 8,"bold italic"),background=framec_back).place(x=150,y=90)
#----------------------------------------------------------------------------------------------------

def Call_calc():  
    Label(text="                                       ", background="Black",bg='#fff').place(x=400, y=100)
    numbers= [air_gap.get(), peak_c.get(),indutance.get(),N_turns.get()] 
    result = "Result : "+ str(calcs_data(numbers))
    
    Label(text=result, background="#1B1B1B", fg='white' ).place(x=400, y=100)


    
    
call_app = Button(root, text="Calculate", width=20,command=Call_calc)
call_app.place(x=10, y=200)

#Result Frame-------------------------------------------------------------------------------


#Notes Frame ---------------------------------------------------------------------------------
notes_frame= Frame(root,borderwidth=1,background=b_color)
notes_frame.place(x=5,y=300,width=700,height=200)
Label(notes_frame, text= "How to use: Complete the variables you have and let the one you want to calculate empty",background=b_color).pack()


root.mainloop()
