import re


tt = ['i pad', 'mousePad()', 'CodeSwarm', 'orange highlighter']
i = 0
while True:
    try:
        start_string = input().rstrip()
        if start_string == "":
            break
    except EOFError:
        break
    rules = start_string.split(';')
    match rules[0]:
        case 'S':
            match rules[1]:
                case 'M':
                    rules[2] = re.sub(r'([A-Z][a-z]+)\(\)', lambda m: ' ' + m.group(1).lower(), rules[2])
                case 'C':
                    rules[2] = re.sub(r'(?<=[a-z])([A-Z])', lambda m:  ' '+ m.group(1), rules[2]).lower()
                case 'V':
                    rules[2] = re.sub(r'([A-Z])', lambda m: ' ' + m.group(1).lower(), rules[2])
        case 'C':
            match rules[1]:
                case 'M':
                    rules[2] = re.sub(r' ([a-z])', lambda m: m.group(1).upper(), rules[2]) + '()'
                case 'C':
                    rules[2] = re.sub(r'(^|\s)([a-z])', lambda m: m.group(2).upper(), rules[2])
                case 'V':
                    rules[2] = re.sub(r' ([a-z])', lambda m: m.group(1).upper(), rules[2])
    print(rules[2], rules[2] == tt[i])
    i += 1
#
# S;V;iPad
# C;M;mouse pad
# C;C;code swarm
# S;C;OrangeHighlighter