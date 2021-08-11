from interface import admin_interface

def frozen():
    while True:
        frozen_user = input('请输入要冻结的用户名:')
        flag,msg = admin_interface.frozen_interface(
            frozen_user
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)
            continue

def change_balance():
    while True:

        change_bal_user = input('请输入要修改余额的用户名:')
        change_money = input('请输入要修改的金额:')
        flag,msg = admin_interface.change_bal_interface(
            change_bal_user,change_money
        )

        if flag:
            print(msg)
            break
        else:
            print(msg)
            continue

def relieve():

    while True:
        relieve_user = input('请输入要解冻的用户名:')
        flag, msg = admin_interface.relieve_interface(
            relieve_user
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)
            continue
tab_dic ={
        "0":0,
        "1":frozen,
        "2":change_balance,
        "3":relieve,

}

def run():
    while True:
        print(
            '''
        =====欢迎进入管理员功能=====
        
        0、退出
        1、冻结功能
        2、修改余额功能
        3、解冻功能
        
        =====欢迎进入管理员功能=====
            '''

        )

        count = input("请输入要进行的操作编号:")

        if count in tab_dic:
            if count != "0" :
                tab_dic[count]()
            else:
                exit("退出成功，欢迎下次继续使用")
        else:
            print("请重新输入编号")
            continue