"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                total = digits[i] + 1
            else:
                total = digits[i] + carry
            
            if total >= 10:
                digits[i] = total % 10
                carry = total // 10
            else:
                digits[i] = total
                carry = 0
                break
        if carry > 0:
            digits.insert(0, carry) 
        return digits
    

sol = Solution()
print(sol.plusOne([1,2,3]))  # Output: [1,2,4]
print(sol.plusOne([4,3,2,1]))  # Output: [4,3,2,2]