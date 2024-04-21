#User function template for Python
"""
Given an array of size n and a range [a, b]. The task is to partition the array around the range such that the array is divided into three parts.
1) All elements smaller than a come first.
2) All elements in range a to b come next.
3) All elements greater than b appear in the end.
The individual elements of three sets can appear in any order. You are required to return the modified array.

Note: The generated output is 1 if you modify the given array successfully.

Geeky Challenge: Solve this problem in O(n) time complexity.

Example 1:

Input: 
n = 5
array[] = {1, 2, 3, 3, 4}
[a, b] = [1, 2]
Output: 
1
Explanation: 
One possible arrangement is: {1, 2, 3, 3, 4}. If you return a valid arrangement, output will be 1.

Example 2:

Input: 
n = 6 
array[] = {1, 4, 3, 6, 2, 1}
[a, b] = [1, 3]
Output: 
1
Explanation: 
One possible arrangement is: {1, 3, 2, 1, 4, 6}. If you return a valid arrangement, output will be 1.
Your Task:
You don't need to read input or print anything. The task is to complete the function threeWayPartition() which takes the array array, a, and b as input parameters and modifies the array in place according to the given conditions.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= n <= 106
1 <= array[i], a, b <= 109


"""
class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
	def threeWayPartition(self, arr, a, b):
	    # code here 
	    n=len(arr)
	    start = 0
	    end = n-1
	    i = 0
	    
	    while i<=end:
	        if arr[i]<a:
	            arr[start], arr[i] = arr[i], arr[start]
	            start +=1
	            i += 1
	        elif arr[i] > b:
	            arr[i], arr[end] = arr[end], arr[i]
	            end -= 1
	        else:
	            i += 1
	    return 1


#{ 
 # Driver Code Starts
#Initial template for Python

from collections import Counter

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        array = list(map(int, input().strip().split()))
        original = Counter(array)
        a,b = list(map(int, input().strip().split()))
        ob = Solution()
        ob.threeWayPartition(array, a, b)

        k1 = k2 = k3 = 0
        for e in array:
            if e > a:
                k3+=1
            elif e<=a and e>=b:
                k2+=1
            elif e<a:
                k1+=1

        m1 = m2 = m3 = 0
        for e in range(k1):
            if array[e]<a:
                m1+=1
        for e in range(k1, k1+k2):
            if array[e]<=a and array[e]>=b:
                m2+=1
        for e in range(k1+k2, k1+k2+k3):
            if array[e]>=a:
                m3+=1

        flag = False
        if k1==m1 and k2==m2 and k3==m3:
            flag = True
        for e in range(len(array)):
            original[array[e]]-=1
        for e in range(len(array)):
            if original[array[e]]!=0:
                flag = False
        if flag:
            print(1)
        else:
            print(0)

# } Driver Code Ends
