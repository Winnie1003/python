#coding=utf-8
#打印功能提示
print("="*50+"Name Manage System"+"="*50)

#获取用户选择
print("1:增加一个学生")
print("2:删除一个学生")
print("3:修改学生的姓名")
print("4:查询学生姓名")
print ("5:退出系统")
print("="*120)

#定义一个空的列表来存放添加的学生姓名
names = []

while True:

    #对用户的输入进行合法检查
    while True:
        num = raw_input("请输入编号进行操作：")
        if num.isdigit():
            num = int(num)
            break
        else:
            print ("输入有误！请输入数字编号！")

    #根据用户的选择，执行相应的功能
    #添加学生
    if num == 1:
        new_name = raw_input("请输入要添加的学生的姓名：")
        names.append(new_name)
        print(names)
    #删除学生
    elif num == 2:
        del_name = raw_input("请输入要删除的学生的姓名：")
        if del_name in names:
            names.remove(del_name)
            print (names)
    #修改学生姓名
    elif num == 3:
        exsit_name = raw_input("请输入您要修改的学生的姓名:")
        if exsit_name in names:
            i = 0
            modify_name = raw_input("请输入修改后的姓名：")
            for i in range(len(names)):
                if names[i] == exsit_name:
                    names[i] = modify_name
                    i += 1
                else:
                    i += 1
            print names
        else:
            print ("您要修改的学生姓名不存在！")
    #查询学生姓名
    elif num == 4:
        find_name = raw_input("请输入您要查询的学生的姓名：")
        if find_name in names:
            print ("找到了")
        else:
            print ("没有您要找的学生！")
    #退出系统
    elif num == 5:
        break
    else:
        print ("您输入的信息有误！请重新输入！")
