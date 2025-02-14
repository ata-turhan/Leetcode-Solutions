class ProductOfNumbers:

    def __init__(self):
        """
        Initializes the data structure to store the sequence of numbers 
        and their prefix product values.
        """
        self.numbers = []  # Stores the sequence of numbers
        self.last_zero_index = -1  # Tracks the last occurrence of zero
        self.prefix_products = []  # Stores prefix product values

    def add(self, num: int) -> None:
        """
        Adds a number to the sequence and updates the prefix product list.
        If the number is zero, reset the prefix product calculations.
        """
        self.numbers.append(num)

        if num == 0:
            self.last_zero_index = len(self.numbers) - 1  # Mark the index of the last zero
            self.prefix_products.append(1)  # Reset prefix product after zero
        else:
            if self.prefix_products:
                self.prefix_products.append(self.prefix_products[-1] * num)
            else:
                self.prefix_products.append(num)

    def getProduct(self, k: int) -> int:
        """
        Returns the product of the last k numbers in the sequence.
        If there is a zero in the range, the product is 0.
        """
        start_index = len(self.numbers) - k

        if start_index <= self.last_zero_index:
            return 0
        return self.prefix_products[-1] if start_index == 0 else self.prefix_products[-1] // self.prefix_products[start_index - 1]



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)