class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Count frequencies of each character
        freq = Counter(s)
        
        # Use a max heap for characters (-ord(char) for max heap)
        max_heap = [(-ord(char), char, count) for char, count in freq.items()]
        heapq.heapify(max_heap)
        
        result = []
        
        while max_heap:
            # Get the largest character
            _, char, count = heapq.heappop(max_heap)
            
            # How many times can we add this character?
            max_add = min(count, repeatLimit)
            result.extend([char] * max_add)
            
            # If we have leftover count for this character
            if count > max_add:
                # Check if we can add a smaller character in between
                if max_heap:
                    # Get the next largest character
                    _, next_char, next_count = heapq.heappop(max_heap)
                    
                    # Add one of the next largest character
                    result.append(next_char)
                    
                    # If there's more of the next character, push it back
                    if next_count > 1:
                        heapq.heappush(max_heap, (-ord(next_char), next_char, next_count - 1))
                    
                    # Push the remaining of the current character back
                    heapq.heappush(max_heap, (-ord(char), char, count - max_add))
                else:
                    # If no smaller character is available, we're done
                    break
        
        return ''.join(result)

        