class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        persons = list(zip(heights, names))
        persons.sort(reverse=True)
        return [name for height, name in persons]