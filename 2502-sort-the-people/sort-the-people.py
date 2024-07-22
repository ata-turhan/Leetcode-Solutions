class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Combine heights and names into a list of tuples
        persons = list(zip(heights, names))
        # Sort the list of tuples in descending order based on heights
        persons.sort(reverse=True)
        # Extract the names from the sorted list of tuples
        return [name for height, name in persons]
