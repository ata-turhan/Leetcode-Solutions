class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:len(s1)])
        matched = 0
        required = len(s1_counter)
        for letter in s1_counter:
            if s1_counter[letter] <= s2_counter[letter]:
                matched += 1
        if matched == required:
            return True

        for i in range(len(s1), len(s2)):
            deleted_char = s2[i - len(s1)]
            if s2_counter[deleted_char] == s1_counter[deleted_char]:
                matched -= 1
            s2_counter[deleted_char] -= 1

            added_char = s2[i]
            if (s2_counter[added_char] + 1 ) == s1_counter[added_char]:
                matched += 1
            s2_counter[added_char] += 1

            if matched == required:
                return True

        return False

            


        