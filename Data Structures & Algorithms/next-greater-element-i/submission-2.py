class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for num in nums1:
            indx = nums2.index(num)
            for j in range(indx + 1, len(nums2)):
                if nums2[indx] < nums2[j]:
                    res.append(nums2[j])
                    break
            else:
                res.append(-1)

        return res
