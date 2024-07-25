from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Helper function to perform merge sort
        def merge_sort(array):
            # Base case: a single-element array is already sorted
            if len(array) <= 1:
                return array
            
            # Find the middle index of the array
            mid = len(array) // 2
            # Recursively sort the left and right halves
            left_half = merge_sort(array[:mid])
            right_half = merge_sort(array[mid:])
            
            # Merge the sorted halves
            return merge(left_half, right_half)
        
        # Helper function to merge two sorted arrays
        def merge(left, right):
            sorted_array = []
            i = j = 0
            
            # Merge the elements from left and right arrays in sorted order
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    sorted_array.append(left[i])
                    i += 1
                else:
                    sorted_array.append(right[j])
                    j += 1
            
            # If there are remaining elements in the left array, add them
            sorted_array.extend(left[i:])
            # If there are remaining elements in the right array, add them
            sorted_array.extend(right[j:])
            
            return sorted_array
        
        # Call merge_sort on the entire array and return the sorted result
        return merge_sort(nums)
