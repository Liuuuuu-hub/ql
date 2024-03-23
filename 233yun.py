'''
time：2024.3.23
cron: 55 5 * * *
new Env('233yun签到');
地址：https://233yun.xyz/
环境变量 233yun_data = 邮箱#密码
多账号新建变量或者用 & 分开
'''

import os
import requests
from bs4 import BeautifulSoup

# 获取环境变量中的账号和密码
account_password = os.environ.get('233yun_data')
if account_password:
    # 使用#号分割账号和密码
    account, password = account_password.split('#')
else:
    print('环境变量233yun_data未设置')
    exit(1)

# 定义签到函数
def sign_in():
    # 构造签到请求的URL和参数
    login_url = 'https://233yun.xyz/login'  # 请替换为实际的登录URL
    data = {
        'username': account,
        'password': password
    }

    # 发送签到请求
    response = requests.post(login_url, data=data)

    # 检查响应状态码
    if response.status_code == 200:
        # 签到成功后的处理逻辑
        print('签到成功')
    else:
        # 签到失败后的处理逻辑
        print('签到失败')

# 主函数
if __name__ == '__main__':
    sign_in()
```
