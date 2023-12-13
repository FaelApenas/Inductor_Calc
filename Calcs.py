import numpy as np
from Aux_fun import * 


def calcs_data(numbers): 
    type_calc= f_calc_type(numbers)
    if type_calc==0xFF: 
        print("Only one variable should be empty") 
        return
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
    


def fourth_var(numbers): 
    print("Numr de voltas")
    pass

def third_var(numbers): 
    print("Indutancia")

    pass 

def first_var(numbers): 
    print("Area das espiras")

    pass

def second_var(numbers): 
    print("Comprimento das espiras ")

    pass