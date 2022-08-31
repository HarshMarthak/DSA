class Solution:
    def findDuplicate(self, A):
        tort,hare = A[0],A[A[0]]
        while hare!=tort:
            tort,hare = A[tort],A[A[hare]]
        tort = 0
        while hare!=tort:
            tort,hare = A[tort],A[hare]
        return tort
