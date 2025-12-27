class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_r = reversed(' ' + s)
        i = 0
        flag = False
        n = next(s_r)
        # consume whitespace
        j = 0
        while n == ' ':
            i += 1
            j += 1
            n = next(s_r)
        # consume the first word
        print(f"Skipped {j} spaces")
        while n != ' ':
            i += 1
            n = next(s_r)
        return i - j
    
sol = Solution()
test_string = "a"
result = sol.lengthOfLastWord(test_string)
print(f"The length of the last word in '{test_string}' is: {result}")