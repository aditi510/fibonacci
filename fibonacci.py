def fibonacci(n):
    fib_sec = [0, 1]
    for i in range(2, n):
        next_number = fib_sec[i-1]+fib_sec[i-2]
        fib_sec.append(next_number)

        return fib_sec[:n ]
        n = 10
        result = fibonacci(n)
        print(f"The first {n} numbers in the Fibonacci sequence are:", result)
