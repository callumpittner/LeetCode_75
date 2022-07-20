class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dictionary = {}
        t_dictionary = {}
        for idx, letter in enumerate(s):
            ltr1, ltr2 = letter, t[idx]

            if ltr1 in s_dictionary and s_dictionary[ltr1] != ltr2:
                return False
            if ltr2 in t_dictionary and t_dictionary[ltr2] != ltr1:
                return False
            s_dictionary[ltr1] = ltr2
            t_dictionary[ltr2] = ltr1
        return True
            
