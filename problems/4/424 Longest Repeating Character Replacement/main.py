class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        freq = Counter()
        total = major = 0
        result = 0 
        for j in range(len(s)):
            freq[s[j]] += 1
            major = max(major, freq[s[j]])
            total += 1
            if total - major <= k:
                result = max(result, j - i + 1)
            else:
                # remove s[i]
                freq[s[i]] -= 1
                total -= 1
                i += 1
        return result        