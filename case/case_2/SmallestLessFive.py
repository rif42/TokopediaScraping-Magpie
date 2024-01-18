import random

def generate_input():
    return random.randint(-99999999999,99999999999)

def slf(num):
    final=[]
    fiveindexes = []
    numtype=False if num < 0 else True #check if negative/positive
    num = abs(num)
    for index, digits in enumerate(str(num)): #chatgpt to get value and index in one loop
        # get the index of number 5
        if digits == "5":
            fiveindexes.append(index)

    for index in fiveindexes:
        #remove the character at index
        temp = str(num)
        temp = temp[:index] + temp[index+1:]
        
        #append to list
        if numtype == False:
            final.append(int(temp)*-1)
        elif numtype == True:
            final.append(int(temp))

    #sort final list
    final.sort()
    print(final)
    if len(final) == 0:
        return 0
    else:
        return final[0]

randinput = generate_input()
print(randinput)
print(slf(randinput))