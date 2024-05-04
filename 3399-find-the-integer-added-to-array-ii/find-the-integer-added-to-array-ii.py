class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        # Sort the input lists
        nums1.sort()
        nums2.sort()
        
        # Initialize the result to positive infinity
        res = float("inf")
        
        # Iterate through pairs of elements in nums1
        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                # Create a copy of nums1 with the current pair removed
                cop = list(nums1)
                del cop[j]
                del cop[i]
                
                # Calculate the difference between the minimum element in nums2 and the minimum element in the modified nums1
                diff = min(nums2) - min(cop)
                
                # Check if the difference is consistent across all corresponding elements in nums2 and the modified nums1
                for k in range(len(nums2)):
                    if nums2[k] - cop[k] != diff:
                        break
                else:
                    # If the difference is consistent, update the result
                    res = min(res, diff)
        
        # Return the minimum added integer required to make the modified nums1 identical to nums2
        return res
