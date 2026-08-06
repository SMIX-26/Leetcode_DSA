class Solution:
    def frequencySort(self, s: str) -> str:

        freq = {}

        
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        ans = ""

        while len(freq) > 0:

            max_char = ""
            max_count = 0

            
            for i in freq:
                if freq[i] > max_count:
                    max_count = freq[i]
                    max_char = i

            
            ans += max_char * max_count

        
            del freq[max_char]

        return ans
        