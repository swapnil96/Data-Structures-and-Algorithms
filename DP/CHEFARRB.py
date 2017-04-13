'''Link - https://www.codechef.com/COOK77/problems/CHEFARRB'''

def check(num, string1):

    string = [0]*32
    for i in xrange(32):
        if string1[i] > 0:
            string[i] = 1

    to = int(''.join(map(str, string)), 2)
    return to >= num

def solve(n, got, num):

    till = [0]*32
    end = 0
    count = 0
    for i in xrange(n):
        if check(got, till) == 1:
            count += n - end + 1
            a = bin(num[i])[2:]
            length = len(a)
            for j in xrange(length):
                if a[j] == '1':
                    till[32 - length + j] -= 1

        else:
            for k in xrange(end, n):
                a = bin(num[k])[2:]
                length = len(a)
                for j in xrange(length):
                    if a[j] == '1':
                        till[32 - length + j] += 1

                if check(got, till) == 1:
                    end = k + 1
                    count += n - k
                    a = bin(num[i])[2:]
                    length = len(a)
                    for j in xrange(length):
                        if a[j] == '1':
                            till[32 - length + j] -= 1

                    break

    return count

tt = int(raw_input())
for i in xrange(tt):
    n, k = map(int, raw_input().split())
    a = map(int, raw_input().split())
    print solve(n, k, a)
