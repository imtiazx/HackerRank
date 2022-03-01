if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        input_list = input().split()
        if input_list[0] == 'print':
            print(arr)
        elif input_list[0] == 'insert':
            arr.insert(int(input_list[1]), int(input_list[2]))
        elif input_list[0] == 'remove':
            arr.remove(int(input_list[1]))
        elif input_list[0] == 'pop':
            arr.pop()
        elif input_list[0] == 'append':
            arr.append(int(input_list[1]))
        elif input_list[0] == 'sort':
            arr.sort()
        else:
            arr.reverse()
