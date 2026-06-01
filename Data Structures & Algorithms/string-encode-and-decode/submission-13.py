class Solution:

    def encode(self, strs: List[str]) -> str:
        
        if not strs:
            return ""

        encoded_str = ""

        
        length_part = str(len(strs[0])) #lengths seperated by ","
        word_part = strs[0] #all words put directly one after eachother

        for s in strs[1:]:
            length_part+="," + str(len(s))
            word_part+=s
        
        #split by : later in decode bc we know length wont have any ":" and only spliting into 2 categoriues
        encoded_str = length_part + ":" + word_part

        print(encoded_str)
        return encoded_str
       

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


        # lengths = [int(x) for x in length_part.split(",")]

        # idx = 0
        # for word_length in lengths:
        #     word = word_part[idx : idx+word_length]
        #     print("word: " + word)

        #     decoded_str.append(word)
        #     idx+=word_length
        
        return decoded_str
        


       
        
            


                


        

           