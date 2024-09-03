import re
import math


with open('input.txt', 'r') as f:
  data = f.read().split("\n")

def equationroots( a, b, c): 
 
    # calculating discriminant using formula
    dis = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis)) 
     
    # checking condition for discriminant
    if dis > 0: 
        print("real and different roots") 
        answera = ((-b + sqrt_val)/(2 * a)) 
        answerb = ((-b - sqrt_val)/(2 * a)) 
        print(int(math.floor(answerb) - math.floor(answera)))
     
    elif dis == 0: 
        print("real and same roots") 
        print(-b / (2 * a)) 
     
    # when discriminant is less than 0
    else:
        print("Complex Roots") 
        print(- b / (2 * a), + i, sqrt_val) 
        print(- b / (2 * a), - i, sqrt_val) 


durations = re.findall(r'\d+', data[0])
records = re.findall(r'\d+', data[1])

duration = int(''.join(durations))
record = int(''.join(records))


print(duration,records)
equationroots(-1,duration, -1 * record)
