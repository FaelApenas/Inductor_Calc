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
    
def first_var(numbers):  
    print("first var")
    peak_c= handle_data(numbers[1])
    indutance= handle_data(numbers[2])
    N_turns= handle_data(numbers[3])
    air_gap= (indutance* peak_c*100000)/(Mag_field*N_turns)
    return air_gap

def second_var(numbers): 
    print("Comprimento das espiras ")
    air_gap= handle_data(numbers[0])
    indutance= handle_data(numbers[2])
    N_turns= handle_data(numbers[3])
    peak_c= (Mag_field*N_turns*air_gap)/(indutance*100000)
    return peak_c

def third_var(numbers): 
    print("Indutancia")
    air_gap= handle_data(numbers[0])
    peak_c= handle_data(numbers[1])
    N_turns= handle_data(numbers[3])
    indutance= (Mag_field*N_turns*air_gap)/(peak_c*100000)
    return indutance


     

    
def fourth_var(numbers):
    air_gap= handle_data(numbers[0])
    peak_c= handle_data(numbers[1])
    indutance= handle_data(numbers[2])

    N_turns= (indutance* peak_c*100000)/(Mag_field*air_gap)
    return N_turns





