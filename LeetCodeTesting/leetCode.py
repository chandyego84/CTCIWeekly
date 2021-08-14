class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''Longest substring without repeeating characters'''
        charDict = {}
        left = 0
        longest = 0
        
        for c in range(len(s)):
            if (s[c] not in charDict):
                # new char encountered 
                longest = max(longest, c - left + 1)
            
            else:
                if (charDict[s[c]] < left):
                     # old char encountered again but prev index is not in current window
                    longest = max(longest, c - left + 1)
                else:
                    # old char encounteed again but prev index is in current window
                    left = charDict[s[c]] + 1
            
            charDict[s[c]] = c  # update index of curr char in dict
        
        return longest

    def reverse(self, x: int) -> int:
        '''Given a signed 32-bit integer x, return x with its digits reversed. 
        If reversing x causes the value to go outside 
        the signed 32-bit integer range [-231, 231 - 1], then return 0.'''
        # assume environment does not allow you to store 64-bit ints
        reversed = 0 
        xLength = len(str(x))

        if (x < 0):
            x += x * -2
            xLength -= 1
            while (xLength != 0):
                reversed += (x % 10) * (10 ** (xLength - 1))
                x //= 10
                xLength -= 1  
            reversed -= reversed * 2
        else:
            while (xLength != 0):
                reversed += (x % 10) * (10 ** (xLength - 1))
                x //= 10
                xLength -= 1    
        
        if (reversed < 2 ** 31 or reversed > -2 ** 31):
            return 0

        return reversed


    def longestPalindrome(self, s: str) -> str:
        '''Given string s, return longest palindromic substring in s'''
        # can be done using Dynamic Programming
        



solt = Solution()
print(solt.lengthOfLongestSubstring(("tmmxyzta")))
