import textwrap

def wrap(string, max_width):
    # num_of_groups = (len(string))//(max_width)
    # for iter in range(num_of_groups+1):
    #     text_snip = string[(iter*max_width):(iter*max_width)+max_width]
    #     print(text_snip)
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
