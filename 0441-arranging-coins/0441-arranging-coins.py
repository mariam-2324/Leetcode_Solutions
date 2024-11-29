class Solution:
    def arrangeCoins(self, n: int) -> int:
        s, e = 1, n
        res = 0

        while s <= e:
            mid = (s + e) // 2
            coins = (mid / 2) * (mid + 1)

            if coins > n:
                e = mid - 1
            else:
                s = mid + 1
                res = max(res, mid)
        return res