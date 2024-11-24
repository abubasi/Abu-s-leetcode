class Solution:
    def twosum(self,nums,target):
        has_map = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in has_map:
                return [has_map[diff],i]
            has_map[num] = i
if __name__=="__main__":
    solution=Solution()
    nums=[2,7,5,6]
    target=9
    result=solution.twosum(nums,target)
    print(result)
