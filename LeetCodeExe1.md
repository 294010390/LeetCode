# 1.两数之和
- 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
- 示例:
    - 给定 nums = [2, 7, 11, 15], target = 9, 
    因为 nums[0] + nums[1] = 2 + 7 = 9, 
    所以返回 [0, 1]
    
    思路1：
    1.在列表中remove Num[0]生成新列表L
    2.在新列表L中搜索target-Num[0]，如果结果存在新列表L中，则return结果
    3.如果target-Num[0]不在新列表中，则判断Num[1]是否满足条件，以此类推
    
    思路2：
    1.Target - Num[i]生成新列表L
    2.求列表L和Nums的并集，得出结果

- 代码：
    - 方式1实现 （执行时间：1840 ms）   

        def twoSum(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            newnums = [] # 用以生成新列表L
            [newnums.append(nums[i]) for i in range(len(nums))] # 用以生成新列表L
    
            for i in nums: 
                num1 = i
                num2 = target - i
                
                if num1 in nums :
    
                    if num1 == num2: 
                        newnums.remove(num1)
    
                    if num2 in newnums:
                        if num1 == num2:
                            return [nums.index(num1), newnums.index(num2)+1]
                        else:
                            return [nums.index(num1), nums.index(num2)]
    - 方式2实现：（执行时间：48 ms）
    
        def twoSum(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            newnums = []
            result = []
            
            [newnums.append(target-nums[i]) for i in range(len(nums))] # 用以生成新列表L
    
            a = list(set(nums).intersection(newnums)) #求两个列表的交集
    
            if len(a)>2:
                [a.remove(i) for i in a if i == target or i == target/2] #排除异常的可能性
    
            if len(a)==1: # 两个值相等的情况
                result.append(nums.index(a[0]))
                nums.remove(a[0])
                result.append(1+nums.index(a[0]))
            elif len(a) == 2: # 两个值不等的情况
                result.append(nums.index(a[0]))
                result.append(nums.index(a[1]))
    
            return result
            
    
