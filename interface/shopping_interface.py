from db import db_handler
from lib import common

shop_logger = common.add_logger('shop')

#购物车结账接口
def payback_interface(username,shop_car_dic):
    from interface import bank_interface

    total_money = 0
    for each_shop in shop_car_dic.values():
        total_money += each_shop[0]*each_shop[1]

    flag = bank_interface.pay_interface(
        username,total_money
    )

    if flag:
        shop_logger.info(f'{username}支付成功！')
        return True,'支付成功！'

    else:
        shop_logger.warn(f'{username}余额不足，支付失败！')
        return False,'余额不足，支付失败！'

#添加购物车接口
def add_shop_car_interface(username,shop_car_dic):

    user_dic = db_handler.select(username)
    exist_shop_car = user_dic['shop_car']

    for good,price_number in shop_car_dic.items():
        price = price_number[0]
        number = price_number[1]
        if good not in exist_shop_car:
            user_dic['shop_car'].update(
                {good:[price,number]}
            )

        else:
            user_dic['shop_car'][good][1] += number

    db_handler.save(user_dic)

    shop_logger.info(f'{username}购物车添加成功！')
    return True,'购物车添加成功!'

#查看购物车接口
def check_shop_car_interface(username):
    user_dic = db_handler.select(username)
    shop_car = user_dic['shop_car']

    shop_logger.info(f'{username}查看购物车成功！')
    return shop_car