class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        d = defaultdict(int)

        for num1 in nums1:
            d[num1[0]] += num1[1]

        for num2 in nums2:
            d[num2[0]] += num2[1]

        return [list(item) for item in sorted(d.items(), key=lambda x: x[0])]