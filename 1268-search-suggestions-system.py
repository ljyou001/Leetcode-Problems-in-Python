class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        # res = [products[0:3]]\
        res = []
        for i in range(1, len(searchWord)+1): # Attention: i should start from i as i act as the ending index in the following loop
            resu = []
            for j in products:
                if len(j)>=i and searchWord[0:i] == j[0:i]:
                    resu.append(j)
            res.append(resu[0:3])
        return res