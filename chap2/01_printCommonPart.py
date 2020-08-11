def printCommonPart(array1,array2):
    data=[]
    index1=0
    index2=0
    while index1 <len(array1) and index2 <len(array2):
        if array1[index1]==array2[index2]:
            data.append(array1[index1])
            index1 +=1
            index2 +=1
        elif array1[index1]<array2[index2]:
            index1 +=1
        elif array1[index1]>array2[index2]:
            index2 +=1
    return data


n = int(input())
array1 = list(map(int,input().strip().split()))
m = int(input())
array2 = list(map(int,input().strip().split()))
data=printCommonPart(array1, array2)
print(' '.join(map(str,data)))