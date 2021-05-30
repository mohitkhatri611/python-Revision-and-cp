
def replaceChars(intput,c1,c2):
    newChars = map(lambda x: x if (x!=c1 and x!=c2) else \
                   c1 if (x==c2) else c2, input)

    print(''.join(newChars))


if __name__=="__main__":
    input='grrksfoegrrks'
    c1='e'
    c2='r'
    replaceChars(input,c1,c2)
