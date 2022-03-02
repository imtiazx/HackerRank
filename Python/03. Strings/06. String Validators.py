def check_alnum(string):
    for s in string:
        if s.isalnum():
            return True
            break        
    return False

def check_alpha(string):
    for s in string:
        if s.isalpha():
            return True
    return False

def check_digit(string):
    for s in string:
        if s.isdigit():
            return True
            break
    return False

def check_lower(string):
    for s in string:
        if s.islower():
            return True
            break
    return False

def check_upper(string):
    for s in string:
        if s.isupper():
            return True
            break
    return False

if __name__ == '__main__':
    string = input()
    print(check_alnum(string))
    print(check_alpha(string))
    print(check_digit(string))
    print(check_lower(string))
    print(check_upper(string))
