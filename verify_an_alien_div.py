class Solution:
    def isOrdered(self,order, a,b):
        min_val = min(len(a),len(b))
        for j in range(min_val):
            if order.index(a[j]) == order.index(b[j]):
                continue
            elif order.index(a[j]) < order.index(b[j]):
                return True
            else:
                return False
        if len(a) <= len(b):
            return True
        else:
            return False
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):
            if self.isOrdered(order, words[i], words[i+1]) == True:
                continue
            else:
                return False
        return True
