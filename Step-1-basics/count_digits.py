def count_digits(value):
    n = abs(value)
    count = 1 if n == 0 else 0
    while n:
        count += 1
        n //= 10
    return count


print(count_digits(12124))
