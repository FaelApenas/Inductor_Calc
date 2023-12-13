def f_calc_type(numbers):
    verify_lock=True
    Calc_type= 0   #The type of the calc will be defined by this number 
    for number in numbers: 
        if number =="":
            if verify_lock==False: 
                print("Only one variable should be empty")
                return  0xFF
            Calc_type= Calc_type + numbers.index(number)+1
            verify_lock=False 


    return Calc_type  

        



teste_n=["","","2","4"]
f_calc_type(teste_n)