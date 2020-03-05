
def fibonacci(n):
    fibs = [0, 1]
    for i in range(n):
        fibs.append(fibs[-2] + fibs[-1])
        print("fibonacci[%d]=%d"%(i+1, fibs[i]))
    # print(fibs)
fibonacci(200)


