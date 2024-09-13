big_string = ["Thousand", "Million", "Billion"]
digit_string = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teen_string = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
ten_string = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        num_str = str(num)
        res = []
        big_count = 0

        while num_str:
            chunk = num_str[-3:]
            num_str = num_str[:-3]
            
            if int(chunk) > 0:
                chunk_word = self.handling_three_digits(chunk)
                if big_count > 0:
                    chunk_word += ' ' + big_string[big_count - 1]
                res.append(chunk_word)
            big_count += 1
        
        return ' '.join(res[::-1])
    
    def handling_three_digits(self, chunk):
        n = int(chunk)
        if n == 0:
            return ""
        
        res = []
        
        if n >= 100:
            res.append(digit_string[n // 100] + " Hundred")
            n %= 100
        
        if n >= 20:
            res.append(ten_string[n // 10])
            if n % 10 > 0:
                res.append(digit_string[n % 10])
        elif n >= 10:
            res.append(teen_string[n - 10])
        elif n > 0:
            res.append(digit_string[n])
        
        return ' '.join(res)