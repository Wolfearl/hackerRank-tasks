def highestValuePalindrome(s, n, k):
    first = ''
    second = ''
    rn = n - 1
    count = 0
    for i in range(n // 2):
        if s[i] != s[rn - i]:
            count += 1
    if k < count:
        return '-1'
    else:
        for i in range(n // 2):
            left = s[i]
            right = s[rn - i]
            if left == right:
                if left == '9' or k - 2 < count:
                    first += left
                    second += left
                else:
                    first += '9'
                    second += '9'
                    k -= 2
            else:
                if k - 1 >= count and left != '9' and right != '9':
                    first += '9'
                    second += '9'
                    k -= 2
                else:
                    if left > right:
                        first += left
                        second += left
                    else:
                        first += right
                        second += right
                    k -= 1
                count -= 1
        if n % 2 == 1:
            if k > 0:
               return first + '9' + second[::-1]
            else:
                return first + s[n // 2] + second[::-1]
        else:
            return first + second[::-1]


print(highestValuePalindrome('5', 1, 1))