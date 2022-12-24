class Solution(object):
    def lengthOfLongestSubstring(self, s):
        output = 0
        count = {}
        pos = -1
        for index, letter in enumerate(s):
            if letter in count and count[letter] > pos:
                pos = count[letter]
            count[letter] = index
            output = max(output,index-pos)
        return output


# class Solution(object):
#
#     def lengthOfLongestSubstring(self, s):
#         def myFunc(e):
#             return len(e)
#
#         """
#         :type s: str
#         :rtype: int
#         """
#         substring = ""
#         sub_list = []
#         max_len = -1
#         res = ''
#         for i in s:
#             # if i == ' ' or i == " ":
#             #     return 1
#
#             if i not in substring:
#                 substring += i
#                 sub_list.append(substring)
#
#             else:
#                 sub_list.append(substring)
#                 substring = ''
#                 substring += i
#                 sub_list.append(substring)
#             sub_list.append(substring)
#         for ele in sub_list:
#             if len(ele) > max_len:
#                 max_len = len(ele)
#                 res = ele
#
#         return len(res)


result = Solution()

x = result.lengthOfLongestSubstring("dvdf")
print(x)
