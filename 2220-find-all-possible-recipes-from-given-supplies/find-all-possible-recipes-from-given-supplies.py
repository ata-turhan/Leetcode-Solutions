class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        supplies_set = set(supplies)
        res = set()

        for _ in range(n):
            for recipe, ingredient in zip(recipes, ingredients):
                if all(i in supplies_set for i in ingredient):
                    res.add(recipe)
                    supplies_set.add(recipe)

        return list(res)

        