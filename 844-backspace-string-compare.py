class Solution_me:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_res = []
        if len(s)==0: pass
        else:
            for i in s:
                if i == '#' and len(s_res)==0: pass
                elif i== '#' and len(s_res)>0:
                    s_res.pop()
                else:
                    s_res.append(i)
        print(s_res)
        t_res = []
        if len(t)==0: pass
        else:
            for i in t:
                if i == '#' and len(t_res)==0: pass
                elif i== '#' and len(t_res)>0:
                    t_res.pop()
                else:
                    t_res.append(i)
        print(t_res)
        return s_res == t_res

class Solution_Github:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_string(s):
            res = []
            for i in s:
                if i == '#':
                    if len(res) > 0:
                        res.pop()
                else:
                    res.append(i)
            return ''.join(res)
        return get_string(s) == get_string(t)