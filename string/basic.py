

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



"""
sliding window application

s = "aabaabaa"
pattern = "aaba"
anagram -> must have 3 a's, 1 b(same characters, irrespective of position)
number of anagrams -> 4[(0,3),(1,4),(3,6),(4,7)]
s="nayan"
pattern="ay"
"""

#TODO: find when character frequency becomes negative
def getFrequencyMap(s,n):
	res = {}
	for character in s:
		if character in res:
			res[character] += 1
		else:
			res[character] = 1
	return res

def count_anagrams(s,n, pattern, k):

	i = 0
	j = 0
	patternFreqMap = getFrequencyMap(pattern,k)
	count = len(patternFreqMap)  #number of unique elements
	res = 0
	demoPatternFreqMap = patternFreqMap
	for j in range(n):
		character = s[j]
		#1. calculate
		if character in patternFreqMap:
			patternFreqMap[character] -= 1
			if patternFreqMap[character] == 0:
				count -= 1
		else:
			patternFreqMap = demoPatternFreqMap #if element mismatch, reset the patternFreqMap
			count = len(patternFreqMap)
		if count == 0:
			res += 1
		# print(i,j,character, count,patternFreqMap,res)
		if j-i+1<k:
			j += 1
		else:
			#2. discard prior calculation
			leftCharacter = s[i]
			if leftCharacter in patternFreqMap:
				patternFreqMap[leftCharacter] += 1
				if patternFreqMap[leftCharacter] == 1:
					count += 1
			#3. slide window
			i +=1 
			j += 1
		# print(i,j,character, count,patternFreqMap,res)

		
	return res
s = "aabaabaa"
pattern = "aaba"
# s="nayan"
# pattern="ay"
s="mississippi"
pattern="is"
# print(count_anagrams(s,len(s), pattern, len(pattern)))




"""
"""

def longest_substring_with_k_unique_characters(s,n,k):
	i = 0
	j = 0

	maxSubstringLength = 0

	uniqueCharsCount = 0
	foundCharFreq = {}

	while j < n:
		character = s[j]
		# print(i, j, character, uniqueCharsCount, maxSubstringLength, foundCharFreq)
		if character in foundCharFreq: 	
			foundCharFreq[character] += 1
		else:
			foundCharFreq[character] = 1
			uniqueCharsCount += 1
		if uniqueCharsCount == k:
			maxSubstringLength = max(maxSubstringLength, j-i+1)
			j += 1
		elif uniqueCharsCount < k:
			j += 1
		else:

			foundCharFreq[s[i]] -= 1
			if foundCharFreq[s[i]] == 0:
				uniqueCharsCount -= 1
			i += 1
	return maxSubstringLength

s="aaa"
s="aabacbebebe"
# print(longest_substring_with_k_unique_characters(s,len(s),3))


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

def longest_substring_without_repeating_characters_1(s, n):
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
# print(longest_substring_without_repeating_characters_1(s, len(s)))

"""
we store index instead of frequency because we never would store repititive chars anyway
"""

def longest_substring_without_repeating_characters_2(s,n):
	i = 0
	j = 0
	maxSubstringLength = 0
	foundCharIndex = {}
	while j < n:
		character = s[j]
		index = foundCharIndex.get(character, -1)
		# print(i,j,character, index,foundCharIndex, maxSubstringLength)
		foundCharIndex[character] = j
		if index > -1:
			i = index + 1  #directlty bring the i'th index to next of already found character(duplicate)
		else:
			maxSubstringLength = max(maxSubstringLength, j-i+1)
		j += 1

	return maxSubstringLength

s="abbc" #Use this to trace
# s="abcabcbb"
# s="pwwkew"
# s="bbbbb"
# print(longest_substring_without_repeating_characters_2(s,len(s)))



"""
given string, in which each character indicates a toy,
aim is to find max. number of toys can one get, given
1. continous chars/toys(substring)
2. not exceeds number of unique chars/toys(k) 
example -s="abaccab", k = 2
max here would be 2,5->acca
as one would get 4 chars(max) with 2 unique (given k) 

This will not work with longest_substring_with_k_unique_characters because of -
s = "aaaaa"
k = 2
answer is len(s)

"""

def longest_substring_with_atmost_k_unique_characters(s,n,k):
	# i  = 0
	# j = 0
	# uniqueCharsCount = 0
	# maxSubstringLength = 0
	# foundCharIndex = {}
	# while j < n:
	# 	character = s[j]
	# 	index = foundCharIndex.get(character, -1)
	# 	foundCharIndex[character] = j

	# 	print(i,j,character,index,uniqueCharsCount,foundCharIndex,maxSubstringLength)
	# 	if index == -1: 	#if element is already considered
	# 		uniqueCharsCount += 1

	# 		#check if we've already hit the limit, if so then decrease window(by removing the i'th element completely, refer a)
	# 		if uniqueCharsCount > k:
	# 			iCharacter = s[i]
	# 			i = foundCharIndex[iCharacter] + 1
	# 			del foundCharIndex[iCharacter]
	# 			uniqueCharsCount -= 1

	# 	maxSubstringLength = max(maxSubstringLength,j-i+1)
	# 	j += 1



	return maxSubstringLength

s="abaccab"
# s="aaaaa"
# s = "sasss"
print(longest_substring_with_atmost_k_unique_characters(s,len(s),2))