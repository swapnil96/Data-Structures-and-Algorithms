
import math



def func(num):

    max_a = int(math.sqrt(num))
    min_a = int(math.sqrt(num/4))
    got = 0
    for a in xrange(min_a, max_a+1):

        temp = num - a**2
        max_b = int(math.sqrt(temp))
        min_b = int(math.sqrt(temp/3))

        for b in xrange(min_b, max_b+1):

            temp1 = temp - b**2
            max_c = int(math.sqrt(temp1))
            min_c = int(math.sqrt(temp1/2))

            for c in xrange(min_c, max_c + 1):

                temp2 = temp1 - c**2
                root = int(math.sqrt(temp2))
                if root**2 == temp2:
                    got = 1
                    d = root
                    break

            if got == 1:
                break

        if got == 1:
            break

    print a, b, c, d

func(int(raw_input()))
