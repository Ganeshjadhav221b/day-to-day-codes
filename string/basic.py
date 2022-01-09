"""
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.
 
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:
Input: s = ""
Output: 0

"""

def longest_substring_without_repeating_characters(s, n):
	mp = {}
	res = 0
	i = 0
	for j in range(n):
		if s[j] in mp:
			i = max(mp[s[j]],i)
		res = max(res, j-i+1)
		mp[s[j]] = j +1
	return res	

s = "pwwkew"
print(longest_substring_without_repeating_characters(s, len(s)))

"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
 
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""
def longest_common_prefix(s,n):
	pass
