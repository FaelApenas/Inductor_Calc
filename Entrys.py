from tkinter import *
import tkinter as tk
from Calcs import *
 
##000000, #151515, #f8a145, #f07900 and #d35100
b_color = "#B7B7A4"  # Background color
font_v  = "Times" 


root = tk.Tk()
root.geometry("800x600")
root.title("Inductor calculator")
root.configure(background=b_color)
root.resizable(False, False)



#Frame "Inductor calculator"--------------------------------------------
Frame_p= Frame(root,borderwidth=1,relief="sunken",background="#595f39")
Frame_p.place(x=0,y=0,width=800,height=40)
lb1 = Label(root, text="Inductor Calculator", font=(font_v, 20,"bold italic"),background="#595f39",fg="white").place(x=300,y=0)


#--------------------------------------------------------------------- 

#Frame Parameters -------------------------------------------------------

framec_back= "#C4C5BA"
Frame_c= Frame(root,borderwidth=1,relief="sunken",background=framec_back)
Frame_c.place(x=5,y=45,width=700,height=200)

Label(Frame_c,text="Coil área",font=(font_v, 12),background=framec_back).place(x=0,y=0)
coil_area = Entry(Frame_c)
coil_area.place(x=100, y=5, width=40, height=20)
Label(Frame_c,text="Metros Quadrados",font=(font_v, 8),background=framec_back).place(x=150,y=5)



Label(Frame_c,text="Coil Lenght",font=(font_v, 12),background=framec_back).place(x=0,y=30)
coil_len = Entry(Frame_c)
coil_len.place(x=100, y=30, width=40, height=20)
Label(Frame_c,text="Metros",font=(font_v, 8),background=framec_back).place(x=150,y=30)


Label(Frame_c,text="Indutance",font=(font_v, 12),background=framec_back).place(x=0,y=60)
indutance = Entry(Frame_c)
indutance.place(x=100, y=60, width=40, height=20)
Label(Frame_c,text="Henrys",font=(font_v, 8),background=framec_back).place(x=150,y=60)


Label(Frame_c,text="Coil área",font=(font_v, 12),background=framec_back).place(x=0,y=90)
N_turns = Entry(Frame_c)
N_turns.place(x=100, y=90, width=40, height=20)
Label(Frame_c,text="Metros Quadrados",font=(font_v, 8),background=framec_back).place(x=150,y=90)
#----------------------------------------------------------------------------------------------------

def Call_calc():  
    Label(text="                                       ", background="Black",bg='#fff').place(x=400, y=100)
    numbers= [coil_area.get(), coil_len.get(),indutance.get(),N_turns.get()] 
    result = "Result : "+ str(calcs_data(numbers))
    
    Label(text=result, background="#1B1B1B", fg='white' ).place(x=400, y=100)


    
    
    

call_app = Button(root, text="Calculate", width=20,command=Call_calc)
call_app.place(x=10, y=200)

#Notes Frame ---------------------------------------------------------------------------------
notes_frame= Frame(root,borderwidth=1,background=b_color)
notes_frame.place(x=5,y=300,width=700,height=200)
Label(notes_frame, text= "How to use: Complete the variables you have and let the one you want to calculate empty",background=b_color).pack()


root.mainloop()
