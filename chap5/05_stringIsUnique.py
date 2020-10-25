#基本思路：用哈希表储存已经出现的字符
#算法时间复杂度：O(N),算法空间复杂度：O(N)
def isUnique(string):
    if string==None:
        return True
    data={}  #记录已经出现的字符
    for item in string:
        if item not in data:
            data[item]=1
        else:
            return  False
    return  True