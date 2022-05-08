class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email = []
        for i in emails:
            i = i.split("@")
            if "+" in i[0]: 
                i[0] = i[0].split("+")
                i[0] = i[0][0]
            if "." in i[0]:
                i[0] = i[0].split(".")
                i[0] = ''.join(str(e) for e in i[0])
            email.append(str(i))
        return len( set(email) )