class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = ''
        for i in strs:
            i = i.replace(';', ';;')
            res += ';' + i
        return res
    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        res = []
        i = 1
        string = ''
        while i < len(str):
            if str[i] != ';':
                string += str[i]
                i += 1
            else:
                if i < len(str) - 1 and str[i] == str[i+1]:
                    string += ';'
                    i += 2
                else:
                    res.append(string)
                    string = ''
                    i += 1
        res.append(string)
        return res