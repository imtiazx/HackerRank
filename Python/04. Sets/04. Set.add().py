def num_unique_countries():
    n = int(input())
    set_countries = set()
    for i in range(n):
        set_countries.add(input())
    return len(set_countries)

print(num_unique_countries())
