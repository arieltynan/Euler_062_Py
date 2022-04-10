#Ariel Tynan
#Euler Problem 062, Cubic permutations, solved in Python
#Started 10 April 2022, completed 10 April 2022

from collections import Counter

#Function splits num into digits and then computes how many of each digit in number
def split_nums(num): 
    d_arr = [0,0,0,0,0,0,0,0,0,0] #array of number of digits in each number
    digits = [int(a) for a in str(num)]
    for dig in digits:
        d_arr[dig] = d_arr[dig] + 1 
    return d_arr

comp_arr = [] #array of d_arr for all cubes
for i in range(0,10000):
    comp_arr.append(split_nums(i*i*i))

str_comp_arr = [] #array of strings converted from comp_arr
for i in comp_arr: #convert list of lists into list of strings
    str_list = [str(int) for int in i]
    str_comp_arr.append(int("".join(str_list)))

#print(Counter(str_comp_arr).most_common(1)) #Find mode and number of occurences (5)
mode = Counter(str_comp_arr).most_common(1)[0][0] #Isolates mode value
index = str_comp_arr.index(mode) #Takes index of lowest cube
print(index*index*index) #Answer, lowest cube

#for index, elem in enumerate(str_comp_arr): #Lists all 5 cubes
#    if elem == mode:
#        print(elem,index)