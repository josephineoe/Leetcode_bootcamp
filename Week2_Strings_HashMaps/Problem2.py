class Solution:
    def findAnagrams(self, s: str, p: str):
        res = []
        len_p, len_s = len(p), len(s)

        if len_p > len_s:
            return res

        p_count = Counter(p)
        s_count = Counter(s[:len_p - 1])

        for i in range(len_p - 1, len_s):
            s_count[s[i]] += 1  # include new char
            
            if s_count == p_count:
                res.append(i - len_p + 1)

            # remove leftmost char
            left_char = s[i - len_p + 1]
            s_count[left_char] -= 1
            if s_count[left_char] == 0:
                del s_count[left_char]

        return res
