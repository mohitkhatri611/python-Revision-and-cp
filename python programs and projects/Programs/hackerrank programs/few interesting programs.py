
#https://www.hackerrank.com/challenges/python-mutations/problem
#as we know string are immutable so using this prog we change the character in sting.
def immutable_sting():
    s = input()
    i, c = input().split()
    i = int(i)
    print(s[:i] + c + s[(i+1):])

#other but not better way
def split_and_join(line):
    # write your code here
    line=line.split()
    line='-'.join(line)
    return line


