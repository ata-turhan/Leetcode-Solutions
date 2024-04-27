class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge two sorted arrays nums1 and nums2 into nums1 in-place.
        
        Args:
            nums1 (List[int]): First sorted array with extra space at the end.
            m (int): Number of elements in nums1.
            nums2 (List[int]): Second sorted array.
            n (int): Number of elements in nums2.
            
        Returns:
            None: Modifies nums1 in-place.
        """
        # Initialize pointers for nums1, nums2, and the write index
        a, b, write_index = m - 1, n - 1, m + n - 1

        # Loop until all elements of nums2 are merged into nums1
        while b >= 0:
            # Compare elements pointed to by pointers a and b
            if a >= 0 and nums1[a] > nums2[b]:
                # If element from nums1 is larger, place it at the end of nums1
                nums1[write_index] = nums1[a]
                a -= 1
            else:
                # Otherwise, place element from nums2 at the end of nums1
                nums1[write_index] = nums2[b]
                b -= 1

            # Move write index and pointer for nums1 backwards
            write_index -= 1

        # No need to handle remaining elements in nums1 as they are already in place
