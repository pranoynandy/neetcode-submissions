class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr = ''
        for word in strs:
            newStr += str(len(word)) + '#' + word
        return newStr

    def decode(self, s: str) -> List[str]:
        org,i = [],0
        num,word = '',''
        while i in range(len(s)):
            if s[i] != '#':
                num += s[i]
                i += 1
            elif s[i] == '#':
                num = int(num)
                word = s[i+1:i+num+1]
                org.append(word)
                i += num+1
                num = ''
        return org

            
