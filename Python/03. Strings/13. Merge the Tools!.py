from collections import OrderedDict
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        sub_string = (string[i:i+k])
        print(''.join(OrderedDict.fromkeys(sub_string).keys()))
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
