#coding:utf-8

'''
For LeetCode
'''
#Exe1
# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         newtar = target // 2
#         newnums = []
#         for i in range(len(nums)):
#             newnums.append(nums[i])
#         print(newnums)
#         print(id(newnums))
#         print(id(nums))
#         print(newtar)
#
#         for i in range(newtar+1):
#             num1 = i
#             num2 = target - i
#             print(num1,num2)
#
#             if num1 in nums :
#                 #nums1 = copy.copy(nums)
#                 if num1 == num2:
#                     newnums.remove(num1)
#                     print(newnums)
#                 print(nums)
#                 print("nums.index(num1)",nums.index(num1))
#
#                 if num2 in newnums:
#                     if num1 == num2:
#                         print("nums.index(num1)", nums.index(num1))
#                         print("nums1.index(num2)", newnums.index(num2))
#                         return [nums.index(num1), newnums.index(num2)+1]
#                     else:
#                         print("nums.index(num1)", nums.index(num1))
#                         print("nums1.index(num2)", newnums.index(num2))
#                         return [nums.index(num1), newnums.index(num2)]

#Exe2
# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         newnums = []
#         result = []
#
#         for i in range(len(nums)):
#             newnums.append(target-nums[i])
#         print(newnums)
#         a = list(set(nums).intersection(newnums))
#
#         if len(a)>2:
#             [a.remove(i) for i in a if i == target or i == target/2]
#
#         if len(a)==1:
#             result.append(nums.index(a[0]))
#             nums.remove(a[0])
#             result.append(1+nums.index(a[0]))
#         elif len(a) == 2:
#             result.append(nums.index(a[0]))
#             result.append(nums.index(a[1]))
#         else:
#             print("error",a)
#
#         print(result)
#         return result

#Exe3
# 给定一个字符串，找出不含有重复字符的最长子串的长度。
#
# 示例：
#
# 给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。
#
# 给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。
#
# 给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。
# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         # i = 0
#         # j = 0
#         # key = range(len(s))
#         # val = list(s)
#         # newdic = dict(zip(key,val))
#         # Lvalue = []
#         # Lvaluevv = []
#         # news = []
#         # while j < len(s):
#         #     news = val[i:j]
#         #     print("first news ",news)
#         #
#         #     if val[j] in news:
#         #         Lvalue.append(len(news))
#         #         Lvaluevv.append(news)
#         #         print("first j is ",j)
#         #         for k in range(j):
#         #             if newdic[k]==val[j]:
#         #                 Lindex = k
#         #         i = Lindex + 1
#         #
#         #
#         #         # print('current i is',i)
#         #         # print('current j is', j)
#         #
#         #
#         #     j += 1
#         #     if j == len(s) :
#         #         news = val[i:j]
#         #         Lvaluevv.append(news)
#         #         Lvalue.append(len(news))
#         #
#         # print("The max number is ",max(Lvalue))
#         # print(Lvaluevv)
#
#         indexDict = {}
#         i = 0
#         j = 0
#
#         Lvalue = []
#         Lvaluevv = []
#         news = []
#         if len(s) == 0:
#             val = 0
#         else:
#
#             while j < len(s):
#                 if s[j] in news:
#                     Lvalue.append(len(news))
#                     Lvaluevv.append(news)
#                     i = indexDict[s[j]] + 1
#
#                 indexDict[s[j]] = j
#                 j += 1
#                 news = s[i:j]
#                 if j == len(s):
#                     Lvalue.append(len(news))
#                     Lvaluevv.append(news)
#             val = max(Lvalue)
#
#         print("The max number is ",val)
#         print(Lvaluevv)
#         print(indexDict)

#Exe4
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
#
# 请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 中位数是 2.0

# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         nums = nums1 + nums2
#         nums.sort()
#
#         if len(nums) == 0:
#             val = 0
#         else:
#
#             i = len(nums) % 2
#             key = int(len(nums) / 2)
#             if i == 0:
#                 val = (nums[key - 1] + nums[key]) / 2
#             else:
#                 val = nums[key]
#         print(val)
#         return val

#Exe5
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba"也是一个有效答案。
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

if __name__ == '__main__':
    newSolution = Solution()
    # res = newSolution.twoSum([-3,0,8,2,3,9],0)
    # print(res)
    # res = newSolution.twoSum([2, 7, 11, 15],9)
    # newSolution.lengthOfLongestSubstring('qwnfenpglqdq')
    # newSolution.lengthOfLongestSubstring('qwnfenpglqdq')

    #Exe4
    # nums1 = [1, 2,5,6]
    # nums2 = [3, 4]
    # newSolution.findMedianSortedArrays(nums1,nums2)

