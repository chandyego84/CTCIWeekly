'''
Longest substring without repeeating characters
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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

longSubStr = Solution()
print(longSubStr.lengthOfLongestSubstring(("tmmxyzta")))