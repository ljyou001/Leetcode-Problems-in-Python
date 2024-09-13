class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        comment_mode = False
        for s in source:
            if not comment_mode:
                output = ''
            parsing_mode = True
            i = 0
            while i < len(s):
                if not comment_mode and (s[i] == "'" or s[i] == '"'):
                    parsing_mode = not parsing_mode
                    i += 1
                elif parsing_mode and i + 3 <= len(s) and s[i: i + 3] == '/*/':
                    comment_mode = not comment_mode
                    i += 3
                elif not comment_mode and parsing_mode and i + 2 <= len(s) and s[i: i + 2] == '//':
                    i = len(s)
                elif not comment_mode and parsing_mode and i + 2 <= len(s) and s[i: i + 2] == '/*':
                    comment_mode = True
                    i += 2
                elif comment_mode and parsing_mode and i + 2 <= len(s) and s[i: i + 2] == '*/':
                    comment_mode = False
                    i += 2
                else:
                    if not comment_mode:
                        output += s[i]
                    i += 1
            if output and not comment_mode:
                res.append(output)
        return res