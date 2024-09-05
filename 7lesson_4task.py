import time

def decorator(in_func):
    def out_func(*args, **kwargs):
        start = time.time()
        res = in_func(*args, **kwargs)
        print(time.time() - start)
        return res
    return  out_func

@decorator
def in_func(first, second):
    return (int(first) ** int(second))

print(in_func("8", "5"))



