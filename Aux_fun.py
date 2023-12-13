u= 0.000001 # micro
m= 0.001# mili

def f_calc_type(numbers):
    if "" in numbers: 
        print(nu) 
    pass
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