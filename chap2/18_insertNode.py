def insertNode(listArray,num):
    flag = False     #判断该数值是否插入在链表的中间
    for index in range(len(listArray)):
        if  listArray[index]>=num:
            flag=True
            listArray.insert(index, num)
            break
    if flag==False:
        listArray.append(num)
    return listArray

listLength=int(input()) #链表长度
#链表节点的数值，并且将其转化为环型链表结构
listArray=list(map(int,input().strip().split()))
num=int(input())       #待插入的数值

nodeList=insertNode(listArray,num)
print(" ".join(map(str,nodeList)))