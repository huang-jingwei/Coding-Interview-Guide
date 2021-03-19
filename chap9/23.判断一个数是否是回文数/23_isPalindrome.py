import copy
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x==0:                        # 输入数值为0，为回文字符串
            return True
        elif x<0:                       # 输入数值为负数，不可能为回文字符串
            return False
        else:
            numArray=[]                 # 获得输入数值的各个位数
            while x>0:
                numArray.append(x % 10)
                x=x // 10    
            numStack=copy.copy(numArray)

            while len(numArray)>0:
                num1=numArray.pop(0)
                num2=numStack.pop()

                if num1 !=num2:
                    return False
            return True