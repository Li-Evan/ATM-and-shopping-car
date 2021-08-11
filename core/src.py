'''
用户视图层
'''
from  interface import user_interface,shopping_interface,bank_interface
from lib import common
from db import db_handler

login_user = None
# 1、注册功能
def register():
    while True:
        username = input('请输入用户名:')
        password = input('请输入密码:')
        re_password = input('请再次输入密码:')

        if password == re_password:
            #调用接口层函数
            flag,msg = user_interface.register_interface(
                username,password
            )
            if flag:
                print(msg)
                break
            else:
                print(msg)



# 2、登录功能
def login():
    while True:
        username = input('请输入用户名:')
        password = input('请输入密码:')
        flag,msg = user_interface.login_interface(
            username,password
        )
        if flag:
            print(msg)
            global login_user
            login_user = username
            break
        else:
            print(msg)


# 3、查看余额
@common.login_auth
def check_balance():

    balance = user_interface.check_bal_interface(
        login_user
    )

    print(f'{login_user}账户余额为{balance}元')

# 4、提现功能
@common.login_auth
def withdraw():
    while True:
        take_out_money = input('请输入要提现的金额:').strip()

        if not take_out_money.isdigit():
            print('请重新输入')
            continue

        flag,msg = bank_interface.withdraw(
            login_user,take_out_money
        )

        if flag:
            print(msg)
            break
        else:
            print(msg)

# 5、还款功能
@common.login_auth
def repay():

    while True:
        money = input('请输入要还款的金额:')

        if not money.isdigit():
            print('请输入正确金额！')
            continue

        money = int(money)
        if money > 0:
            flag,msg = bank_interface.repay_interface(
                login_user,money
            )
            if flag:
                print(msg)
                break
        else:
            print('请输入大于0的金额!')

# 6、转账功能
@common.login_auth
def transfer():
    while True:
        receiver = input('请输入要转账的对象:')
        tran_money = input('请输入要转账的金额:')

        if not tran_money.isdigit():
            print('请输入正确金额！')
            continue

        flag,msg = bank_interface.tranfer_interface(
            login_user,receiver,tran_money
        )

        if flag:
            print(msg)
            break
        else:
            print(msg)


# 7、查看流水
@common.login_auth
def check_flow():

    res = user_interface.check_flow_interface(
        login_user
    )

    for flow in res:
        print(flow)

# 8、购物功能
@common.login_auth
def shopping():
    shop_li = [
        ['asus', 7999],
        ['macbook', 9999],
        ['huawei', 6999],
        ['xiaomi', 5999],
        ['dell', 8999]
    ]
    shop_car_dic = {}

    while True:

        #打印商品列表给用户，并让用户选择
        for index,shop in enumerate(shop_li):
            print(f'商品编号:{index},名称:{shop[0]},价格:{shop[1]}')
        choice = input('请输入要添加进入购物车的商品编号(输入y结账，输入n加入购物车):')

        if choice == 'y':
            if shop_car_dic:
                flag,msg = shopping_interface.payback_interface(
                    login_user,shop_car_dic
                )
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)
                    continue
            else:
                print('购物车为空，请先添加商品！')
                continue

        if choice == 'n':
            if shop_car_dic:
                flag,msg = shopping_interface.add_shop_car_interface(
                    login_user,shop_car_dic
                )
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)
                    continue
            else:
                print('购物车为空，请先添加商品！')
                continue

        if not choice.isdigit():
            print('请输入正确编号！')
            continue

        choice = int(choice)
        if choice not in range(len(shop_li)):
            print('请输入正确编号！')
            continue

        #根据用户输入添加单次购物车

        name = shop_li[choice][0]
        price = shop_li[choice][1]

        if name not in shop_car_dic.keys():
            shop_car_dic[name] = [price,1]
            print(shop_car_dic)
        else:
            shop_car_dic[name][1] += 1
            print(shop_car_dic)



# 9、查看购物车
@common.login_auth
def check_shop_car():
    res = shopping_interface.check_shop_car_interface(
        login_user
    )
    print(res)

# 10、管理员功能
@common.login_auth
def admin():
    from core import admin
    admin.run()

# 主程序运行选项卡及代码
tab_dic ={
        "0":0,
        "1":register,
        "2":login,
        "3":check_balance,
        "4":withdraw,
        "5":repay,
        "6":transfer,
        "7":check_flow,
        "8":shopping,
        "9":check_shop_car,
        "10":admin,
}
def run():
    while True:
        print(
            '''
        0、退出
        1、注册功能
        2、登录功能
        3、查看余额
        4、提现功能
        5、还款功能
        6、转账功能
        7、查看流水
        8、购物功能
        9、查看购物车
        10、管理员功能
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