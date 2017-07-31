#coding=utf-8

#功能：定义一个函数，这个函数可以接受三个变量,把这三个值的和打出来
def sum_three_nums(a,b,c):
    result = a+b+c
    # print ("%d+%d+%d=%d"%(a,b,c,result))
    return result

def average_3_nums(a1,b1,c1):
    result = sum_three_nums(a1,b1,c1)
    result /= 3 #result = result/3
    print ("平均值为%d"%result)

#用户输入第一个值
num1 = int(raw_input("please input a number:"))

#用户输入第二个值
num2 =int(raw_input("please input a number:"))

#用户输入第三个值
num3 = int(raw_input("please input a number:"))

# sum_three_nums(num1,num2,num3)
average_3_nums(num1,num2,num3)
