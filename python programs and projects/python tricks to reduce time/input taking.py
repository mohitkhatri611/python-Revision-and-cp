NO_OF_CHARS = 256
def areAnagram(str1, str2):
    # Create two count arrays and initialize all values as 0
    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS
    """observe the initialize of arrays to 0"""
    for i in str1:
        count1[ord(i)] += 1

    for i in str2:
        count2[ord(i)] += 1

    if len(str1) != len(str2):
        return 0
    key="key"; value="value"
    #for representig the format
    print("%s == %s" % (key, value))

    print("HCF of {0} and {1} is {2}", format(key,value,areAnagram(key,value)))


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())


if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())


"""
#for taking input like this
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

"""
if __name__ == '__main__':
    #for taking inp as above ex.
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    """2
       1 2     """