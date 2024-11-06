class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def get_bit_count(num):
            return bin(num).count("1")

        def swap(i, j):
            if bit_counts[nums[i]] != bit_counts[nums[j]]:
                return False
            else:
                nums[i], nums[j] = nums[j], nums[i]
                return True

        bit_counts = dict()
        for num in nums:
            if num not in bit_counts:
                bit_counts[num] = get_bit_count(num)

        groups = []
        prev_bit_count = bit_counts[nums[0]]
        min_num = 2**9
        max_num = 0
        for num in nums:
            if prev_bit_count == bit_counts[num]:
                min_num = min(min_num, num)
                max_num = max(max_num, num)
            else:
                groups.append(min_num)
                groups.append(max_num)
                prev_bit_count = bit_counts[num]
                min_num = num
                max_num = num

        groups.append(min_num)
        groups.append(max_num)

        return groups == sorted(groups)