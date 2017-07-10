#-*-coding:utf=8-*-

age = raw_input("please input your age:") #获取用户输入的年龄

age_num = int(age) #将用户输入的字符串类型的年龄转化为整型数字
print(age_num)

if age_num > 18:
    print("you have been an adult!")
else:
    print("you are an child!")