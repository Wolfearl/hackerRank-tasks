def superDigit(n, k):
    initial_sum = sum(int(digit) for digit in n) * k

    def recursive_super_digit(x):
        if x < 10:
            return x
        else:
            return recursive_super_digit(sum(int(digit) for digit in str(x)))

    return recursive_super_digit(initial_sum)


print(superDigit('123', 3))