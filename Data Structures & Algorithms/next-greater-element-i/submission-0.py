class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        stack = []

        for i in range(len(nums1)):
            added = False
            indx = nums2.index(nums1[i])
            for j in range(indx + 1, len(nums2)):
                if nums2[indx] < nums2[j]:
                    res.append(nums2[j])
                    added = True
                    break
            if not added:
                res.append(-1)
                

        return res