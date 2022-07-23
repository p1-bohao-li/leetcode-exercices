# 3. Longest Substring Without Repeating Characters

from collections import deque 


class Solution:

    def removeUntil(self, dq, set_, c):
        while True:
            removed_character = dq.popleft()
            set_.remove(removed_character)
            if removed_character == c:
                break

    def lengthOfLongestSubstring(self, s: str) -> int:
        record = 0
        characters_set = set()
        characters_dq = deque()
        for c in s:
            if c in characters_set:
                self.removeUntil(characters_dq, characters_set, c)
            characters_set.add(c)
            characters_dq.append(c)

            if len(characters_set) > record:
                record = len(characters_set)

        return record


s = Solution()

# Special case 1
# Input string length is 1
# result = s.lengthOfLongestSubstring(" ") 

# Special case 2
# Input string length is 0
# result = s.lengthOfLongestSubstring("")

# Special case 3
# The result string is the input string itself
# result = s.lengthOfLongestSubstring("au")

# result = s.lengthOfLongestSubstring("dvdf")
result = s.lengthOfLongestSubstring("abcabcbb")
print(result)
