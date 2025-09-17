from typing import List
from sortedcontainers import SortedList

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        """
        Initializes the FoodRatings system with food names, their cuisines, and ratings.
        """
        self.food_info = {}      # Maps food name → (rating, cuisine)
        self.cuisine_map = {}    # Maps cuisine → SortedList of (-rating, food name)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            entry = (-rating, food)
            if cuisine not in self.cuisine_map:
                self.cuisine_map[cuisine] = SortedList()
            self.cuisine_map[cuisine].add(entry)
            self.food_info[food] = (rating, cuisine)

    def changeRating(self, food: str, newRating: int) -> None:
        """
        Updates the rating of the given food and maintains SortedList ordering.
        """
        old_rating, cuisine = self.food_info[food]
        old_entry = (-old_rating, food)
        self.cuisine_map[cuisine].remove(old_entry)

        new_entry = (-newRating, food)
        self.cuisine_map[cuisine].add(new_entry)
        self.food_info[food] = (newRating, cuisine)

    def highestRated(self, cuisine: str) -> str:
        """
        Returns the name of the highest-rated food in the specified cuisine.
        Ties are broken by lexicographical order of food names.
        """
        return self.cuisine_map[cuisine][0][1]
