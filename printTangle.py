#coding=utf-8
#打印如下所示的一个三角形
#*
#**
#***
#****
#*****
i = 1
while i <= 5:

	#用来控制每一行的列数
	j = 1
	while j <= i:
		print("*"),
		j = j+1
		
	print("")
	
	i = i+1