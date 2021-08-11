from db import db_handler
from lib import common

user_logger = common.add_logger('user')


#注册接口
def register_interface(username,password,balance=15000):
    password = common.hash_password(password)
    user_dic = db_handler.select(username) #如果用户存在则为用户信息字典，否则为None
    if user_dic:
        return False,'用户已经存在！'
    else:
        user_dic = {
            'username':username,
            'password':password,
            'balance':balance,
            'flow':[],
            'shop_car':{},
            'frozen':False
        }
        db_handler.save(user_dic)
        user_logger.info(f'{username}注册成功！')
        return True,f'{username}注册成功！'

#登录接口
def login_interface(username,password):
    password = common.hash_password(password)
    user_dic = db_handler.select(username)

    if user_dic:
        if user_dic['password'] == password:
            if user_dic['frozen'] == True:
                return False,f'{username}已被冻结，请联系管理员解冻！'
            user_logger.info(f'{username}登录成功！')
            return True,f'{username}登录成功！'
        else:
            user_logger.warn(f'{username}密码输入错误！')
            return False,'密码输入错误！'
    else:
        return False,'用户不存在！'

#查看余额接口
def check_bal_interface(username):
    user_dic = db_handler.select(username)

    user_logger.info(f'{username}查看余额成功！')
    return user_dic['balance']

#查看流水接口
def check_flow_interface(username):

    user_dic = db_handler.select(username)
    flow = user_dic['flow']

    user_logger.info(f'{username}查看流水成功！')
    return flow
