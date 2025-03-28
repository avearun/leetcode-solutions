
# Brute Force Soultion
class Solution(object):
    def containsDuplicate(self,nums):
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

# print solutions

print(sol.containsDuplicate(test1))
print(sol.containsDuplicate(test2))
print(sol.containsDuplicate(test3))

#time complexity : O(n^2)
#space complexity: O(1)

#-------------------------------------------------------------------------------------------------------------

# Sort + Two pointer Solution

class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                return True
        return False
# Create instance of class
sol = Solution()
# Check Solution
test1 = [1,2,3,1]
test2 = [2,3,4,5,6]
test3 = [2,3,3,3]

# Print Solutions
print(sol.containsDuplicate(test1))
print(sol.containsDuplicate(test2))
print(sol.containsDuplicate(test3))

#time complexity : O(n logn)
#space complexity: O(1)

#------------------------------------------------------------------------------------------

# HashSet Method

class Solution(object):
    def containsDuplicate(self, nums):
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False

# Create instance of class
sol = Solution()
# Check Solution
test1 = [1,2,3,1]
test2 = [2,3,4,5,6]
test3 = [2,3,3,3]

# Print Solutions
print(sol.containsDuplicate(test1))
print(sol.containsDuplicate(test2))
print(sol.containsDuplicate(test3))        
             
#time complexity : O(n)
#space complexity: O(n)
