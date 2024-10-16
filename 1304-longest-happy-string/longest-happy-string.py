class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counts = []
        if a > 0:
            counts.append([-a, "a"])
        if b > 0:
           counts.append([-b, "b"])
        if c > 0:
            counts.append([-c, "c"])
        heapify(counts)
        happy_string = []

        while counts:
            count, char = heappop(counts)
            count = -count
            if len(happy_string) >= 2 and happy_string[-2:] == [char] * 2:
                if not counts:
                    break
                else:
                    second_count, second_char = heappop(counts)
                    second_count = -second_count
                    happy_string.append(second_char)
                    if second_count != 1:
                        heappush(counts, [-second_count+1, second_char])
                    heappush(counts, [-count, char])
            else:
                happy_string.append(char)
                if count != 1:
                    heappush(counts, [-count+1, char])

        return "".join(happy_string)

            

            


        