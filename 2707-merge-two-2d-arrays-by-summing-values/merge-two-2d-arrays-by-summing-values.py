class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        id_to_values = defaultdict(int)

        for id_, val in nums1:
            id_to_values[id_] += val

        for id_, val in nums2:
            id_to_values[id_] += val

        res = []

        for key in sorted(id_to_values.keys()):
            res.append([key, id_to_values[key]])

        return res