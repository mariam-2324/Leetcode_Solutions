class Solution:
    def sortString(self, s: str) -> str:
        # 1) Build frequency dictionary
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        result = []

        # 2) Continue until all characters are used
        while len(result) < len(s):

            # Increasing order
            for ch in sorted(freq.keys()):
                if freq[ch] > 0:
                    result.append(ch)
                    freq[ch] -= 1

            # Decreasing order
            for ch in sorted(freq.keys(), reverse=True):
                if freq[ch] > 0:
                    result.append(ch)
                    freq[ch] -= 1

        return "".join(result)