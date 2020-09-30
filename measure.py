def measure_go_nogo_calculate(upper, lower, value):
    gonogo = bool
    if value <= upper and lower<=value:
        gonogo = True
    else:
        gonogo = False
    return gonogo
def measure_Yield(upper, lower, values):
    excellent = []
    inferior = []
    all = []
    for value in values:
        value = float(value)
        if value <= upper and lower <= value:
            excellent.append(value)
        else:
            inferior.append(value)
        all.append(value)
    return (len(excellent), len(inferior), len(all))