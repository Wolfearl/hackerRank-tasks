def caesarCipher(s, k):
    k = k % 26
    result = ""
    for char in s:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + k) % 26 + base)
            result += new_char
        else:
            result += char
    return result


print(caesarCipher("www.abc.xy", 87))