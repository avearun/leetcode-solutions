# Brute Force Soultion
class Solution(object):
    def containDuplicate(self,nums):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
        return False
# Create instance of class
sol = Solution()
# Check Solution
test1 = [1,2,3,1]
test2 = [2,3,4,5,6]
test3 = [2,3,3,3]
