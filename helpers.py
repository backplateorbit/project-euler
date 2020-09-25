def fibo_sequence(count=None, stop=None):
    def next_fibo(l, m):
        return l + m

    fibos = [1,2]

    if stop:
        while fibos[-1] < stop:
            fibos.append(next_fibo(fibos[-1], fibos[-2]))
    elif count:
        while len(fibos) < count:
            fibos.append(next_fibo(fibos[-1], fibos[-2]))

    return fibos

    