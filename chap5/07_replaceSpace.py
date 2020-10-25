class Solution:
    def replaceSpace(self, s: str) -> str:
        array=[s[i] for i in range(len(s))]
        for i in range(len(array)):
            if array[i]==" ":
                array[i]='%20'
        string=""
        for i in range(len(array)):
            string=string+array[i]
        return string