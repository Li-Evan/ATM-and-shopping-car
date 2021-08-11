'''
管理员要实现的功能：
1.冻结账户
2.改变用户金额
3.解冻账户
'''
from db import db_handler
from lib import common

admin_logger = common.add_logger('admin')


def frozen_interface(username):

    user_dic = db_handler.select(username)
    if user_dic:
        user_dic["frozen"] = True
        db_handler.save(user_dic)

        admin_logger.info(f'{username}冻结成功！')
        return True,f'{username}冻结成功！'

    return False,f'用户不存在！'

def change_bal_interface(username,balance):
    balance = int(balance)
    user_dic = db_handler.select(username)

    if user_dic:
        user_dic['balance'] = balance
        db_handler.save(user_dic)

        admin_logger.info(f'修改{username}余额成功！')
        return True,'修改成功!'

    return False,'用户不存在！'

def relieve_interface(username):

    user_dic = db_handler.select(username)

    if user_dic:
        user_dic["frozen"] = False
        db_handler.save(user_dic)

        admin_logger.info(f'{username}解冻成功！')
        return True, f'{username}解冻成功！'

    return False, f'用户不存在！'
