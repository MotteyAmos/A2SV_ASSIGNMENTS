class Solution:
    def freqAlphabets(self, s: str) -> str:
        dict_val = {}

        num = 1
        for i in range(97,123):
            chr_val = chr(i)
            
            if num < 10:
                num_str = str(num)
            else:
                num_str = str(num) + "#"
            num += 1
            dict_val.setdefault(num_str, chr_val)
        
        if len(s) == 1:
            return dict_val(s[0])
        elif len(s) == 2:
            return dict_val(s[0]+s[1])
        
        count = 0
        new_s = ""
        while count < len(s) -2:
            if s[count+2] != "#":
                new_s += dict_val[s[count]]
            else:
                new_s = new_s + dict_val[s[count:count + 3]]
                count += 2
            count +=1
        
        for i in range(count, len(s)):
            new_s +=  dict_val[s[i]]

        return new_s
