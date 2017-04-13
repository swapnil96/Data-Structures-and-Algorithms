
length = 60
done = [False]*length;
smallest_prime = [0]*length

def Sieve():

    smallest_prime[0] = 0
    smallest_prime[1] = 1
    for i in xrange(2, length, 2):
        smallest_prime[i] = 2

    for i in xrange(3, length, 2):

        if done[i] == False:
            smallest_prime[i] = i
            for j in xrange(i, length/i, 2):
                if done[j*i] == False:
                    done[j*i] = True
                    smallest_prime[j*i] = i

if __name__ == "__main__" :
    Sieve()
    for i in xrange(30):
        print smallest_prime[i]
