def print_numbers(current, n):
    if current > n:
        return
    print(current)
    print_numbers(current + 1, n)   # Tail recursive call

n = 5
print_numbers(1, n)