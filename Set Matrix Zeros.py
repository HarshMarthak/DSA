class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r=len(matrix)
        c=len(matrix[0])
        column=True

        for i in range(r):

        	if matrix[i][0]==0:
        		column=False

        	for j in range(1,c):

        		if matrix[i][j]==0:

        			matrix[i][0]=0
        			matrix[0][j]=0

        for i in reversed(range(r)):
        	for j in range(c-1,0,-1):
        		if matrix[i][0]==0 or matrix[0][j]==0:
        			matrix[i][j]=0

        	if column==False:
        		matrix[i][0]=0