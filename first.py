def caching_fibonacci(n):
    cache = {}

    def fibonacci(n):
        if n in cache <= 0:
            return 0
        elif n in cache == 1:
            return 1
        elif n in cache:
            return cache[n]

        result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        return result
    

    return fibonacci
    
n= 5
print(caching_fibonacci)

#caching_fibonacci()



fib = caching_fibonacci
cache = {},
