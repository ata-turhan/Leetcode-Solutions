from typing import List

class Solution:
    def findAllRecipes(
        self,
        recipes: List[str],
        ingredients: List[List[str]],
        supplies: List[str]
    ) -> List[str]:
        """Finds all recipes that can be prepared using available supplies and other recipes."""

        available = set(supplies)
        discovered_recipes = set()
        total_recipes = len(recipes)

        # Perform up to n passes to allow chained dependency resolution
        for _ in range(total_recipes):
            for recipe, required_ingredients in zip(recipes, ingredients):
                if recipe in discovered_recipes:
                    continue  # Already added
                
                if all(item in available for item in required_ingredients):
                    discovered_recipes.add(recipe)
                    available.add(recipe)

        return list(discovered_recipes)
