class notation(object): 
    def __init__(self,letter,value): 
        self.letter = letter
        self.value= value

notation_table= {0: notation("m",10**(-3)),
                 1: notation("u",10**(-6)), 
                 2: notation("n",10**(-9)),
                 3: notation("k",10**3), 
                 4: notation("M",10**6),
                 }
u= 0.000001 # micro
m= 0.001# mili

def f_calc_type(numbers):
    verify_lock=True
    Calc_type= 0   #The type of the calc will be defined by this number 
    for number in numbers: 
        if number =="":
            if verify_lock==False: 
                return  0xFF
            Calc_type= Calc_type + numbers.index(number)+1
            verify_lock=False 
    return Calc_type 
 
def handle_data(data): 
    if(data[-1:]=='u'): 
        data = data.rstrip(data[-1])
        data = float(data)
        data = data * u
        return data 
    if (data[-1:]=='m'): 
        data = data.rstrip(data[-1])
        data = float(data)
        data = data * m
        return data 

    return float(data)