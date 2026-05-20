class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for c in strs:
            encoded_str+= str(len(c)) + "#" + c
        return encoded_str
            

    def decode(self, s: str) -> List[str]:
        #____5#hello5#world
        strs = []
        i = 0

        while i < len(s):
            word_length = 0
            while s[i] != "#":
                word_length = word_length * 10 + int(s[i])
                i += 1
        
            i+=1
            word = s[i : i + word_length]
            strs.append(word)
            
            i+=word_length
        return strs

            

