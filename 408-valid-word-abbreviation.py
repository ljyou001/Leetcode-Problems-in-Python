# LINT 637

class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def valid_word_abbreviation(self, word: str, abbr: str) -> bool:
        # write your code here
        s_index = 0
        a_index = 0
        numbers = set('0123456789')
        while s_index < len(word) and a_index < len(abbr):
            if abbr[a_index] not in numbers:
                if abbr[a_index] != word[s_index]:
                    return False
                a_index += 1
                s_index += 1
                continue

            skip_num = abbr[a_index]
            if skip_num == '0':
                return False
            a_index += 1
            while a_index < len(abbr) and abbr[a_index] in numbers:
                skip_num += abbr[a_index]
                a_index += 1
            skip_num = int(skip_num)
            s_index += skip_num
        return s_index == len(word) and a_index == len(abbr)