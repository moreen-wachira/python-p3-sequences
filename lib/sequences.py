# In lib/sequences.py

def print_fibonacci(length):
    fib_sequence = []

    while len(fib_sequence) < length:
        if len(fib_sequence) == 0:
            fib_sequence.append(0)
        elif len(fib_sequence) == 1:
            fib_sequence.append(1)
        else:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    print(fib_sequence)
