if __name__ == '__main__':
    n = int(input())
    marksheets = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        marksheets[name] = scores
    
    query_name = input()
    req_marks = marksheets[query_name]
    print(format(sum(req_marks)/len(req_marks), '.2f'))
