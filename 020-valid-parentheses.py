class Solution:
    def isValid(self, s: str) -> bool:
        bracket = []
        
        for i in s:
            if i in ["(", "{", "["]:
                bracket.append(i)
            elif i == ")" and len(bracket) > 0 and bracket[-1] == "(":
                bracket.pop()
            elif i == "]" and len(bracket) > 0 and bracket[-1] == "[":
                bracket.pop()
            elif i == "}" and len(bracket) > 0 and bracket[-1] == "{":
                bracket.pop()
            else: 
                return False
        return not bracket