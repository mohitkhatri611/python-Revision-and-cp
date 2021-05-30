if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print("{:.6f}".format(sum(student_marks.get(query_name))/len(scores))) # this will print upto 6 digit after decimal.
    #output: 56.000000

    #other way:
    #print("%.2f" % (sum(marks) / len(marks)))
    Numbers = [1, 2, 3, 4, 6, 4, 3, 6, 8, 5, 8]
    for i in enumerate(Numbers):
        print("Index of {} is {}".format(i[1],i[0]))

    pm = ['modi', 'biden', 'jacinda', 'scott', 'boris']
    country = ['india', 'us', 'nz', 'aus', 'uk']

    for pm ,country in zip(pm,country):
        print("Prime Minister: %s Country is: %s" %(pm,country))