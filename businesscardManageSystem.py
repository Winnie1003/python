#coding=utf-8
#Function:businessManageSystem
#Date:2017/7/23
#Author:Winnie

#1.打印提示
print("="*50)
print("1.增加一个名片")
print("2.删除一个名片")
print("3.修改一个名片")
print("4.查询一个名片")
print("5.显示系统中的所有名片")
print("6.退出系统")
print("="*50)


# 定义一个列表
business = []
#2.用户根据提示进行输入,对用户的输入进行合法检查
while True:
    while True:
        #获取用户的操作序号
        num = raw_input("请输入编号进行操作：")
        if num.isdigit():
            num = int(num)
            break
        else:
            print ("输入有误！请输入数字编号！")
    #3.根据用户的选择进行判断
    if num == 1:
        new_name = raw_input("请输入姓名：")
        new_wechat = raw_input("请输入微信号：")
        new_qq = raw_input("请输入qq号：")
        new_addr = raw_input("请输入地址：")

        # 定义一个字典，来存储名片
        card_infos = {}
        card_infos['name'] = new_name
        card_infos['wechat'] = new_wechat
        card_infos['qq'] = new_qq
        card_infos['addr'] = new_addr

        #将一个字典添加到列表当中
        business.append(card_infos)
        # print business  #for test

    elif num == 2:
        flag = 0 #定义一个变量，默认表示没有找到
        del_name = raw_input("请输入要删除的名片")
        for temp in business:
            if del_name == temp['name']:
                business.remove(temp)
                flag = 1
                # print business  #for test
        if flag == 0:
            print ("没有找到要删除的名片！")

    elif num == 3:
        pass

    elif num == 4:
        flag = 0 #定义一个变量，表示没找到
        find_name = raw_input("请输入您要查找的名片：")
        for temp in business:
            if find_name == temp["name"]:
                flag = 1
                print ("%s\t%s\t%s\t%s"%(temp['name'],temp['wechat'],temp['qq'],temp['addr']))
                break
        if flag == 0:
            print ("没有所要查找的名片！")

    elif num == 5:
        print ("姓名\t微信\tqq\t地址")
        for temp in business:
            print ("%s\t%s\t%s\t%s"%(temp['name'],temp['wechat'],temp['qq'],temp['addr']))

    elif num == 6:
        break

    else:
        print ("您的输入有误，请输入正确的编号!")


