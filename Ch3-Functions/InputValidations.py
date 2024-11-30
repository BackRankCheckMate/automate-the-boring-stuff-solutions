def collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

try:
    start = int(input('Enter a number: '))
    print(collatz(start))
except ValueError:
    print("The input must be an integer")
