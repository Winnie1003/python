#coding=utf-8
import random

#1.获取用户输入
player = int(input("please input a number:0:剪刀,1:石头,2:布..."))

#2.获取电脑输入
computer = random.randint(0,2)

#3.将玩家的输入和电脑的输入作比较
#玩家盈
if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
	print("Congradulation!You win!")
#平局
elif player == computer:
	print("WIN-WIN!")
#玩家输
else:
	print("Sorry!You failed!")

