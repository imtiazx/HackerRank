def swap_case(s):
    output = ''
    for char in s:
        if char.isupper():
            output += char.lower()
        elif char.islower():
            output += char.upper()
        else:
            output += char
    return output

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
