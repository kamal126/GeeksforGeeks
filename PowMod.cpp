/**
									20 MAY 2024

Modular Exponentiation for large numbers

hashtag#POTD hashtag#GFG hashtag#100DayProblemChallange
Implement pow(x, n) % M.
In other words, for a given value of x, n, and M, find (x^n) % M.
 
Example 1:
Input: x = 3, n = 2, m = 4 
Output: 1 
Explanation: 32 = 9. 9 % 4 = 1.
Example 2:
Input: x = 2, n = 6, m = 10 
Output: 4 
Explanation: 26 = 64. 64 % 10 = 4.

Your Task:
You don't need to read or print anything. Your task is to complete the function PowMod() which takes integers x, n, and M as input parameters and returns x^n % M.
 
Expected Time Complexity: O(log(n))
Expected Space Complexity: O(1)
 
Constraints:
1 ≤ x, n, M ≤ 10^9
  */

class Solution
{
	public:
		long long int PowMod(long long int x,long long int n,long long int M)
		{
		    // Code here
		    if(n==0) return 1;
		    if(n==1) return x;
		    
		    long long val = PowMod(x,n/2, M);
		    val = (val*val)%M;
		    
		    if(n%2==1) return (val*x)%M;
		    
		    return val;
		}
};
