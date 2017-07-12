#coding=utf-8
#打印九九乘法表

i = 1

#打印每一行的值
while i <= 9:

	j = 1
	
	while j <= i:
		print("%d*%d=%d\t"%(j,i,i*j)),
		j += 1
		
	print("")	
	
	i += 1