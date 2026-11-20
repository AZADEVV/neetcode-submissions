class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1 = set(nums1)
        nums2 = set(nums2)

        res = []
        for num1 in nums1:
            if num1 in nums2 and num1 not in res:
                res.append(num1)

        return res