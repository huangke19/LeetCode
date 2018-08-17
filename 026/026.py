import copy

class Solution:

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bag = set()
        newnums = copy.deepcopy(nums)
        for n in newnums:
            if n in bag:
                nums.remove(n)
            else:
                bag.add(n)
        return len(nums)

s = Solution()

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
s.removeDuplicates(nums)

print(s)
print(nums)
