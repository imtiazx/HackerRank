if __name__ == '__main__':
    N = int(input())
    records = []
    scores = set()
    for i in range(N):
        name = input()
        score = float(input())
        records.append([score, name])
        scores.add(score)
    
    second_lowest_score = sorted(scores)[1]
    second_lowest_names = []
    for score, name in records:
        if score == second_lowest_score:
            second_lowest_names.append(name)  

    for name in sorted(second_lowest_names):
        print(name, end = '\n')
