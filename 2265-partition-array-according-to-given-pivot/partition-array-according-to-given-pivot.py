class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smallers, equals, largers = [], [], []

        for num in nums:
            if num < pivot:
                smallers.append(num)
            elif num > pivot:
                largers.append(num)
            else:
                equals.append(num)

        return smallers + equals + largers
        