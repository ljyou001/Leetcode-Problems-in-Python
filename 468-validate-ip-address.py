CHARSET4 = set('0123456789')
CHARSET6 = set('0123456789ABCDEFabcdef')

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if not queryIP:
            return 'Neither'

        queryIP = queryIP.split('.')
        if len(queryIP) == 4:
            return self.valid_v4(queryIP)
        elif len(queryIP) == 1:
            queryIP = queryIP[0].split(':')
            if len(queryIP) == 8:
                return self.valid_v6(queryIP)

        return 'Neither'

    def valid_v4(self, queryIP):
        for seg in queryIP:
            if not 1 <= len(seg) <= 3:
                return 'Neither'
            for char in seg:
                if char not in CHARSET4:
                    return 'Neither'
            intseg = int(seg)
            if not 0 <= intseg <= 255:
                return 'Neither'
            if not str(intseg) == seg:
                return 'Neither'
        return 'IPv4'

    def valid_v6(self, queryIP):
        for seg in queryIP:
            if not 1 <= len(seg) <= 4:
                return 'Neither'
            for char in seg:
                if char not in CHARSET6:
                    print(char)
                    return 'Neither'
        return 'IPv6'