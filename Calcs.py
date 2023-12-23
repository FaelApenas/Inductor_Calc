import numpy as np
from Aux_fun import * 

# Constants 
Mag_field = 0.35 
#----------


def calcs_data(numbers): 
    type_calc= f_calc_type(numbers)
    if type_calc==0xFF: 
        print("Only one variable should be empty") 
        return "Only one variable should be empty"
    else: 
        match type_calc: 
            case 1: 
                result= first_var(numbers) 
                return result
            case 2: 
                result= second_var(numbers)
                return result
            case 3: 
                result= third_var(numbers)
                return result
            case 4: 
                result= fourth_var(numbers)
                return result 
    
def first_var(numbers):  # 
    print("first var")
    coil_len= handle_data(numbers[1])
    indutance= handle_data(numbers[2])
    N_turns= handle_data(numbers[3])
    result = coil_len*indutance*N_turns
    return result

def second_var(numbers): 
    print("Comprimento das espiras ")


def third_var(numbers): 
    print("Indutancia")

    pass 

    pass
def fourth_var(numbers): 
    print("Numr de voltas")
    pass





