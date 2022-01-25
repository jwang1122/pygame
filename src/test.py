a, b = 5, 6
flag = True

def add(x):
    global flag
    while flag:
        answer = input("yes or no? ")
        if(answer=='n'):
            flag = False
    return x + a

if __name__ == '__main__':
    print(add(6))
    a = 12
    print(add(4))