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
Frame_c.place(x=5,y=45,width=700,height=300)

Label(Frame_c,text="Air Gap Área",font=(font_v, 16),background=framec_back).place(x=0,y=0)
air_gap = Entry(Frame_c)
air_gap.place(x=160, y=5, width=50, height=20)
Label(Frame_c,text="m",font=(font_v, 12),background=framec_back).place(x=220,y=5)
Label(Frame_c,text="2",font=(font_v, 7),background=framec_back).place(x=234,y=2)


Label(Frame_c,text="Peak current ",font=(font_v, 16),background=framec_back).place(x=0,y=30)
peak_c = Entry(Frame_c)
peak_c.place(x=160, y=30, width=50, height=20)
Label(Frame_c,text="A",font=(font_v, 12),background=framec_back).place(x=220,y=30)


Label(Frame_c,text="Indutance",font=(font_v, 16),background=framec_back).place(x=0,y=60)
indutance = Entry(Frame_c)
indutance.place(x=160, y=60, width=50, height=20)
Label(Frame_c,text="H",font=(font_v, 12),background=framec_back).place(x=220,y=60)


Label(Frame_c,text="Number of turns",font=(font_v, 16),background=framec_back).place(x=0,y=90)
N_turns = Entry(Frame_c)
N_turns.place(x=160, y=90, width=50, height=20)
Label(Frame_c,text="u",font=(font_v, 12),background=framec_back).place(x=220,y=90)


#----------------------------------------------------------------------------------------------------

def Call_calc():  
    result_frame_b= "#F0EFEB"
    result_frame =Frame(root,borderwidth=1,background=result_frame_b) 
    result_frame.place(x=400,y=100,width=300, height=50)
    
    Label(result_frame,text="Result : ",background= result_frame_b,font=(font_v,12)).place(x=0,y=0)

    numbers= [air_gap.get(), peak_c.get(),indutance.get(),N_turns.get()] 
    result =  str(calcs_data(numbers))

    result_label=Label(result_frame,text=result, background=result_frame_b,font=(font_v,12)).place(x=50,y=0)
    
call_app = Button(root, text="Calculate", width=20,command=Call_calc)
call_app.place(x=10, y=200)


#Notes Frame ---------------------------------------------------------------------------------
notes_frame= Frame(root,borderwidth=1,background=b_color)
notes_frame.place(x=5,y=300,width=700,height=200)
Label(notes_frame, text= "How to use: Complete the variables you have and let the one you want to calculate empty",background=b_color).pack()


root.mainloop()
