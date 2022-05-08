class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = {}
        for i in cpdomains:
            num_name = i.split(" ")
            names = num_name[1].split('.')
            j = len(names) - 1
            while j >= 0:
                name = '.'.join(str(e) for e in names[j:len(names)])
                print(num_name[0], name)
                if name in res: 
                    res[name] += int(num_name[0])
                else: 
                    res[name] = int(num_name[0])
                j = j - 1
        result = []
        for i in res.keys():
            result.append(str(res[i])+" "+i)
        return result