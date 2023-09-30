class Solution:
    def intToRoman(self, num: int) -> str:
        intToRoman = {
            "1": "I",
            "5": "V",
            "10": "X",
            "50": "L",
            "100": "C",
            "500": "D",
            "1000": "M",
            "4": "IV",
            "9": "IX",
            "40": "XL",
            "90": "XC",
            "400": "CD",
            "900": "CM"
        }
        
        def ones(n):
            if(n < 4):
                return intToRoman["1"] * n
            elif(n == 4):
                return intToRoman["4"]
            elif(n == 5):
                return intToRoman["5"]
            elif(n > 5 and n < 9):
                return intToRoman["5"] + (intToRoman["1"] * (n-5))
            elif(n == 9):
                return intToRoman["9"]
            else:
                ""
        
        def tensz(n):
            tens = n // 10
            if(n < 40):
                return (intToRoman['10'] * tens) + ones(n - (tens*10))
            elif(n >= 40 and n < 50):
                return intToRoman['40'] + ones(n-40)
            elif(n >= 50 and n < 90):
                return intToRoman['50'] + (intToRoman['10'] * (tens-5)) + ones(n - (tens*10))
            elif(n >= 90 and n < 100):
                return intToRoman['90'] + ones(n-90)
            else:
                return ""
        
        def hundres(n):
            hund = n//100
            if(n < 400):
                return (intToRoman['100'] * hund) + tensz(n - (hund*100))
            elif(n >=400 and n < 500):
                return intToRoman['400'] + tensz(n-400)
            elif(n >= 500 and n < 900):
                return intToRoman['500'] + (intToRoman['100'] * (hund-5)) + tensz(n - (hund*100))
            elif(n >= 900 and n < 1000):
                return intToRoman['900'] + tensz(n-900)
            else:
                return ""
            
        def thousands(n):
            thou = n //1000
            return (intToRoman["1000"] * thou) + hundres(n-(thou*1000))
    
        rom = ''
        numString = str(num)
        
        if(numString in intToRoman):
            rom = intToRoman[numString]
        else:
            length = len(numString)
            if(length == 1):
                rom = ones(num)
            elif(length == 2):
                rom = tensz(num)
            elif(length == 3):
                rom = hundres(num)
            elif(length == 4):
                rom = thousands(num)

        return rom