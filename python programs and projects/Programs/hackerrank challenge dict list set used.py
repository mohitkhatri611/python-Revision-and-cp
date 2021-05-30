#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    myDict = {}
    myset = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())

        if score in myDict:
            li = myDict[score]
            li.append(name)
            myDict[score] = li
        else:
            li = [name]
            myDict[score] = li
            myset.add(score)

    # print(sorted(myset)[0])
    lst = sorted(myDict[sorted(myset)[1]])

    for i in lst:
        print(i)

