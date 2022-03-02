def print_full_name(first, last):
    print("Hello {f1} {f2}! You just delved into python.".format(f1 = first_name, f2 = last_name))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
