from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        """
        Implements LeetCode 966: Vowel Spellchecker.

        Strategy (in strict precedence order):
          1) Exact match (case-sensitive)
          2) Case-insensitive match (return first word in wordlist with same lowercase form)
          3) Vowel-error match (treat all vowels as the same token and match on lowercase)
          4) If none match, return ""

        Time:
          Building indices:  O(N * L)
          Answering queries: O(M * L)
          (N = len(wordlist), M = len(queries), L <= 7)

        Space:
          O(N * L) for indices.
        """
        vowels = set("aeiou")

        def mask_vowels_lower(s: str) -> str:
            """Lowercase s and replace every vowel with a sentinel (e.g., '*')."""
            s = s.lower()
            # Using list comprehension is faster than repeated string concatenation for small L.
            return "".join('*' if ch in vowels else ch for ch in s)

        # 1) Exact match set for O(1) lookups (case-sensitive).
        exact_words = set(wordlist)

        # 2) Case-insensitive dictionary: lowercase(word) -> first occurrence in wordlist
        first_case_insensitive: dict[str, str] = {}

        # 3) Vowel-error dictionary: mask_vowels_lower(word) -> first occurrence in wordlist
        first_vowel_masked: dict[str, str] = {}

        for w in wordlist:
            lw = w.lower()
            mw = mask_vowels_lower(w)
            # setdefault keeps the first encountered mapping, as required by the problem.
            first_case_insensitive.setdefault(lw, w)
            first_vowel_masked.setdefault(mw, w)

        result: List[str] = []
        for q in queries:
            if q in exact_words:
                # Rule 1: exact (case-sensitive) match
                result.append(q)
                continue

            lw = q.lower()
            if lw in first_case_insensitive:
                # Rule 2: case-insensitive match; return first word from wordlist
                result.append(first_case_insensitive[lw])
                continue

            mw = mask_vowels_lower(q)
            if mw in first_vowel_masked:
                # Rule 3: vowel-error match; return first word from wordlist
                result.append(first_vowel_masked[mw])
                continue

            # Rule 4: no match
            result.append("")

        return result
