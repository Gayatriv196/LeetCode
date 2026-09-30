class Solution:
    def runningSum(self, a):
        for i in range(1, len(a)):
            a[i] = a[i] + a[i - 1]
        
        return a