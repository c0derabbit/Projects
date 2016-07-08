# generate the fibonacci sequence to the n-th number (limited to 10000, reasonably fast)
def fib(n):
    if n <= 1:
        return n
    else:
        if n > 10000:
            n = 10000
        arr = [0, 1]
        for i in range(2,n):
            arr.append(arr[i-1]+arr[i-2])
        return arr
