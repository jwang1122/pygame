def f(*args, **kwargs):
    print(args)
    print(kwargs)

if __name__ == '__main__':
    f(1,2,3, k1=1,k2=2,k3=3)