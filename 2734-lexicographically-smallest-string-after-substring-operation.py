class Solution:
    def smallestString(self, s: str) -> str:
        if not s:
            # None or ''
            return ''
        
        s = list(s)
        start = -1
        end = -1
        for i in range(len(s)):
            if start == -1:
                if s[i] == 'a':
                    continue
                else:
                    start = i
            elif s[i] == 'a':
                end = i
                break
                # Remember to break here!

        if start == -1:
            start = len(s) - 1

        s = self.change_char(s, start, end)
        return ''.join(s)

    def change_char(self, s, start, end):
        if end == -1:
            end = len(s)

        for i in range(start, end):
            s[i] = chr(ord(s[i]) - 1) if ord(s[i]) > ord('a') else 'z'

        return s
