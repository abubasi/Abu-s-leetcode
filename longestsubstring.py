class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}
        max_length = 0
        start = 0

        for end, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = end 
            max_length = max(max_length,end - start +1)
        return max_length
if __name__ == "__main__":
    lls = Solution()
    result = lls.lengthOfLongestSubstring(s="abuabu")
    
    print(result)
