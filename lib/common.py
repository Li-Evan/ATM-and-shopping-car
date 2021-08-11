import hashlib
import logging.config
from conf import settings

#登录认证装饰器
def login_auth(func):
    from core import src
    def wrapper(*args,**kwargs):
        if src.login_user == None:
            print('请优先进行登录！')
            src.login()
        else:
            res = func(*args,**kwargs)
            return res
    return wrapper

#密码加密
def hash_password(password):
    m = hashlib.md5()
    m.update('ev'.encode('utf-8'))
    m.update(password.encode('utf-8'))
    m.update('an'.encode('utf-8'))
    return m.hexdigest()

#添加日志功能
def add_logger(log_type):

    #加载日志配置信息
    logging.config.dictConfig(
        settings.LOGGING_DIC
    )

    #制定日志类型
    logger = logging.getLogger(log_type)
    return logger
