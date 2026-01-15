class Solution(object):
    def intToRoman(self, num):
        num = str(num).zfill(4)

        ones = {
            "0": "",
            "1": "I",
            "2": "II",
            "3": "III",
            "4": "IV",
            "5": "V",
            "6": "VI",
            "7": "VII",
            "8": "VIII",
            "9": "IX",
        }
        tens = {
            "0": "",
            "1": "X",
            "2": "XX",
            "3": "XXX",
            "4": "XL",
            "5": "L",
            "6": "LX",
            "7": "LXX",
            "8": "LXXX",
            "9": "XC",
        }
        hundreds = {
            "0": "",
            "1": "C",
            "2": "CC",
            "3": "CCC",
            "4": "CD",
            "5": "D",
            "6": "DC",
            "7": "DCC",
            "8": "DCCC",
            "9": "CM",
        }
        thousands = {
            "0": "",
            "1": "M",
            "2": "MM",
            "3": "MMM",
        }

        rom_num = thousands[num[0]] + hundreds[num[1]] + tens[num[2]] + ones[num[3]]

        return rom_num
