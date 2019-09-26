# coding:utf-8
import os,configparser

cur_path = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(cur_path,"cfg.ini")
conf = configparser.ConfigParser()
conf.read(configPath,encoding='UTF-8')

# 发邮件配置
smtp_server = conf.get("email","smtp_server")
sender = conf.get("email","sender")
psw = conf.get("email","psw")
receiver = conf.get("email","receiver")
port = conf.get("email","port")
# 环境配置，test测试，live生产
url = conf.get("url","test")
# H5环境配置，test测试，live生产
H5URL = conf.get("h5Url","live")
# 账号配置
shopAccount = conf.get("loginUser","shopAccount")
shopPassword = conf.get("loginUser","shopPassword")
adminAccount = conf.get("loginUser","adminAccount")
adminPassword = conf.get("loginUser","adminPassword")
h5Account = conf.get("loginUser","h5Account")
h5Password =conf.get("loginUser","h5Password")
