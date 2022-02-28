if __name__ == '__main__':
    n = int(input())
    score = list(map(int, input().split()))
    print(sorted(set(score))[-2])
