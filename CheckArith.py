class Solution:
    
    def checkIsAP(self, arr, n):
        arr.sort()
        for i in range(1,n-1):
            if arr[i]-arr[i-1]!=arr[i+1]-arr[i]:
                return False
        return True
