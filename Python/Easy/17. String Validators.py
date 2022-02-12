def check_alnum(s):
    for c in range(len(s)):
        if s[c].isalnum():
            return True
            break
    return False

def check_alpha(s):
    for c in range(len(s)):
        if s[c].isalpha():
            return True
            break
    return False

def check_digit(s):
    for c in range(len(s)):
        if s[c].isdigit():
            return True
            break
    return False

def check_lower(s):
    for c in range(len(s)):
        if s[c].islower():
            return True
            break
    return False

def check_upper(s):
    for c in range(len(s)):
        if s[c].isupper():
            return True
            break
    return False


if __name__ == '__main__':
    s = input()
    print(check_alnum(s))
    print(check_alpha(s))
    print(check_digit(s))
    print(check_lower(s))
    print(check_upper(s))
    