# 处理输入
# step1：字符串长度
stringLength = list(map(int, input().strip().split()))
n = stringLength[0]
m = stringLength[1]
# step2：获取字符串
str1 =input().strip()
str2 =input().strip()


# 主函数入口
# 若两个字符串互为变形词，那么字符串长度必然一致
if len(str1) != len(str2):
    print("false")
    exit()
string_times = {}

for index in range(len(str1)):
    if str1[index] not in string_times:
        string_times[str1[index]] = 1
    else:
        string_times[str1[index]] += 1

    if str2[index] not in string_times:
        string_times[str2[index]] = -1
    else:
        string_times[str2[index]] -= 1
for key, time in string_times.items():
    if time != 0:
        print("false")
        exit()
print("true")