def matchingStrings(strings, queries):
    result = []
    for query in queries:
        result.append(strings.count(query))
    return result


print(matchingStrings(['ab', 'ab', 'abc'], ['ab', 'abc', 'bc']))