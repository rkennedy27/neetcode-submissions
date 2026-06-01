class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""


        lengths = []
        words = []

        for s in strs:
            lengths.append(str(len(s)))
            words.append(s)

        return ",".join(lengths) + ":" + "".join(words)


       

    def decode(self, s: str) -> List[str]:
        decoded_str = []     

        if not s:
            return decoded_str

        length_part, word_part = s.split(":", 1) #
        idx = 0

        for l in length_part.split(","):
            word_length = int(l)
            word = word_part[idx : idx+word_length]
            print("word: " + word)

            decoded_str.append(word)
            idx+=word_length
        
        return decoded_str
        


       
        
            


                


        

           