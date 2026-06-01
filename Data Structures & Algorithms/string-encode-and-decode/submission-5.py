class Solution:

    def encode(self, strs: List[str]) -> str:
        #Hello World--> 5#Hello5#World


        encoded_str = ""

        for s in strs:
            preFix = str(len(s)) + "#"
            encoded_str += preFix + s
        
        print("Encoded: " + encoded_str)

        return encoded_str

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        
        while i < len(s):
            word_length = 0
           
            while s[i] != "#":
                word_length = word_length * 10 + int(s[i])
                i+=1
            
            #now s[i] = "#" --> need to advance 
            i+=1

            word = s[i : i + word_length]
            strs.append(word)

            i+=word_length
        return strs
            
        
            


                


        

           