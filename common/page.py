# coding:utf-8
import time,requests
from common.logger import Log
from common.base import Base
from config import readConfig

class requestMethod(Base):

    # s = requests.session # 全局参数
    timestamp = (str(time.time()).replace('.', ''))[:-4]
    log = Log()
    base = Base()
    # def __init__(self,s):
    #     self.s = s

    # 登录公共用例
    # address：接口地址
    # account：登录账号
    # password：登录密码（MD5加密）
    def login(self,address,account,password):
        # 登录接口校验
        url = readConfig.url + address
        # 请求参数
        params = {"account":account,"password":password,"timestamp":self.timestamp}
        # 加密参数获取sign值
        sign = self.base.encrypt(params)
        # 完整请求参数
        params["sign"] = sign
        # 请求方法
        self.s = requests.post(url=url,params=params)

        if self.s.status_code == 200:
            self.log.info("【ADDRESS】：%s 【MESSAGE】：%s" %(address,self.s.json()))
            if self.s.json()["resultCode"]==200:
                # cookies
                self.Cookie = {}
                self.Cookie["Cookie"] = self.s.headers.get("Set-Cookie")
                # 保存token
                self.token = self.s.json()["data"]["token"]
                # 保存userId
                self.userId = self.s.json()["data"]["userId"]
            else:
                self.log.error("【ADDRESS】：%s 【MESSAGE】：%s" % (address, self.s.json()))
                return False
        else:
            self.log.error("【ADDRESS】：%s 【MESSAGE】：%s" %(address,self.s.text))
            return False
    
    # Get请求
    # address：接口地址
    # params：请求参数，可以为空
    def get(self, address, params=''):
        # 访问路径
        path = readConfig.url + address
        # 登录返回token以及userId，拼接成JSON
        loginData = {"token": self.token, "userId": self.userId, "timestamp": self.timestamp}
        # 请求参数 + 登录参数
        loginData.update(params)
        # 参数加密获取sign
        sign = self.base.encrypt(loginData)
        # 加上sign
        loginData["sign"] = sign
        # 请求接口
        self.s = requests.get(url=path, params=loginData,headers=self.Cookie)
        # self.log.info("【ADDRESS】：%s 【MESSAGE】：%s" % (address, self.s.text))
        if self.s.status_code == 200:
            self.log.info("【ADDRESS】：%s 【MESSAGE】：%s" %(address,self.s.json()))
        else:
            self.log.error("【ADDRESS】：%s 【MESSAGE】：%s" %(address,self.s.json()))
            return False

    # Post请求
    # address：接口地址
    # params：请求参数
    def post(self, address, params):
        # 访问路径
        path = readConfig.url + address
        # 登录返回参数
        loginData = {"token": self.token, "userId": self.userId, "timestamp": self.timestamp}
        # 请求参数 + 登录参数
        loginData.update(params)
        # 参数加密获取sign
        sign = self.base.encrypt(loginData)
        # 请求参数加上sign
        loginData["sign"] = sign
        # 请求方式
        self.s = requests.post(url=path, params=loginData,headers=self.Cookie)
        # self.log.info(self.s.text)
        # self.log.info("【ADDRESS】：%s 【MESSAGE】：%s" %(address,self.s.text))
        if self.s.status_code == 200:
            self.log.info("【ADDRESS】：%s 【MESSAGE】：%s" %(address,self.s.json()))
        else:
            self.log.error("【ADDRESS】：%s 【MESSAGE】：%s" %(address,self.s.text))
            return False
    def crearAccount(self,account,password,address="login_v2/signin"):
        path = readConfig.url + address
        params = {"account":account,"code":8432,"password":password,"repassword":password,"timestamp":self.timestamp}
        sign = self.base.encrypt(params)
        params["sign"] = sign
        self.s = requests.post(url=path,data=params,headers=self.Cookie)
        if self.s.status_code == 200:
            self.log.info("【ADDRESS】：%s 【MESSAGE】：%s" %(address,self.s.json()))
        else:
            self.log.error("【ADDRESS】：%s 【MESSAGE】：%s" %(address,self.s.text))
            return False

    def postNotNeedToken(self, address, params):
        path = readConfig.url + address
        sign = self.base.encrypt(params)
        params["sign"] = sign
        self.s = requests.post(url=path, data=params,)
        if self.s.status_code == 200:
            self.log.info("【ADDRESS】：%s 【MESSAGE】：%s" %(address,self.s.json()))
        else:
            self.log.error("【ADDRESS】：%s 【MESSAGE】：%s" %(address,self.s.text))
            return False

    def orgList(self,address="work_v2/organization/index",params=""):
    # 门店列表
        self.get(address,params)
        self.orgId = self.s.json()["data"]["list"][0]["id"]

    def upload(self, address, files):
        # 访问路径
        path = readConfig.url + address
        # 登录返回参数
        self.s = requests.post(url=path, files=files,headers=self.Cookie)
        if self.s.status_code == 200:
            self.log.info("【ADDRESS】：%s 【MESSAGE】：%s" %(address,self.s.json()))
        else:
            self.log.error("【ADDRESS】：%s 【MESSAGE】：%s" %(address,self.s.text))
            return False

if __name__ == "__main__":
    import requests
    requestMethod().login(address="login_v2/index",account="19667893203",password="c4ca4238a0b923820dcc509a6f75849b")
    requestMethod().orgList()
