class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        result = []  # Initialize an empty list to store characters of the smallest string

        for i in range(len(s)):
            for j in range(26):
                new_char = chr(ord('a') + j)  # Generate a new character
                cur_change = min(abs(ord(new_char) - ord(s[i])), 26 - abs(ord(new_char) - ord(s[i])))  # Calculate the change needed to transform s[i] to new_char
                if cur_change > k:
                    continue  # If the change needed is greater than remaining k, skip to the next character
                else:
                    result.append(new_char)  # Add the new character to the result
                    k -= cur_change  # Update the remaining k after making the change
                    if k == 0:
                        result.extend(s[i+1:])  # If k becomes zero, append the remaining characters of s to the result and return
                        return "".join(result)
                    else:
                        break  # Break the inner loop to move to the next character in s

        return "".join(result)  # Return the smallest string formed

        
    
