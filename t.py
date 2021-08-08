# from pyfirmata2 import Arduino, util
# import time
# board = Arduino('COM7')
# for i in range(0,100):
#     board.digital[13].write(1)
#     # time.sleep(1000)
#     board.digital[13].write(0)
#     # time.sleep(1000)
a = [None]
print(a)
a.append(int(3))
print(a)
# test1
guss_me = 7
if guss_me < 7:
    print("too low")
elif guss_me > 7:
    print('too high')
else:
    print('just right')
# test2
guss_me = 7
start = 1
while start < 9:
    if start<guss_me:
        print("too low")
    elif start==guss_me:
        print("found it!")
    else:
        print("oops")
    start += 1
# test3
a = [3,2,1,0]
for b in a:
    print(b)
# test4
double = []
for number in range(0,11,2):
    double.append(number)
print(double)
# test4-1
double=list(range(0,11,2))
print(double)
# test5
def good():
    a=['Harry','Ron',"Hermione"]
    print(a)
good()