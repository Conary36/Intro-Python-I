"""
algorithm Sieve of Eratosthenes is
    input: an integer n > 1.
    output: all prime numbers from 2 through n.

    let A be an array of Boolean values, indexed by integers 2 to n,
    initially all set to true.

    for i = 2, 3, 4, ..., not exceeding √n do
        if A[i] is true
            for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n do
                A[j] := false

    return all i such that A[i] is true.


"""

def SieveOfEratosthenes(n):

    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        
        if (prime[p] == True):
            
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    
    for p in range(n +1):
        if prime[p]:
            print(p),
    if __name__ == '__main__':
        n = 100
        print("Following are the prime numbers smaller than or equal to", n)
SieveOfEratosthenes(99)