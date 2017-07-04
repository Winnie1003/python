# -*- coding:utf-8 -*-
x = "There are %d types of people." %10
binary  = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" %(binary,do_not) #字符串嵌套字符串1

print x #打印字符串x
print y #打印字符串y

print "I said:%r" %x #字符串嵌套字符串2

print "I also said:'%s'." %y #字符串嵌套字符串3

hilarious = False
joke_evaluation = "Isn''t that joke so funny?%r"

print joke_evaluation % hilarious #字符串嵌套字符串4

w = "This is a left side of..."
e = "a string with a right side."
print w+e

#常见问题
	#1. %r与%s有什么不同
	#答：%r用来debug更好，因为它会显示变量的原始数据raw data,而其他的符号则是用来向用户显示输出的。
	#2.既然有了%r了，为什么还要用%s和%d?
	#答：%r用来debug最好，其他数据则是用来向用户显示输出的。


