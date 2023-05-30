class Solution:
    count = 0
    def isPrime(self, num):
        mid = num // 2
        for i in range(2,mid+1):
            if num % i == 0:
                return False
            else:
                continue
        return True
    def countPrimes(self, n: int) -> int:
        for j in range(2, n):
            if self.isPrime(j) == True:
                self.count += 1
            else:
                continue
        return self.count
