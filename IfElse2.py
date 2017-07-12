#coding=utf-8
#判断用户是否为白富美

color = raw_input("Are you fair-skinned?")
rich = raw_input("Are you rich enough?")
beatiful = raw_input("Are you attractive?")

if color == "yes" and rich == "yes" and beatiful == "yes":
    print("You are a fair-skinned and attractive!")
else:
    print("You are not perfect!")