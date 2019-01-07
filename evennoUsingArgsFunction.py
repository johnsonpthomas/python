b = []
def evenno(*args):
    for i in args:
        if i%2 ==0:
            b.append(i)
    print(b)

evenno(5,6,7,8)
