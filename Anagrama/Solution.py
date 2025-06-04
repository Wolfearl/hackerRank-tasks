from collections import Counter

def anagram(s):
    n = len(s)//2
    s1 = s[:n]
    s2 = s[n:]
    if len(s1) != len(s2):
        return -1
    counter1 = Counter(s1)
    counter2 = Counter(s2)
    all_chars = set(s)
    r = 0
    for char in all_chars:
        r += abs(counter1[char] - counter2[char])
    return r // 2

print(anagram("xaxbbbxx"))