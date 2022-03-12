def minion_game(s):
    stuart = 0
    kevin = 0
    vow = 'AEIOU'
    for i in range(len(s)):
        if s[i] not in vow:
            stuart = stuart + (len(s)-i)  
        else:
            kevin = kevin + (len(s)-i)  
    if stuart > kevin:
        print('Stuart', stuart)
    elif stuart < kevin:
        print('Kevin', kevin)
    else:
        print('Draw')
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
