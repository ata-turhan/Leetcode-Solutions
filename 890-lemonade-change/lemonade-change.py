from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollar_count, ten_dollar_count = 0, 0  # Initialize counts for $5 and $10 bills

        for bill in bills:
            if bill == 5:
                # Customer pays with a $5 bill
                five_dollar_count += 1
            elif bill == 10:
                # Customer pays with a $10 bill, needs $5 change
                if five_dollar_count > 0:
                    five_dollar_count -= 1
                    ten_dollar_count += 1
                else:
                    return False  # Not enough $5 bills for change
            else:  # bill == 20
                # Customer pays with a $20 bill, prioritize giving one $10 and one $5 as change
                if five_dollar_count >= 1 and ten_dollar_count >= 1:
                    ten_dollar_count -= 1
                    five_dollar_count -= 1
                elif five_dollar_count >= 3:
                    # If no $10 bills, give three $5 bills as change
                    five_dollar_count -= 3
                else:
                    return False  # Not enough change for a $20 bill

        return True  # All customers received correct change
