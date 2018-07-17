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
# class Solution:
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         L = len(s)
#         Val = ''
#         flg1 = False
#
#         if Solution.iszichuan(s):
#             Val = s
#         else:
#             for k in range(1,L):
#                 for i in range(k+1):
#                     aa = s[i:i+L-k]
#                     if Solution.iszichuan(aa):
#                         Val = aa
#                         flg1 = True
#                         break
#                 if flg1:
#                     break
#
#         print(Val)
#         return Val
#
#     def iszichuan(a):
#         flg = True
#         num = len(a)
#         i = len(a) % 2
#         j = int(len(a)/2)
#
#         # flg = [False for v in range(j) if a[v] != a[num - 1 - v]]
#         for v in range(j):
#             if a[v] != a[num-1-v]:
#                 flg = False
#
#         # print(flg)
#         return flg

#Exe6
# 将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"
#
# 实现一个将字符串进行指定行数变换的函数:
#
# string convert(string s, int numRows);
# 示例 1:
#
# 输入: s = "PAYPALISHIRING", numRows = 3
# 输出: "PAHNAPLSIIGYIR"
# class Solution:
#     def convert(self, s, numRows):
#         """
#         :type s: str
#         :type numRows: int
#         :rtype: str
#         """
#         Line = 0
#         New = {}
#         Plus_flg = 1
#         rs = []
#
#         if len(s) == 0:
#             return ''
#
#         if numRows == 1:
#             return s
#
#         New[0]=[s[0]]
#
#         for i in range(1,len(s)):
#
#             if Plus_flg == 1:
#                 Line += 1
#                 if Line not in New:
#                     New[Line] = [s[i]]
#                 else:
#                     New[Line].append(s[i])
#
#                 if Line == numRows-1:
#                     Plus_flg = 0
#             else:
#                 Line -= 1
#                 New[Line].append(s[i])
#
#                 if Line == 0:
#                     Plus_flg = 1
#
#         print(New)
#         for k,v in New.items():
#             rs += v
#
#         newrs = ''.join(rs)
#         print(newrs)


#Exe7
# 给定一个 32 位有符号整数，将整数中的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#  示例 2:
#
# 输入: -123
# 输出: -321
# 示例 3:
#
# 输入: 120
# 输出: 21
# 注意:
#
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
#
# class Solution:
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#
#         if x>2**31-1 or x <-2**31:
#             return 0
#
#         if x < 0:
#             Val = -__class__.cal(self, -x)
#         else:
#             Val = __class__.cal(self, x)
#         return Val
#
#     def cal(self,x):
#         # Val = 0
#         # L = len(str(x))
#         # if L == 1:
#         #     Val = x
#         # else:
#         #     for i in range(1,L):
#         #         y = int(x % 10)
#         #         x = int(x / 10)
#         #
#         #         Val += y*(10**(L-i))
#         #         if i == L-1:
#         #             Val += x
#         #
#         # if Val > 2 ** 31 - 1 or Val < -2 ** 31:
#         #     Val =  0
#         # print(Val)
#         s = str(x)
#         s = s[::-1]
#
#         Val = int(s)
#
#         if Val > 2 ** 31 - 1 or Val < -2 ** 31:
#             Val =  0
#         print(Val)
#
#         return Val

# Exe8
# 实现 atoi，将字符串转为整数。
# 示例 1:
#
# 输入: "42"
# 输出: 42
# 示例 2:
#
# 输入: "   -42"
# 输出: -42
# 解释: 第一个非空白字符为 '-', 它是一个负号。
#      我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
# 示例 3:
#
# 输入: "4193 with words"
# 输出: 4193
# 解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
# 示例 4:
#
# 输入: "words and 987"
# 输出: 0
# 解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
#      因此无法执行有效的转换。
# 示例 5:
#
# 输入: "-91283472332"
# 输出: -2147483648
# 解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
#      因此返回 INT_MIN (−231) 。


# class Solution:
#     def myAtoi(self, str):
#         """
#         :type str: str
#         :rtype: int
#         """
#         if len(str) == 0:
#             return 0
#
#         li = list(str)
#         while(len(li) and li[0]==' '):
#             del li[0]
#         str = "".join(li)
#
#         if len(str) == 0:
#             return 0
#         print("current str = ",str)
#
#         if str[0].isdigit():
#             Val = __class__.ReNum(self, str)
#         elif str[0] == '-':
#             if len(str)>1 and str[1].isdigit():
#                 Val = -__class__.ReNum(self,str[1:])
#             else:
#                 Val = 0
#         elif str[0] == '+':
#             if len(str)>1 and str[1].isdigit():
#                 Val = __class__.ReNum(self, str[1:])
#             else:
#                 Val = 0
#         else:
#             Val = 0
#
#         if Val >= 2 ** 31 - 1:
#             Val =  2 ** 31 - 1
#         elif Val <= -2 ** 31:
#             Val =  -2 ** 31
#         print(Val)
#
#
#     def ReNum(self,str):
#         Val = 0
#         if len(str):
#             for i in range(len(str)):
#                 if str[i].isdigit() == False:
#                     Val = str[:i]
#                     break
#                 else:
#                     if i == len(str)-1:
#                         Val = str
#         Val = int(Val)
#         print("cueent Val is ",Val)
#         return Val

# Exe9
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 示例 1:
#
# 输入: 121
# 输出: true
# 示例 2:
#
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3:
#
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# class Solution:
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         # Solution1
#         # a = list(str(x))
#         # b = a[::-1]
#         #
#         # print(a)
#         # print(b)
#         #
#         # a = ''.join(a)
#         # b = ''.join(b)
#         #
#         # if a == b:
#         #     print("Same")
#         # else:
#         #     print("False")
#
#         # Solution2

# Exe 11
# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
# 画 n 条垂直线，使得垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        MaxS = 0
        Cur_Max_xtmp = -1

        # dicVal = {i:height[i] for i in range(len(height))}
        dicVal = dict(zip(range(len(height)),height))
        print(dicVal)

        Cur_Max_x1 = height.index(max(height))
        Cur_Max_y1 = dicVal.pop(height.index(max(height)))

        x_index = list(dicVal.keys())
        v_index = list(dicVal.values())

        index1 = v_index.index(max(dicVal.values()))  #返回字典中最大值的下标
        k = x_index[index1] #返回字典中最大值的索引(key)

        # max(dicVal.values())
        # for k,v in dicVal.items():
        #     if v == max(dicVal.values()):
        #         break

        Cur_Max_x2 = k
        Cur_Max_y2 = dicVal.pop(k)

        print(Cur_Max_y2)
        print(dicVal)
        print('*'*20)


        MINY = min(Cur_Max_y2,Cur_Max_y1)
        Xrange = abs(Cur_Max_x2-Cur_Max_x1)

        S = MINY*Xrange

        if S>MaxS:
            MaxS = S

        print(MaxS)

        if len(dicVal) == 0:
            return MaxS

        for ii in range(len(dicVal)):
            if Cur_Max_xtmp == -1:
                Cur_Max_xtmp = Cur_Max_x1


            dicVal = {k:v for k,v in dicVal.items() if k<min(Cur_Max_x2,Cur_Max_x1,Cur_Max_xtmp) or k>max(Cur_Max_x2,Cur_Max_x1,Cur_Max_xtmp) }
            if len(dicVal)==0:
                print("Current Max Val is ",MaxS)
                return MaxS

            print(dicVal)
            print('*'*20)

            # for k,v in dicVal.items():
            #     if v == max(dicVal.values()):
            #         break

            x_index = list(dicVal.keys())
            v_index = list(dicVal.values())
            index1 = v_index.index(max(dicVal.values()))  # 返回字典中最大值的下标
            k = x_index[index1] # 返回字典中最大值的索引(key)

            Cur_Max_xtmp = k
            Cur_Max_ytemp = dicVal.pop(k)

            print(Cur_Max_ytemp)
            print(dicVal)
            print('*'*20)

            MINY = min(Cur_Max_ytemp,MINY)
            MINX = min(Cur_Max_x2,Cur_Max_x1)
            MAXX = max(Cur_Max_x2,Cur_Max_x1)

            if Cur_Max_xtmp < MINX :
                 Xrange = abs(MAXX-Cur_Max_xtmp)
            else:
                 Xrange = abs(MINX-Cur_Max_xtmp)

            S = MINY*Xrange
            if S>MaxS:
                MaxS = S
                if Cur_Max_xtmp < MINX:
                    Cur_Max_x1 = Cur_Max_xtmp
                    Cur_Max_x2 = MAXX
                else:
                    Cur_Max_x1 = MINX
                    Cur_Max_x2 = Cur_Max_xtmp
                print("*" * 30)
                print("y = ",MINY)
                print("x1 = ", MINX)
                print("x2 = ", MAXX)
                print("*" * 30)

            print("Current S is ",S)
            print("Loop count is ",ii)
            print("Current maxS is ",MaxS)
            # return MaxS
        return MaxS

if __name__ == '__main__':
    newSolution = Solution()

    # Exe 11
    # x = [ 1,11,2,3,2,3,4,5,1,2,2,12]
    # x = [1,2,3,4,5,6,7,8,9,10]
    x = [76,155,15,188,180,154,84,34,187,142,22,5,27,183,111,128,50,58,2,112,179,2,100,111,115,76,134,120,118,103,31,146,
         58,198,134,38,104,170,25,92,112,199,49,140,135,160,20,185,171,23,98,150,177,198,61,92,26,147,164,144,51,196,42,
         109,194,177,100,99,99,125,143,12,76,192,152,11,152,124,197,123,147,95,73,124,45,86,168,24,34,133,120,85,81,163,146,75,92,198,126,191]
    Ma = newSolution.maxArea(x)
    print("Get S is ",Ma)

    # Exe9
    # x = 12321
    # newSolution.isPalindrome(x)

    # Exe8
    # x = "42"
    # newSolution.myAtoi(x)

    # Exe7
    # x = 1534236469
    # newSolution.reverse(x)

    # Exe6
    # s = "PAYPALISHIRING"
    # numRows = 3
    #
    # newSolution.convert(s,numRows)

    # Exe5
    # s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    # newSolution.longestPalindrome(s)

    # Exe4
    # nums1 = [1, 2,5,6]
    # nums2 = [3, 4]
    # newSolution.findMedianSortedArrays(nums1,nums2)

    # res = newSolution.twoSum([-3,0,8,2,3,9],0)
    # print(res)
    # res = newSolution.twoSum([2, 7, 11, 15],9)
    # newSolution.lengthOfLongestSubstring('qwnfenpglqdq')
    # newSolution.lengthOfLongestSubstring('qwnfenpglqdq')


