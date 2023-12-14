class notation(object): 
    def __init__(self,letter,value): 
        self.letter = letter
        self.value= value

notation_table= {'m': notation("m",10**(-3)),
                 'u': notation("u",10**(-6)), 
                 'n': notation("n",10**(-9)),
                 'k': notation("k",10**3), 
                 'M': notation("M",10**6),
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
    if data[-1:] in notation_table:
        notes= notation_table[data[-1:]].value
        data =data.rstrip(data[-1:])
        data =float(data)
        data = data *  notes
    return float(data)