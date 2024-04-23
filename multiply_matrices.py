"""
Rohan's Love for Matrix
=========================
Rohan has a special love for the matrices especially for the first element of the matrix. Being good at Mathematics, he also loves to solve the different problem on the matrices. So one day he started to multiply the matrix with the original matrix.  The elements of the original matrix a are given by [a00=1 , a01=1, a10=1, a11=0].
Given the power of the matrix, n calculate the an and return the a10 element mod 1000000007.

Example 1:

Input: 
n = 3
Output: 
2 
Explanation: Take the cube of the original matrix 
i.e a3 and the (a10)th element is 2.
Example 2:

Input: 
n = 4
Output: 
3
Explanation: Take the cube of the original matrix 
i.e a4 and the (a10)th element is 3.
Your Task:  
You dont need to read input or print anything. Complete the function firstElement() which takes n as input parameter and returns the a10 element mod 1000000007 of an.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1<= n <=106
"""
class Solution:
    def multiply_matrices(self, a, b):
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += a[i][k] * b[k][j]
                    result[i][j] %= 1000000007
        return result

    def matrix_power(self, a, n):
        result = [[1, 0], [0, 1]]
        while n:
            if n % 2:
                result = self.multiply_matrices(result, a)
            a = self.multiply_matrices(a, a)
            n //= 2
        return result

    def firstElement(self, n):
        a = [[1, 1], [1, 0]]
        result = self.matrix_power(a, n)
        return result[1][0]

        
#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.firstElement(n))
# } Driver Code Ends
