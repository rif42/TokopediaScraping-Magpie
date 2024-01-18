import random
import time

def generate_input():
    start = time.time()

    inputs = []
    for i in range(0, 10):
        inputs.append(str(random.randint(0, 100)))

    result_input = ' '.join(inputs)
    
    end = time.time()
    print(f"generate_input() ran for: {(end-start)*10**3:.03f}ms")
    return result_input


def check(string):
    start = time.time()

    string = [int(x) for x in string.split()] #chatgpt to make one line code
    smallest = string[0]

    for i in range(0, len(string)):
        if i != len(string)-1:
            if string[i] < string[i+1]:
                smallest = string[i]
            if string[i] > string[i+1] and string[i+1] < smallest:
                return i+1
            
    end = time.time()
    print(f"check() ran for: {(end-start)*10**3:.03f}ms")

    return 0

testinput = generate_input()
print(testinput)
customtest = "3 4 1"
print(check(testinput))