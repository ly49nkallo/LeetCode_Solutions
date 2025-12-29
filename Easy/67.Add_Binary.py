from typing import List

"""
Given two binary strings a and b, return their sum as a binary string.
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            sum = carry
            if i >= 0:
                sum += int(a[i])
                i -= 1
            if j >= 0:
                sum += int(b[j])
                j -= 1
            
            result.append(str(sum % 2))
            carry = sum // 2
        
        return ''.join(reversed(result))
    
sol = Solution()
print(sol.addBinary("11", "1"))  # Output: "100"
print(sol.addBinary("1010", "1011"))  # Output: "10101"