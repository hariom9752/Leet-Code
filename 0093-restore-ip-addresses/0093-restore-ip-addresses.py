class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(i, parts):
            if len(parts) == 4:
                if i == len(s):
                    res.append(".".join(parts))
                return

            for length in range(1, 4):
                if i + length > len(s):
                    break

                part = s[i:i + length]

                if (len(part) > 1 and part[0] == '0') or int(part) > 255:
                    continue

                backtrack(i + length, parts + [part])

        backtrack(0, [])
        return res