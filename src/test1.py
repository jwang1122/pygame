class A:
    def __init__(self):
        self.a = 5
        self.c = 20

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 10
    
if __name__ == '__main__':
    b = B()
    print(b.a)
    print(b.c)