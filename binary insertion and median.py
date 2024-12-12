def insort(a, x, lo=0, hi=None):

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    a.insert(lo, x)

def process_queries(queries):
    f_x = 0
    n = 0
    median = 0
    my_list = []
    absum = 0
    results = []
    if queries:
        first_query = queries[0] 
        a, b = first_query[1], first_query[2]
        f_x += b
        my_list.append(a)
        n += 1
        median = a
        queries = queries[1:] 
        
    for query in queries:
        if query[0] == 1:
            a, b = query[1], query[2]
            f_x += b
            insort(my_list, a)
            n += 1
            if n % 2 == 0:
                absum += abs(median - my_list[(n//2 - 1 + n % 2)])
                median = my_list[(n//2 - 1 + n % 2)]
                absum += abs(a - median)
            if n % 2 != 0:
                if a < median:
                    absum += 2 * abs(median - my_list[(n//2 - 1 + n % 2)])
                median = my_list[(n//2 - 1 + n % 2)]
                absum += abs(a - median)
        elif query[0] == 2:
            results.append((median, absum + f_x))
    
    return results

q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]
results = process_queries(queries)

for res in results:
    print(res[0], res[1])

