from multiprocessing import Pool, Queue, Array

def f(x, y):
    print x, y
    return x*x + y*y

if __name__ == '__main__':
    pool = Pool(processes=4)              # start 4 worker processes
    result = pool.apply_async(f, [10,2])    # evaluate "f(10)" asynchronously
    print result.get(timeout=1)           # prints "100" unless your computer is *very* slow
    m = Array('i', [1,2,2,3])
    n = Array('i', [1,2,2,3,4])
    print help(pool.map)
    print pool.map(f, m, n)          # prints "[0, 1, 4,..., 81]"
