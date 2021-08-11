'''
数据处理层
    专门处理用户数据
'''
import os
import json
from conf import settings

def select(username):
    user_path = os.path.join(
        settings.USER_FILE_PATH,f'{username}.json'
    )
    if os.path.exists(user_path):
        with open(user_path,'rt',encoding='utf-8') as f:
            user_dic = json.load(f)
        return user_dic


def save(user_dic):
    username = user_dic['username']
    user_path = os.path.join(
        settings.USER_FILE_PATH, f'{username}.json'
    )
    with open(user_path,'wt',encoding='utf-8') as f:
        json.dump(user_dic,f,ensure_ascii=False)