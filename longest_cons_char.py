#!/usr/bin/python3

'''
Source: CS Dojo https://www.youtube.com/watch?v=qRNB8CV3_LU
Objective: Given a string, find the longest subsequence consisting 
of a single character.  Example: longest("ABAACDDDBBA") should return {'D': 3}.

'''

import sys

def main(args):
    

    string = args[1]

    longest, current = {},{}

    for char in string:
        # First character. Use 'continue' to prevent rest of
        # logic form being tied to first char
        if not bool(longest):
            longest,current = {char:1},{char:1}
            continue
        # Set current
        if list(current.keys())[0]==char:
            current[char]+=1
        else:
            current = {char:1}
        if list(current.values())[0]>list(longest.values())[0]:
            longest = current.copy()

    print(list(longest.keys())[0],str(list(longest.values())[0]))

if __name__ == '__main__':
    sys.exit(main(sys.argv))
