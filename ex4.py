# -*- coding:utf-8 -*-

#车的数目
cars = 100 
#一辆车的座位容量
space_in_a_car = 4.0
#司机数
drivers = 30
#乘客数
passengers = 90
#不空闲司机数
cars_not_driven = cars-drivers
#不空闲车数
cars_driven = drivers
#总载客数
carpool_capacity = cars_driven*space_in_a_car
#每辆车的平均司机数
average_passengers_per_car = passengers/cars_driven

print "There are",cars,"cars available."
print "There are only",drivers,"drivers available."
print "We can transport",carpool_capacity,"people today."
print "We have ",passengers,"carpool toaday."
print "We need to put about",average_passengers_per_car,"in each car."