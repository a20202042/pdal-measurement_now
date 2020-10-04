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

def draw_measure(data):
    measure_data = []
    upper_data = []
    lower_data = []
    for item in data:
        measure_data.append(float(item[0]))
        upper_data.append(float(item[3]))
        lower_data.append(float(item[4]))
    print(measure_data, upper_data, lower_data)
    return (measure_data, upper_data, lower_data)

# draw_measure([['10', 'mm', '2020-10-05  01:12:59', '10.0', '5.0', '3', '長度', '1 - 1'], ['20', 'mm', '2020-10-05  01:13:01', '10.0', '5.0', '3', '長度', '1 - 2'], ['10', 'mm', '2020-10-05  01:13:13', '10.0', '5.0', '3', '長度', '1 - 3']])
# draw_measure([['10', 'mm', '2020-10-05  01:12:59', '10.0', '5.0', '3', '長度', '1 - 1'], ['20', 'mm', '2020-10-05  01:13:01', '10.0', '5.0', '3', '長度', '1 - 2'], ['10', 'mm', '2020-10-05  01:13:13', '10.0', '5.0', '3', '長度', '1 - 3']])