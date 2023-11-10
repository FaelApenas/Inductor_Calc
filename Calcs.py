import numpy as np
u= 0.000001 # micro
m= 0.001# mili



def calcs_data(numbers): 
    counter= 0
    for item in numbers: 
       if item == "" : 
        counter= counter +(numbers.index(item)+5)
        print(counter)
        
    if counter>8: 
        print("Only one variable should be empty") 
        return
    else: 
        match counter: 
            case 5: 
                result= Calc_coilA(numbers) 
                return result

            case 6: 
                result= Calc_coil_len(numbers)
                return
            case 7: 
                result= Calc_ind(numbers)
                return
            case 8: 
                result= Calc_NTurns(numbers)
                return
    


def Calc_NTurns(numbers): 
    print("Numr de voltas")
    pass

def Calc_ind(numbers): 
    print("Indutancia")

    pass 

def Calc_coilA(numbers): 
    print("Area das espiras")

    pass

def Calc_coil_len(numbers): 
    print("Comprimento das espiras ")

    pass