from db import db_handler
from lib import common

bank_logger = common.add_logger('bank')

#提现接口（手续费5%）
def withdraw(username,money):
    user_dic = db_handler.select(username)
    balance = int(user_dic['balance'])
    money2 = int(money)*1.05
    if money2 > balance:
        bank_logger.warn(f"{username}提现金额超过账户余额，提现失败！")
        return False,f'提现金额超过账户余额，提现失败！'
    else:
        user_dic['balance'] = balance - money2
        flow = f'{username}提现{money}元成功！账户余额{user_dic["balance"]}元'
        user_dic['flow'].append(flow)
        db_handler.save(user_dic)

        bank_logger.info(f'{username}提现{money}元成功！账户余额{user_dic["balance"]}元')
        return True,flow

#还款接口
def repay_interface(username,money):
    user_dic = db_handler.select(username)
    user_dic['balance'] += money

    flow = f'{username}还款{money}元成功,账户余额{user_dic["balance"]}元'
    user_dic['flow'].append(flow)

    db_handler.save(user_dic)

    bank_logger.info(f'{username}还款{money}元成功,账户余额{user_dic["balance"]}元')
    return True,flow

#转账接口
def tranfer_interface(tranferor,receiver,money):

    money = float(money)

    tranferor_dic = db_handler.select(tranferor)
    receiver_dic = db_handler.select(receiver)
    tran_balance = tranferor_dic['balance']

    if receiver_dic:

        if tran_balance < money:
            bank_logger.warn(f'{tranferor}余额不足，转账失败!')
            return False,'余额不足，转账失败!'
        else:
            tranferor_dic['balance'] -= money
            receiver_dic['balance'] += money

            tran_flow = f'{tranferor}给{receiver}转账{money}元成功！账户余额{tranferor_dic["balance"]}元'
            tranferor_dic['flow'].append(tran_flow)
            re_flow = f'{receiver}接收到{tranferor}转账的{money}元成功！账户余额{receiver_dic["balance"]}元'
            receiver_dic['flow'].append(re_flow)

            db_handler.save(tranferor_dic)
            db_handler.save(receiver_dic)

            bank_logger.info(f'{tranferor}给{receiver}转账{money}元成功！账户余额{tranferor_dic["balance"]}元')
            return True,tran_flow

    return False,'转账用户不存在，转账失败'

#支付接口
def pay_interface(username,money):

    user_dic = db_handler.select(username)
    balance = user_dic['balance']

    if balance > float(money):

        user_dic['balance'] -= money


        flow = f'{username}消费{money}元成功，账户余额{user_dic["balance"]}元'
        user_dic['flow'].append(flow)

        db_handler.save(user_dic)

        bank_logger.info(f'{username}消费{money}元成功，账户余额{user_dic["balance"]}元')
        return True

    return False