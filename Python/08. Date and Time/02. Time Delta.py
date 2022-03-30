import math
import os
import random
import re
import sys
from datetime import datetime

def time_delta(t1, t2):
    format_string = "%a %d %b %Y %H:%M:%S %z"
    
    parsed_t1 = datetime.strptime(t1, format_string)
    parsed_t2 = datetime.strptime(t2, format_string)
    
    diff = int(abs((parsed_t2 - parsed_t1).total_seconds()))
 
    return(str(diff))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
