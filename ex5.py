# -*- coding:utf-8 -*-
my_name = 'Winnie'
my_age = 35 
my_height = 74 #inches
height_rate = 2.54
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s."%my_name #r为格式化字符，不管什么都打印出来
print "He's %.2f cm tall."%(my_height*2.54)
print "He is %.2f kg heavy."%(my_weight*0.45)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair."%(my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee."%my_teeth
round(3.1415926,2)

#This line is tricky,try to get it exactly right
print "If I add %d,%d,and %d I get %d."%(my_age,my_height,my_weight,my_age+my_height+my_weight)
